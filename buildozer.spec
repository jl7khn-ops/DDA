[app]

# --- 基本情報 -----------------------------------------------------------
title = Driving Dynamics Analyzer
package.name = drivinganalyzer
package.domain = org.jl7khn
version = 1.5

# --- ソース -------------------------------------------------------------
source.dir = .
source.include_exts = py,json,txt,md
source.exclude_dirs = .git,.github,bin,.buildozer,__pycache__,dda_data,report

# --- 画面 ----------------------------------------------------------------
orientation = portrait
fullscreen = 0

# --- Python requirements -------------------------------------------------
requirements = python3,kivy,pyjnius

# --- アイコン/スプラッシュ -----------------------------------------------
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# --- バックグラウンドサービス --------------------------------------------
services = DDAServer:service.py:foreground

# --- Android権限 ---------------------------------------------------------
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,FOREGROUND_SERVICE,WAKE_LOCK

# --- API/アーキテクチャ ---------------------------------------------------
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

# --- Android SDKライセンス ------------------------------------------------
android.accept_sdk_license = True

# --- NDK / python-for-android --------------------------------------------
# Buildozer公式Dockerイメージの環境に合わせるため固定しない
#android.ndk = 25b
#p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
