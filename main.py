import threading
import yt_dlp
import os
import certifi
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import AsyncImage
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import platform

# Configuração SSL para evitar erros de conexão no Android
os.environ['SSL_CERT_FILE'] = certifi.where()

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "CARBANAK VIDEO E AUDIO"
            anchor_title: "center"
            elevation: 2
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "15dp"
            MDTextField:
                id: search_field
                hint_text: "Nome do vídeo"
                mode: "fill"
                on_text_validate: app.iniciar_busca(self.text)
            MDCard:
                id: result_card
                orientation: "vertical"
                padding: "10dp"
                size_hint: 0.95, None
                height: "300dp"
                pos_hint: {"center_x": .5}
                radius: [20,]
                elevation: 2
                opacity: 0
                AsyncImage:
                    id: video_thumbnail
                    size_hint_y: 0.7
                    allow_stretch: True
                MDLabel:
                    id: video_title
                    text: ""
                    halign: "center"
                    bold: True
            MDLabel:
                id: status_log
                text: "Status: Aguardando..."
                halign: "center"
                theme_text_color: "Secondary"
                font_style: "Caption"
            MDFillRoundFlatButton:
                text: "BAIXAR MP4"
                size_hint_x: 1
                on_release: app.iniciar_download("mp4")
            MDFillRoundFlatButton:
                text: "BAIXAR ÁUDIO"
                size_hint_x: 1
                on_release: app.iniciar_download("m4a")
                md_bg_color: 0.2, 0.6, 1, 1
'''

class CarbanakApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.current_video_url = None
        if platform == 'android':
            self.request_android_permissions()
        return Builder.load_string(KV)

    def request_android_permissions(self):
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

    def iniciar_busca(self, query):
        if not query: return
        self.root.ids.result_card.opacity = 1
        self.root.ids.status_log.text = "Buscando..."
        threading.Thread(target=self.processar_busca, args=(query,), daemon=True).start()

    def processar_busca(self, query):
        ydl_opts = {'quiet': True, 'no_warnings': True, 'nocheckcertificate': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch1:{query}", download=False)['entries'][0]
                self.current_video_url = info.get('webpage_url')
                titulo = info.get('title')
                thumb = info.get('thumbnail')
                Clock.schedule_once(lambda dt: self.atualizar_ui(titulo, thumb))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.mostrar_mensagem(f"Erro: {str(e)[:30]}"))

    def atualizar_ui(self, titulo, thumb):
        self.root.ids.video_title.text = titulo[:50]
        self.root.ids.video_thumbnail.source = thumb
        self.root.ids.status_log.text = "Pronto!"

    def mostrar_mensagem(self, texto):
        self.root.ids.status_log.text = texto

    def iniciar_download(self, tipo):
        if not self.current_video_url: return
        self.mostrar_mensagem("Baixando...")
        threading.Thread(target=self.executar_download, args=(tipo,), daemon=True).start()

    def executar_download(self, tipo):
        if platform == 'android':
            from android.storage import primary_external_storage_path
            folder = os.path.join(primary_external_storage_path(), 'Download')
        else:
            folder = os.path.join(os.path.expanduser('~'), 'Downloads')

        os.makedirs(folder, exist_ok=True)
        output = os.path.join(folder, '%(title)s.%(ext)s')
        ydl_opts = {
            'outtmpl': output, 'quiet': True, 'no_warnings': True,
            'format': 'bestaudio[ext=m4a]/best' if tipo == "m4a" else 'best'
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.current_video_url])
            Clock.schedule_once(lambda dt: self.mostrar_mensagem("SUCESSO!"))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.mostrar_mensagem("Erro no download"))

if __name__ == "__main__":
    CarbanakApp().run()
