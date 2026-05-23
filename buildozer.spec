[app]
# (str) Title of your application
title = Crypto Bot

# (str) Package name
package.name = cryptobot

# (str) Package domain (needed for android packaging)
package.domain = org.cryptobot

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# Crucial: This tells the compiler to download Kivy, ccxt, and SSL for secure network calls
requirements = python3,kivy==2.3.0,ccxt,openssl,requests,urllib3,certifi,charset-normalizer,idna

# (str) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (bool) Use fullscreen mode or not
fullscreen = 1

# (list) Permissions your app needs (Internet is required for a crypto bot!)
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) Architecture to build for (arm64-v8a covers almost all modern Android phones)
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
