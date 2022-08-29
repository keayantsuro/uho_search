## Django でなんちゃって検索

<br>

こんなプログラムです。

<img src="https://user-images.githubusercontent.com/44894526/187105751-1a4deaa2-34d8-4dde-a4d6-a24d1ccd8387.gif" width="60%">

<br>
<br>

### 特徴

* 検索文字列はスペースで区切って指定します（大文字、小文字どちらでも可）
* 検索文字列は正規表現が使えます（例: ``` 子$ ^[AB]型 ```） 
* データのアップローダが付いています（サンプルデータ sample.csv 付き）

<br>

### このプログラムを使うには

以下の操作を実行します。

1. 仮想環境の作成
1. settings_local.py の作成
1. マイグレーション
1. プログラムの起動
1. サンプルデータの取り込み

<br>

### 仮想環境の作成

1. python の仮想環境を作ります
   ``` bash
   python3 -m venv venv
   ```
1. venv というフォルダが作成されていることを確認します
   ``` bash
   ls -l venv
   ```
   このように出てくれば OK です
   ``` bash
   drwxrwxr-x 5 uhoo uhoo  7  8月 28 13:32 ./
   drwxrwxr-x 8 uhoo uhoo 13  8月 28 13:32 ../
   drwxrwxr-x 2 uhoo uhoo 12  8月 28 13:32 bin/
   drwxrwxr-x 2 uhoo uhoo  2  8月 28 13:32 include/
   drwxrwxr-x 3 uhoo uhoo  3  8月 28 13:32 lib/
   lrwxrwxrwx 1 uhoo uhoo  3  8月 28 13:32 lib64 -> lib/
   -rw-rw-r-- 1 uhoo uhoo 70  8月 28 13:32 pyvenv.cfg
   ```
2. requirements.txt よりモジュールをインストールします
   ``` bash
   pip install -r requirement.txt
   ```

<br>

### settings_local.py の作成

1. settings.py と同じフォルダに settings_local.py を追加して、次の行をコピペします

   ``` python
   SECRET_KEY = 'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
   ```
1. 下記の SECRET_KEY の生成方法より、新しい SECRET_KEY を生成して settings_local.py に上書きしてください。

<br>

#### SECRET_KEY の生成方法

1. シェルを起動します
   ``` bash
   python3 manage.py shell
   ```
1. get_random_secret_key をインポートします
   ``` python
   from django.core.management.utils import get_random_secret_key
   ```
1. キーを生成します
   ``` python
   get_random_secret_key()
   ```
1. 出てきた文字列を settings_local.py の SECRET_KEY の右辺にコピペします
   ``` python
   'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
   ```
1. CTRL + D  でシェルを抜けます。
   ``` python
   ^D
   ```

<br>

### マイグレーション

``` bash
python3 manage.py migrate
```
これにより db.sqlite3 というファイルが作成されます。

<br>

### プログラムの起動

1. 仮想環境をアクティベートします
   ``` bash
   source venv/bin/activate
   ```
2. ウェブサーバを起動します
   ``` bash
   python manage.py runserver
   ```
   

<br>

### サンプルデータの取り込み

付属の [sample.csv](./sample.csv) を、以下の手順で取り込みます。

1. ブラウザから http://localhost:8000 を開きます
1. 右上の Upload をクリックします
1. 参照ボタンをクリックして [sample.csv](./sample.csv) を選択して開きます
1. アップロードボタンをクリックします

<br>

#### データの作り方

このデータは、kazina 様の [なんちゃって個人情報](http://kazina.com/dummy/index.html) から頂きました。


1. なんちゃって個人情報を開きます
1. 出力形式: CSV を選択します
1. オプションは次を選択します
   * 名前
   * フリガナ
   * メールアドレス
   * 性別
   * 誕生日
   * 血液型
   * 都道府県
   * 電話番号
1. なんちゃって生成ボタンを押します
1. ~/ダウンロード に dummy.cgi がダウンロードされます

<br>

##### ご注意

ダウンロードされた dummy.cgi の文字コードセットは、Shift_Jis 形式なので、UTF-8 の**BOM付き**に変換してください。

<br>

例）

``` bash
nkf -w8 dummy.cgi > sample.csv
```

<br>
おわり
