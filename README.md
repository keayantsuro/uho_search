## Django でなんちゃって検索

<br>

こんなプログラムです。


<img src="https://cdn-ak.f.st-hatena.com/images/fotolife/u/uhoo/20210209/20210209211826.gif" width="60%">

<br>
<br>

### 特徴

* 検索文字列はスペースで区切って指定します（大文字、小文字どちらでも可）
* 検索文字列は正規表現が使えます（例: 名前が子で終わり、血液型がAかB型のとき ``` 子$ ^[AB]型 ```） 
* CSV のアップローダが付いています（サンプルデータ sample.csv 付き）


<br>

### このプログラムを使うには

以下の３つの操作を実行します。

* settings_local.py を作成する
* マイグレーション
* サンプルデータの取り込み

<br>

#### settings_local.py を作成する

1. settings_local.py を追加して、次の行をコピペしてください。

   ``` python
   SECRET_KEY = 'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
   ```
1. 下記の SECRET_KEY の生成方法より、新しい SECRET_KEY を生成して settings_local.py に上書きしてください。

<br>

#### SECRET_KEY の生成方法

1. シェルを起動します
   ``` bash
   python manage.py shell
   ```
1. インポートします
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
1. CTRL + Z + Enter でシェルを抜けます。
   ``` python
   ^Z
   ```

<br>

### マイグレーション

``` bash
python manage.py migrate
```
これにより db.sqlite3 というファイルが作成されます。

<br>

### サンプルデータの取り込み

付属の [sample.csv](./sample.csv) を、以下の手順で取り込みます。

1. このプログラムを起動します ``` python manage.py runserver ```
1. ブラウザから http://localhost:8000 を開きます
1. 右上の三本線のマークをクリックし、アップロードをクリック
1. 参照ボタンをクリックして [sample.csv](./sample.csv) を選択して開く
1. アップロードボタンをクリック

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
