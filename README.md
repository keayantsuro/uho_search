## Django でなんちゃって検索フォーム

<br>

<img src="https://cdn-ak.f.st-hatena.com/images/fotolife/u/uhoo/20210209/20210209211826.gif" width="60%">

<br>
<br>

### 特徴

* 検索文字列はスペースで区切って指定します（大文字、小文字どちらでも可）
* 検索文字列は正規表現が使えます（例:子$ [BA]型 -> 名前が子で終わり、血液型がBかA型） 
* CSV のアップローダが付いています（サンプルデータ sample.csv 付き）


<br>

### settings_local.py について

下記の手順で、settings_local.py に追加してください。
<br>

* SECRET_KEY
* NPM_BIN_PATH


<br>

### SECRET_KEY の生成方法

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

<br>

### NPM_PATH について

* Windows の場合は ``` gcm npm | select source``` 
* Linux の場合は ``` which npm ```

と打って出てきた文字列を NPM_BIN_PATH の右辺にコピペします

<br>

例）settings_local.py
``` python
SECRET_KEY = 'p8tohlyf4#2&7i%ts!9r&p*s-fn*p76@2kiwpj6-*a&33dx155'
NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'
```
<br>

### マイグレーションの手順

``` bash
python manage.py makemigrations
python manage.py migrate
```

<br>

### サンプルデータについて

kazina.com 様の [なんちゃって個人情報](http://kazina.com/dummy/index.html) から頂きました。

<br>

### データの作り方

1. サイトに移動します
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

dummy.cgi の文字コードセットは、Shift_Jis 形式なので、UTF-8 に変換します。
<br>
例）
``` bash
nkf -w8 dummy.cgi > sample.csv
```
<br>
おわり
