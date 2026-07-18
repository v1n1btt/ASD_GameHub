[app]
title = Leitura Social
package.name = leiturasocial
package.domain = org.leiturasocial

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

# Deixa o app travado em modo retrato (celular na vertical)
orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/assets/mia.png

[buildozer]
log_level = 2

[app:android]
android.permissions = 
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
