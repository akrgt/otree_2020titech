# プログラム⑤：公共財ゲームの改良


## これから作る実験プログラムの概要：

* 先程作った公共財ゲームを元に，以下の変更を試みる．
  * 入力方法の変更
    * 数字で入力する方法
    * select形式で入力する方法
    * ラジオボタン（縦長）で入力する方法
    * ラジオボタン（横長）で入力する方法
    * Sliderで入力する方法
    * ボタンで入力する方法（バイナリーチョイス）



## 数字で入力する方法
```Python
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label="あなたはいくら貢献しますか？"
    )
```
* widgetsの指定を特にしなければ，数字を直接入力する形式になります．


## 選択式で入力する方法

```Python
  contribution = models.CurrencyField( 
      choices=currency_range(c(0), c(Constants.endowment), c(1)), 
      label="あなたはいくら貢献しますか？"
  )
```
* `choices`を指定すると，自動的に選択式で入力することができます．


## ラジオボタン（垂直）で入力する方法

```Python
    contribution = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)), 
        label="あなたはいくら貢献しますか？",
        widget=widgets.RadioSelect
    )
```
* `widget=widgets.RadioSelect`を指定することで，ラジオボタン（垂直）で入力できます．


## ラジオボタン（水平）で入力する方法


```Python
    contribution = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)), 
        label="あなたはいくら貢献しますか？",
        widget=widgets.RadioSelectHorizontal
    )
```
* `widgets.RadioSelectHorizontal`を指定することで，ラジオボタン（水平）で入力できます．


## Sliderで入力する方法①

```Python
class Player(BasePlayer):
    contribution = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)),
	min = 0,
	max = 20,
	initial=10,
        label="あなたはいくら貢献しますか？",
        widget=widgets.SliderInput
    )
```
* `widgets.SliderInput`を使うとスライダー形式で入力ができる．
  * 大川内さんありがとうございます！
  * 完璧にできました！！


## Sliderで入力する方法②

### Page1.htmlを書き換える
```html

    <input type="range" name="contribution" min="1" max="20" step="1"> [{{ player.contribution }} ]

</div>
```
* しかし，これだと実はいくら貢献したかがわからない．．．
* もしかしたら使いようがある気もしているが．



## ボタンで入力する方法（バイナリーチョイス）

### Page1.html

```html
{% formfields player.contribution %}
    {% next_button %}
```
* 上記2行を削除する．
  * 入力をボタンで行う＆ボタンを押すと次に進むように設定する．

```html
<p><b>あなたは貢献しますか？</b></p>
<div>
    <button name="contribution" value="0" class="btn btn-primary btn-large">貢献しない</button>
    <button name="contribution" value="20" class="btn btn-primary btn-large">貢献する</button>
</div>
```


## チャットさせてみよう．

* 公共財ゲームを始める前にチャットでのやり取りをしてみましょう．
* Page1の`{% formfield player.contribution %}`の直前に，以下のコードを書いてください．

```html
{% chat %}
```

* 1回実行してみましょう．

* 公共財ゲームのような役割が決まっていないゲームはこれで良いかと思います．
* また，役割があるゲームの場合はこんな感じにしてあげると良さそうです．
  * ex.最終提案ゲーム


`models.py`
```Python
class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'Proposer'
        else:
            return 'Accepter'

    def chat_nickname(self):
        return 'Group {} {}'.format(self.group.id_in_subsession, self.role())
```

`pages.py`
```python
class Page1(Page):
    def vars_for_template(self):
        return dict(
            role=self.player.role(),
            nickname=self.player.chat_nickname()
        )
```
`Page1.html`
```html
{% chat nickname=nickname channel=role %}
```

* ただし問題もある．
  * 役割(role)を日本語にしようとすると2バイト文字はダメ！と怒られる．
  * チャット本文は行けるのになぜ．．．．．


## settingにおけるsession configsの定義：

* oTree で実験を実装するには，`settings.py`の中の`SESSION_CONFIGS`にアプリを登録する必要があります．

```Python
SESSION_CONFIGS = [
    dict(
        name='PG4',
        display_name="はじめての公共財ゲーム",
        num_demo_participants=4, # ここでデモ用に参加する人数は定義しておく必要があります．
        app_sequence=['public_goods_trial']
    ),
]
```


## サーバとして起動
* 自身の端末をサーバとして起動します．
```Python
otree devserver
```
  - これで自身の端末で実験を実施することができます．
  - [http://localhost:8000/](http://localhost:8000/)にアクセスしてみてください．





