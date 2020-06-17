from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='questionnaire',
        display_name="はじめての質問紙",
        num_demo_participants=1, # ここでデモ用に参加する人数は定義しておく必要があります．
        app_sequence=['questionnaire']
    ),

    dict(
        name='UG',
        display_name="はじめての最終提案ゲーム",
        num_demo_participants=2,
        app_sequence=['ultimatum_trial']
    ),
    dict(
        name='DG',
        display_name="はじめての独裁者ゲーム",
        num_demo_participants=2,
        app_sequence=['dictator_trial']
    ),
    dict(
        name='UGDG',
        display_name="はじめての最終提案ゲームとはじめての独裁者ゲーム",
        num_demo_participants=2,
        app_sequence=['ultimatum_trial', 'dictator_trial', 'questionnaire']
    ),
    dict(
        name='public_goods_trial',
        display_name="はじめての公共財ゲーム",
        num_demo_participants=4, 
        app_sequence=['public_goods_trial']
    ),

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'qynhs&e)!bz9#-gz4&)pzybv2hdcu9yx7879_u+pn_l$(#3hr+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
