## Django でなんちゃって検索

<br>

こんなプログラムです。

<img src="https://user-images.githubusercontent.com/44894526/187105751-1a4deaa2-34d8-4dde-a4d6-a24d1ccd8387.gif" width="80%">

<br>
<br>

### 特徴

* 検索文字列はスペースで区切って指定します（大文字、小文字どちらでも可）
* 検索文字列は正規表現が使えます（例: ``` 子$ ^[AB]型 ```） 
* データのアップローダが付いています（サンプルデータ sample.csv 付き）

<br>

### このプログラムを使うには

以下の操作を実行します。

1. リポジトリのクローン
1. 仮想環境の作成
1. settings_local.py の作成
1. マイグレーション
1. プログラムの起動
1. サンプルデータの取り込み

<br>

### リポジトリのクローン

1. 端末を開き、次のように入力します
   ``` bash
   git clone git@github.com:uhoogohan/uho_search.git
   ```
   このように出てくれば OK です
   ``` bash
   Cloning into 'uho_search'...
   remote: Enumerating objects: 114, done.
   remote: Counting objects: 100% (114/114), done.
   remote: Compressing objects: 100% (76/76), done.
   remote: Total 114 (delta 43), reused 99 (delta 28), pack-reused 0
   Receiving objects: 100% (114/114), 678.05 KiB | 962.00 KiB/s, done.
   Resolving deltas: 100% (43/43), done.
   ```
1. ベースディレクトリに移動します
   ```
   cd uho_search
   ```
   <br>

### 仮想環境の作成

1. 仮想環境を作ります
   ``` bash
   python3 -m venv venv
   ```
1. venv というディレクトリが作成されていることを確認します
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
1. 仮想環境をアクティベートします
   ``` bash
   source venv/bin/activate
   ```
1. requirements.txt よりモジュールをインストールします
   ``` bash
   pip install -r requirement.txt
   ```

<br>

### settings_local.py の作成

1. settings.py と同じディレクトリに移動します

   ``` bash
   cd uho_search
   ```
1. settings_local.py に、次の行を追加します
   ``` python
   echo "SECRET_KEY = 'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'" > settings_local.py
   ```
1. 下記の SECRET_KEY の生成方法より、新しい SECRET_KEY を生成して settings_local.py に上書きしてください。

<br>

#### SECRET_KEY の生成方法

1. ベースディレクトリに移動します
   ``` bash
   cd ..
   ```
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
1. 出てきた文字列をコピーしておきます
   ``` python
   'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
   ```
1. CTRL + D  でシェルを抜けます。
   ``` python
   ^D
   ```
1. settings_local.py の SECRET_KEY の右辺にコピペします
   ```
   SECRET_KEY = 'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
   ```

<br>

### マイグレーション

1. ベースディレクトリに戻ります
   ``` bash
   cd ..
   ```
1. 次のように入力します
   ``` bash
   python3 manage.py migrate
   ```
   これにより db.sqlite3 というファイルが作成されます。

<br>

### プログラムの起動

1. ウェブサーバを起動します
   ``` bash
   python3 manage.py runserver
   ```
1. 止めるときは Ctrl + C を押します
   ``` bash
   ^C
   ```
1. 仮想環境を止めます
   ``` bash
   deactivate
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
