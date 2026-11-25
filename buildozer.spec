[app]
title = نظام كاشير سوبر ماركت
package.name = supermarketpos
package.domain = org.supermarket

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
source.main = app_final.py

version = 3.0.0

requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0

# Use a stable p4a release instead of the moving develop branch
p4a.branch = v2024.01.21

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
