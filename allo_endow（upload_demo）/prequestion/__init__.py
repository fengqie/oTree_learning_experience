from otree.api import *

doc = """
Pre-experimental questionnaire
"""


class C(BaseConstants):
    NAME_IN_URL = 'prequestion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    serial_number = models.IntegerField(label='1.Please enter your student number [for revenue verification only]')
    can_contribute = models.BooleanField(
        label='2.If a project has been completed but the maximum number of participants has not been reached,'
              ' can you make an input? [Answer: Yes]',
        choices=[(True, 'Y'), (False, 'N')],
        widget=widgets.RadioSelect
    )
    limited_num = models.IntegerField(
        label='3.What is the maximum number of participants per project in this experiment? [Answer: 5]',
        choices=[2, 3, 5, 6],
        widget=widgets.RadioSelect
    )
    endow = models.IntegerField(
        label='4.What is the allocable endowment per person per round in this experiment? [Answer: 24]',
        choices=[10, 21, 24, 30],
        widget=widgets.RadioSelect
    )
    cd = models.IntegerField(
        label='5.How many seconds is the countdown for each round of this experiment? [Answer: 840]',
        choices=[100, 250, 840, 300],
        widget=widgets.RadioSelect
    )
    hypo_score1 = models.IntegerField(
        label='6.Assuming that the converted points from your inputs in a project end up being 50% of '
              'the inputs from all participants, and that the project has been completed,'
              ' how many points can you earn in this project? [Answer: 60]',
        choices=[60, 10, 40, 90],
        widget=widgets.RadioSelect
    )
    hypo_score2 = models.IntegerField(
        label='7.Assuming that the converted points from your inputs in a project end up being 50% of'
              ' the inputs from all participants, and that the project ends up with a 50% completion schedule,'
              ' how many points can you earn in this project? [Answer: 27]',
        choices=[10, 108, 27, 54],
        widget=widgets.RadioSelect
    )


# PAGES
class StartPage(Page):
    pass


class MyPage(Page):
    form_model = 'player'
    form_fields = ['serial_number', 'can_contribute', 'limited_num', 'endow', 'cd', 'hypo_score1', 'hypo_score2']


class ResultsWaitPage(WaitPage):
    pass


page_sequence = [StartPage, MyPage, ResultsWaitPage]
