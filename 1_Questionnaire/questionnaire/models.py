from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django import forms


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None # 1人の時は"None"と記述します．
    num_rounds = 1 # 1回だけ質問します．


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.CharField(initial=None,
                                choices=['男性', '女性', '回答しない'],
                                verbose_name='あなたの性別を教えてください．',
                                widget=widgets.RadioSelect())
    q_age = models.PositiveIntegerField(verbose_name='あなたの年齢を教えてください．',
                                        choices=range(0, 125),
                                        initial=None)
    q_country = models.CharField(initial=None,
                                choices=['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県','茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県','新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県','滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県','鳥取県', '島根県', '岡山県', '広島県', '山口県','徳島県', '香川県', '愛媛県', '高知県','福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県'],
                                verbose_name='あなたのおすまいの地域を教えてください．',
                                widget=forms.Select())

    q_tanmatsu = models.CharField(initial=None,
                                choices=['パソコン',
                                        'タブレット',
                                        'スマートフォン',
                                        'それ以外'
                                        ],
                                verbose_name='この回答は、どの電子機器で回答していますか？',
                                widget=forms.Select())