from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = 'player'
    form_fields = [
    'q_gender',
    'q_age',
    'q_country',
    'q_tanmatsu'
    ]




page_sequence = [Page1]
