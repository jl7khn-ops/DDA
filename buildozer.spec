[app]

# --- 基本情報 -----------------------------------------------------------
title = Driving Dynamics Analyzer
package.name = drivinganalyzer
package.domain = org.jl7khn
version = 1.5

# --- ソース ---------------------------------------------------------------
source.dir = .
source.include_exts = py,json,txt,md
source.exclude_dirs = .git,.github,bin,.buildozer,__pycache__,dda_data,report

# --- 画面 -------------------------------------------------------------------
orientation = portrait
fullscreen = 0

# --- Python requirements ---------------------------------------------------
# Kivy + pyjnius の最小構成。dda_core.py は標準ライブラリのみで動作。
requirements = python3,kivy,pyjnius

# --- アイコン/スプラッシュ -------------------------------------------------
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# --- バックグラウンドサービス ---------------------------------------------
# 走行中に画面を切り替えても解析ループが継続するフォアグラウンドサービス。
services = DDAServer:service.py:foreground

# --- Android 権限 -----------------------------------------------------------
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,FOREGROUND_SERVICE,WAKE_LOCK

# --- API / アーキテクチャ ---------------------------------------------------
# API 33 はフォアグラウンドサービス種別宣言が不要な最後の世代で安定。
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

# --- p4a / NDK --------------------------------------------------------------
# Buildozer公式Dockerイメージの既定値に委ねる（最もビルド成功率が高い）。
#android.ndk = 25b
#p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
