[app]

# --- 基本情報 -----------------------------------------------------------

title = Driving Dynamics Analyzer
package.name = drivinganalyzer
package.domain = org.jl7khn
version = 1.5

# --- ソース -------------------------------------------------------------

source.dir = .
source.include_exts = py,json,txt,md
source.exclude_dirs = .git,.github,bin,.buildozer,**pycache**,dda_data,report

# --- 画面 ----------------------------------------------------------------

orientation = portrait
fullscreen = 0

# --- Python requirements ------------------------------------------------

requirements = python3,kivy,pyjnius

# --- アイコン/スプラッシュ ----------------------------------------------

#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# --- バックグラウンドサービス -------------------------------------------

services = DDAServer:service.py:foreground

# --- Android権限 --------------------------------------------------------

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,FOREGROUND_SERVICE,WAKE_LOCK

# --- API/アーキテクチャ --------------------------------------------------

android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

# --- Android SDKライセンス ----------------------------------------------

android.accept_sdk_license = True

# --- NDK / python-for-android -------------------------------------------

# Python 3.14環境でのp4aビルドを安定させるためdevelopを使用

p4a.branch = develop

# NDKはBuildozer側の環境に合わせる

#android.ndk = 28c

[buildozer]
log_level = 2
warn_on_root = 1
