# プログラム⑥：もともと用意されているプログラムを使おう．

## わかりやすいように新しいプロジェクトを立ち上げます．

* 今回はわかりやすいようにデスクトップでの作業を例とします．

* Windowsの場合
```
cd C:¥Users¥[ユーザ名]¥Desktop
```

* Macの場合
```
cd /Users/[ユーザ名]/Desktop
```

* 上記にてデスクトップに移動した後に，"otreetest2"という名前のプロジェクトフォルダを作成します．
```
otree startproject otreetest2
```
  - ここで様々な作業を行う感じです．

```
Include sample games? (y or n)→ y
```
* これにより，もともと用意されているプログラムをインストールすることができます．


## 登録されていないプログラムを使えるようにします．

### `SESSION_CONFIGS`に登録しよう

* `SESSION_CONFIGS`の中に登録されていないアプリは使うことができません．
* 下の方にある`inactive session configs`の中に書かれているもの`SESSION_CONFIGS`に登録すると使えるようになります．
  * 今回は`#`を取るのがめんどくさいかと思い，下に既にとったものを用意しました．
  * `SESSION_CONFIGS`をまるまる置き換えてください．

```Python
SESSION_CONFIGS = [
    dict(
        name='public_goods',
        display_name="Public Goods",
        num_demo_participants=3,
        app_sequence=['public_goods', 'payment_info'],
    ),
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        num_demo_participants=3,
        app_sequence=['guess_two_thirds', 'payment_info'],
    ),
    dict(
        name='survey',
        display_name='survey',
        num_demo_participants=1,
        app_sequence=['survey', 'payment_info'],
    ),
    dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
    dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
        app_sequence=['prisoner', 'payment_info']),
    dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
        app_sequence=['volunteer_dilemma', 'payment_info']),
    dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
        'cournot', 'payment_info'
    ]),
    dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
        app_sequence=['dictator', 'payment_info']),
    dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
        'matching_pennies',
    ]),
    dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
        app_sequence=['traveler_dilemma', 'payment_info']),
    dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
        app_sequence=['bargaining', 'payment_info']),
    dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
        app_sequence=['common_value_auction', 'payment_info']),
    dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
        'bertrand', 'payment_info'
    ]),
    dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
        num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
    dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
        app_sequence=['trust_simple']),
]

```

### もともと用意されているもの
* 公共財ゲーム
* 美人投票ゲーム（平均の2/3の推測）
* 調査
* 信頼ゲーム
* 囚人のジレンマ
* ボランティアのジレンマ
* クールノー競争
* 独裁者ゲーム
* マッチングペニー
* 旅人のジレンマ
* 交渉ゲーム
* 共通価値オークション
* ベルトラン競争
* 公共財ゲーム（チュートリアル向けのシンプル版）
* 信頼ゲーム（チュートリアル向けのシンプル版）


