[app]

# (str) Title of your application
title = Carbanak Video Audio

# (str) Package name
package.name = carbanakapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Adicionado yt-dlp, certifi, pillow (para as imagens) e as libs do Kivy
requirements = python3,kivy==2.3.0,kivymd==1.2.0,yt-dlp,certifi,pillow,requests,urllib3,chardet,idna

# (str) Custom source folders for requirements
# (list) Garden requirements
# (str) Presplash of the application
# (str) Icon of the application
# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) Permissions
# INTERNET para busca e WRITE para salvar na pasta Download
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android entry point, default is main.py
python_fallback = False

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpython.so
android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# Para o GitHub Actions, geralmente compilamos para essas duas:
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
