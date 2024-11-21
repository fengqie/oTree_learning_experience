from otree.api import *

doc = """
Post-experimental questionnaire
"""


class C(BaseConstants):
    NAME_IN_URL = 'postquestion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    risk = models.IntegerField(
        label='1.To what extent do you consider yourself willing to take risks in most cases?',
        choices=[
            (1, 'Very reluctant to take risks'),
            (2, 'Reluctance to take risks'),
            (3, 'A little reluctance to take risks'),
            (4, 'Neutral'),
            (5, 'A little willingness to take risks'),
            (6, 'Willingness to take risks'),
            (7, 'Very willing to take risks'),
        ],
        widget=widgets.RadioSelect
    )

    gender = models.IntegerField(
        label='2.Please select your gender',
        choices=[
            (1, 'Male'),
            (2, 'Female')
        ],
        widget=widgets.RadioSelectHorizontal
    )

    age = models.IntegerField(
        label='3.Please select your age range',
        choices=[
            (17, 'under 18'), (18, '18'), (19, '19'), (20, '20'), (21, '21'),
            (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, 'over 25'),

        ],
        widget=widgets.RadioSelectHorizontal
    )

    grade = models.IntegerField(
        label='4.Please select your grade level',
        choices=[(1, 'first-year university student'), (2, 'second-year university student'),
                 (3, 'third-year university student'), (4, 'senior student'), (5, 'Postgraduate and above')],
        widget=widgets.RadioSelectHorizontal
    )

    major = models.IntegerField(
        label='5.Please select the discipline to which your major belongs (options are in no particular order, a rough match is sufficient)',
        choices=[
            (1, 'philosophy'),
            (2, 'economics'),
            (3, 'law'),
            (4, 'pedagogical'),
            (5, 'literary'),
            (6, 'history'),
            (7, 'science'),
            (8, 'engineering'),
            (9, 'agronomy'),
            (10, 'medicine'),
            (11, 'military science'),
            (12, 'management studies'),
            (13, 'art'),
        ],
        widget=widgets.RadioSelectHorizontal
    )

    whether_tm = models.IntegerField(
        label='6.Are you planning to, currently participating in, or have you already participated in the recommendation exemption program?',
        choices=[(1, 'Y'), (2, 'N')],
        widget=widgets.RadioSelectHorizontal
    )

    participated_coop_project = models.IntegerField(
        label='7.Have you ever been involved in a group co-operation project',
        choices=[(1, 'Y'), (2, 'N')],
        widget=widgets.RadioSelectHorizontal
    )

    coop_project_count = models.IntegerField(
        label='8.What is the approximate number of group co-operation projects you have been involved in? (in the last year)',
        choices=[
            (0, '0'),
            (3, '1~5'),
            (8, '6~10'),
            (13, '11~15'),
            (15, 'over 15'),
        ],
        widget=widgets.RadioSelectHorizontal
    )

    coop_project_reason1 = models.IntegerField(
        label='9.Does the reason involve any of the following subjective reasons: Interest & Social Expansion & Skill Acquisition',
        choices=[(1, 'Y'), (2, 'N')],
        widget=widgets.RadioSelectHorizontal
    )

    coop_project_reason2 = models.IntegerField(
        label='10.Whether the reason relates to incentives within the project itself: e.g.the project itself brings incentives such as prizes and honours.',
        choices=[(1, 'Y'), (2, 'N')],
        widget=widgets.RadioSelectHorizontal
    )

    coop_project_reason3 = models.IntegerField(
        label='11.Whether the reason involves incentivising reasons other than the project: e.g.the project can be used as a selection criterion for exemption status',
        choices=[(1, 'Y'), (2, 'N')],
        widget=widgets.RadioSelectHorizontal
    )

    other_reason = models.LongStringField(
        label='12.Other active or passive reasons (please add if you can think of any)',
        blank=True
    )

    consumption_ability = models.IntegerField(
        label='13.Approximately what is your average monthly spending?',
        choices=[
            (500, 'under 500CNY'),
            (1000, '500~1000CNY'),
            (1500, '1000~1500CNY'),
            (2000, '1500~2000CNY'),
            (2500, 'over 2000CNY'),
        ],
        widget=widgets.RadioSelectHorizontal
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'risk',
        'gender',
        'age',
        'grade',
        'major',
        'whether_tm',
        'participated_coop_project',
        'coop_project_count',
        'coop_project_reason1',
        'coop_project_reason2',
        'coop_project_reason3',
        'other_reason',
        'consumption_ability',
    ]


class Results(Page):
    pass


page_sequence = [MyPage, Results]
