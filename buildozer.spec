[app]

# (str) Title of your application
title = Carbanak Video Audio

# (str) Package name
package.name = carbanakapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Version of your application (OBRIGATÓRIO)
version = 0.1

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Adicionado yt-dlp, certifi, pillow e dependências de rede
requirements = python3,kivy==2.3.0,kivymd==1.2.0,yt-dlp,certifi,pillow,requests,urllib3,chardet,idna

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) Permissions
# INTERNET para busca e STORAGE para salvar os arquivos
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Aceitar licenças automaticamente para evitar erro no GitHub
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a libpython.so
android.copy_libs = 1

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
