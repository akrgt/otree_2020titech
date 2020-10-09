## oTreeでオンライン実験の実施環境を作って，実験をやってみよう．



## 今日やること

### 絶対にやること

* サーバへのGoogle Chromeのインストール
* AnacondaによるPythonのインストール
* PostgreSQLのインストール
* Redisのインストール
* Anaconda Powershellを用いたoTreeのインストール
* Settings.pyでの設定
* Firewallの設定

### 余裕があればやりたいこと

* Rooms機能の説明

## 今日できないこと

* Amazon EC2の初期設定
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




### サーバ上での作業
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

  

* 以上でPostgreSQLのインストールは終了です．





## Redisのインストール

引き続き，Redisのインストールを行います．

Redisに関する細かい説明は，以下の参考資料をご確認ください．

* https://qiita.com/tomu28/items/8f13145bd8d45523a195
* https://agency-star.co.jp/column/redis/

### Redisのダウンロード



### Redisのインストール

* https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100よりダウンロードをします．

![27](picture/27.png)



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



* All ConnectionをAllowします．







## Anaconda Powershellを用いたoTreeのインストール

![42](picture/42.png)

* これを右クリックして"Pin to Start"にしておくとこれからの作業が便利です．

* oTreeをインストールするために，以下のコード入力します．

  ````
  pip install -U otree
  ````

* あわせて，PostgreSQLを使うために，'psycopg2'をインストールします．

* 作業のために，Visual Studio Codeを入れます．

* よく見ると，visual C++が求められるかも

* 素直に従いましょう．

https://visualstudio.microsoft.com/ja/vs/features/cplusplus/



インストールしないとまずいみたい．







## Settings.pyでの設定

* ここではデスクトップで'otreetest'という新しいプロジェクトを作って，作業する場合を例とします．

```
cd Desktop
otree startproject otreetest
```







### PostgreSQL関係の設定

　'environ['DATABASE_URL'] = 'postgres://postgres:test@localhost/django_db''







### Redis関係の設定

## 

environ['REDIS_URL'] = 'redis://localhost:6379'



## DEBUG modeの切り替え



### パスワードの設定





## Rooms機能の説明

