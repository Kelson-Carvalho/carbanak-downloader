[app]
title = Carbanak Video Audio
package.name = carbanakapp
package.domain = org.kelson
version = 1.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Requirements otimizados para evitar erro de Broken Pipe e excesso de memória
requirements = python3,kivy==2.3.0,kivymd==1.2.0,yt-dlp,certifi,pillow,requests

orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
