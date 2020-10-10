## oTreeでオンライン実験の実施環境を作って，実験をやってみよう．



## 今日やること

### 絶対にやること

* サーバへのGoogle Chromeのインストール
* AnacondaによるPythonのインストール
* PostgreSQLのインストール
* Redisのインストール
* Firewallの設定
* Anaconda Powershellを用いたoTreeのインストール
* Visual C++のインストール（必要な場合と不要な場合がある模様）
* Settings.pyでの設定

### 余裕があればやりたいこと

* Rooms機能

## 今日できないこと

* Amazon EC2におけるIPアドレスの設定
* Amazon Route 53によるドメイン登録・DNS管理

---

## 今回使うサーバ：

* Amazon Web Service EC2
  * Microsoft Windows Server 2019 Base(64GB)
  * c5.9xlarge
    * 開発時はここまでスペックを上げなくても良いですが，今回はセミナー用ということでスペックアップしています．
    * セキュリティグループで80番ポートを開いておきます．



## 手順

---
### Amazon上での初期設定
* Amazon EC2の初期設定
  * 参考資料：https://qiita.com/leomaro7/items/8560bfbeb0672d0d83ec
* Amazon EC2におけるIPアドレスの設定
  * 参考資料：https://qiita.com/Jerid/items/d5dd3a29ed9a0e374493
* Amazon Route 53によるドメイン登録・DNS管理
  * 参考資料：https://qiita.com/leomaro7/items/8560bfbeb0672d0d83ec

---

ここまでは別途WEB等で公開されている資料をご確認ください．

## Amazon EC2におけるサーバの作成

### サーバの準備

* アカウントの取得等は各自で行っておいてください．

![57](picture/57.png)

* Linuxは苦手なので，windowsサーバを使います．

![58](picture/58.png)

* 今回はかなりスペックの高いものを使います．
  * セミナー用なので．クラウドソーシングなどを用いた大規模実験ではない限りは，ここまでのスペックはいりません．

![59](picture/59a.png)

* 特に設定することがありません．

![60](picture/60.png)

* 特に設定することがありません．

![61](picture/61.png)

* 特に設定することがありません．

![62](picture/62.png)

* 80番ポート（http）を開いておきます．

![63](picture/63.png)

* 一通り確認しておきましょう．
  * 以上でサーバの起動は終了です．

![64](picture/64.png)



### サーバへのアクセス

* 枠のところをクリックします．

![65](picture/65.png)

* クリックします．

![66](picture/66.png)

* 「RDPクライアント」をクリックします．
* さらに，「リモートデスクトップファイルのダウンロード」をクリックします．
  * ダウンロードしたファイルを開きます．
  * macの方はリモートデスクトップのアプリケーションをインストールしておきましょう，
    * https://apps.apple.com/jp/app/microsoft-remote-desktop/id1295203466?mt=12
  * Windowsの方はそのままアクセスできるかと思います．
* そして，「パスワードを取得」をクリックします．

![67](picture/67.png)

* 別途発行したpemファイルをアップするか，開いてテキストとして貼り付けます．
* そして，「パスワードを復号化」をクリックします．

![68](picture/68.png)

* パスワードが復号化されたので，コピーします．

![69a](picture/69a.png)

* 先程ダウンロードしたファイルを開いて，パスワード入力します．

  

![70](picture/70.png)



* 作業は以上で終了です．



## Google Chromeのインストール

* サーバへのGoogle Chromeをインストールする
  * セキュリティの観点からサーバにブラウザは追加しない方がよいとは思いますが，検証作業やPostgreSQLの設定には，やはりブラウザが必要です．
  * 以下のコードをpowershellに打ち込むとGoogle Chromeをインストールしてくれます．

```sh
$Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26browser%3D0%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26brand%3DGTPM/update2/installers/ChromeSetup.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer
```

出典：https://qiita.com/Arahabica/items/04f8469842f29550b831

![1](picture/1.png)

* これを叩くとGoogle Chromeが表示されます．

![2](picture/2.png)



## AnacondaによるPythonのインストール

### Anacondaのダウンロード

* https://www.anaconda.com/products/individual よりダウンロードをします．

  

  ![3](picture/3.png)



### Anacondaのインストール

![4](picture/4.png)

![5](picture/5.png)



![6](picture/7.png)



![7](picture/7.png)



![8](picture/8.png)

* ここでチェックを入れると，powershellやcommand promptでデフォルトのpythonとして使われます．

![9](picture/9a.png)

![10](picture/10.png)



![11](picture/11.png)

* ここではとりあえずチェックを外しておきます．

  



* 以上でAnacondaのインストールは終了です．



## PostgreSQLのインストール

* oTreeにはもともとSQLiteが入っているが，実際の実験の時には安定しないので，PostgreSQLをインストールすることが推奨されています．
  * [参考](https://otree.readthedocs.io/en/latest/server/server-windows.html#install-redis)

### PostgreSQLのダウンロード

* https://www.enterprisedb.com/downloads/postgres-postgresql-downloadsよりダウンロードをします．

![12](picture/12.png)

### PostgreSQLのインストール

![13](picture/13.png)



![14](picture/14.png)



![15](picture/15.png)

* ここは一度全部入れておくことをオススメします．

![16](picture/16.png)

![17](picture/17.png)

* ここでパスワードの設定が必要です．忘れたらとんでもなくめんどくさいことになるので，ご注意ください．
  * ここでは"test"にしておきます．

![18](picture/18.png)

* portも初期設定の"5432"で構いません．



![19](picture/19a.png)

* 日本にしておきましょう．



![20](picture/20.png)



![21](picture/21.png)



![22](picture/22.png)



### PostgreSQLの設定

![23](picture/23.png)

* oTree用のデータベースを設定するために，pgAdminを設定します．

![24](picture/24.png)

* 最初にパスワードの入力が求められるので，先程設定したものを入力します．
* それ以降，聞かれるたびに入れましょう．

![25](picture/25.png)

* ここでは新規のデータベースを作成します．
  * 'django_db'という名前にしておきましょう．

![26](picture/26.png)



* これで"Save"をクリックしてください．

  

* 続いて，`pg_hba.conf`ファイルを変更します．

  * デフォルト設定のままでインストールしていたら，`C:\Program Files\PostgreSQL\`の中のどこかにあります．
  * 今回はPostgreSQL13を使っているので`C:\Program Files\PostgreSQL\13\data`にありました．

![46](picture/46.png)

* 上記の通り，86/88行目を`trust`に変更しました．

  * しかし，oTreeのページではデフォルトである`md5`から`trust`への変更が求められていましたが，デフォルトが`scram-sha-256`になっていたので，PostgreSQL13では違うのかもしれません．
  * 変更しなくても良いかもしれませんが，念のためマニュアルに沿っておきました．
    * [参考](https://otree.readthedocs.io/en/latest/server/server-windows.html#database-postgres)

  

* 以上でPostgreSQLのインストールは終了です．





## Redisのインストール

引き続き，Redisのインストールを行います．

Redisに関する細かい説明は，以下の参考資料をご確認ください．

* https://qiita.com/tomu28/items/8f13145bd8d45523a195
* https://agency-star.co.jp/column/redis/

### Redisのダウンロード

* https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100よりダウンロードをします．

![27](picture/27.png)



### Redisのインストール

![28](picture/28.png)



![29a](picture/29a.png)



![30](picture/30.png)



![31](picture/31.png)



![32](picture/32.png)



![33](picture/33.png)

![34](picture/34.png)



* Redisのインストールは以上です．





## Firewallの設定

引き続き，ファイヤーウォールの設定をします．

![35](picture/35.png)

* これで検索してあげてください．

![36](picture/36.png)



![37](picture/37.png)



![38](picture/38.png)



![39](picture/39a.png)



![40](picture/40.png)





## Anaconda Powershellを用いたoTreeのインストール

![42](picture/42.png)

* これを右クリックして"Pin to Start"にしておくとこれからの作業が便利です．

* oTreeをインストールするために，以下のコード入力します．

  ````
  pip install -U otree
  ````

* あわせて，PostgreSQLを使うために，'psycopg2'をインストールします．

  ```
  pip install -U psycopg2
  ```



* 以上でoTreeのインストールは終了です．
  * ただし，今回はこのあとoTreeを走らせてみようとしたら，Visual C++のインストールが求められました．
  * https://otree.readthedocs.io/en/latest/install-windows.html に記載されている通り，入れてみます．ただ，どういう条件で発動するのかがイマイチわかっていません．



## Visual C++のインストール

### Visual C++ のダウンロード

* https://visualstudio.microsoft.com/ja/vs/features/cplusplus/よりダウンロードします．

![43](picture/43.png)

### Visual C++ のインストール

* 今回は一度インストールしてから入れ直してしまったので，スクショを入れられていません．改めてアップしますので，お許しください．







## Settings.pyでの設定

* 作業のために，IDE（私は最近[Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)派）を入れておきましょう．
  * この後の作業が便利です．
* ここではデスクトップで'otreetest'という新しいプロジェクトを作って，作業する場合を例とします．

```
cd Desktop
otree startproject otreetest
```



* さらに，実際に実験を行うために，`settings.py`で以下の設定が必要になります．



### PostgreSQL関係の設定

* データベースの設定をしておきます．
  * 先程設定したユーザ名とパスワードで入れておきます．

```
environ['DATABASE_URL'] = 'postgres://postgres:test@localhost/django_db'
```



### Redis関係の設定

* oTree3.0から設定が求められるようになりました．
  * [参考](https://otree.readthedocs.io/en/latest/server/server-windows.html#install-redis)

```
environ['REDIS_URL'] = 'redis://localhost:6379'
```



### AUTH_LEVELの設定

* これを設定しないと「実験モード」にならない＝ユーザ名とパスワードの設定が有効になりません．

```
AUTH_LEVEL = 'STUDY'
```



### ユーザ名とパスワードの設定

* 環境変数での設定の方が安全であるようですが，実際にはこちらsettings.pyに書き込むだけで十分かと思います．
  * ここでは`admin`というユーザ名で，`test`というパスワードを設定します．

```
ADMIN_USERNAME = 'admin'

ADMIN_PASSWORD = 'test'
```



![47](picture/47.png)



### DEBUG modeの切り替え

* デバッグモードがオンだと，実験画面にデバッグ情報が表示されてしまいます．

![48](picture/48.png)

* 実際の実験には不要な情報なので，以下のようにします．

```
DEBUG = False
```

* 上記の設定をすることで，以下のようにデバッグ情報を削除することが出来ます．

### ![49](picture/49a.png)

### 



* 適宜，`Server Check`を確認して，問題がないかを確認しましょう．



![50](picture/50.png)

![51](picture/51.png)





## Rooms機能

* Rooms機能を設定すると，こちらで実験参加者IDを設定することが出来ます．
* 経済実験の実施にはこちらで「ID」を発行して，webサイト上で入力をしてもらうことが大半になるかと思います．
  * IDで個人を指定しなければ，成果報酬の支払いが困難になる．

### ID指定ファイルの用意

* oTreeのプロジェクトフォルダの中にある`_room`の中にIDを記録したtxtファイルを作成します．
  * 今回は`trial`という名前のroomを作成して，1-20までのIDを設定しました．
  * アルファベットを設定することも出来ます．
    * 日本語は試したことがありません．．．

![52](picture/52.png)

* ID指定ファイルの作成は以上です．

### settings.py上の作業

* `settings.py` に以下を指定します．

```
ROOMS = [
    dict(
        name='trial',
        display_name='トライアル',
        participant_label_file='_rooms/trial.txt',
    ),
    dict(name='live_demo', 
    display_name='IDを指定しない（好きに入れる）ことも可能'),
]
```



### oTreeページにアクセスしてからの作業

* `Rooms`にアクセスします．

  ![53](picture/53.png)

  

* トライアルをクリックします．

  ![54](picture/54.png)

  

* このページで実施するアプリケーションと参加する人数を設定します．

  * ここで設定する人数はトータルでの実験参加者数です．
  * 実施するアプリケーションで設定されている人数の倍数である必要があります．
  * Ex.3人で実施する実験ならば，3，6，9...人でなければなりません．
  * `create`をクリックすると準備が出来ます．

![55](picture/55.png)



* http://実験用のURL/room/trial/にアクセスします．
  * 赤枠の中にIDを入力してもらうと，実験にアクセスすることが出来ます．

![56](picture/56.png)



* 日本語化する場合には，`settings.py`の`LANGUAGE_CODE = 'en'`を`LANGUAGE_CODE = 'ja'`にしておきましょう．
* このページ自体を変更するのは多少ややこしいので，オススメしません．
  * 実は`C:\ProgramData\Anaconda3\Lib\site-packages\otree\templates\otree`にある`RoomInputLabel.html`を書き換えれば変更できる，
  * 個人的には，`Base.html` にweb解析ツールを仕込むことが多い．
  * ここに入れておけば，全てのoTreeページでの動きを解析できるのでかなり便利である．



## お疲れさまでした．