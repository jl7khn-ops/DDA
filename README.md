# Driving Dynamics Analyzer (DDA) — Android APK ビルド一式

- このAPKは**HTTPサーバーとして動作しブラウザ経由で操作する**設計です
  (元のDDAの設計をそのまま踏襲)。ネイティブなAndroid UIではありません。
- センサー実測値の取得は本APK単体では行わず、別アプリ「Sensor Server」
  経由です(元の仕様通り)。
- `android.api = 33` としているため、Google Play Storeへ配信する場合は
  最新のターゲットAPI要件に合わせて追加対応(フォアグラウンドサービス種別の
  宣言等)が必要です。個人利用(サイドロード)であれば現状のままで問題ありません。
