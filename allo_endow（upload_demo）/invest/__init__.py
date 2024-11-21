from otree.api import *
import random

doc = """
Time Allocation_Round 1
"""


class C(BaseConstants):
    NAME_IN_URL = 'invest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOW = list(range(1, 25))  # 禀赋为24,为传递给前端，使用列表
    INDEX = list(range(1, 23))  # 任务序号从1~22
    POINTS = 248  # 任务完成点数需要248点
    SCORE1 = 120  # 完成的积分为120
    SCORE2 = 108  # 未完成是108点积分
    LIMITED_NUM = 5  # 最大人数为5
    ratio = 0.3
    endow_ratio = 1.1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    first_score = models.FloatField(default=0.00)
    endow_trans = models.FloatField(default=0.00)
    first_income = models.FloatField(default=0.00)
    second_score2_r = models.FloatField(default=0.00)
    second_score2_left = models.FloatField(default=0.00)


class Livedata(ExtraModel):
    player = models.Link(Player)
    group = models.Link(Group)
    remain_time = models.IntegerField(initial='')
    task_choice = models.IntegerField(initial='')
    investment = models.IntegerField(initial='')
    trans = models.IntegerField(initial='')
    left_endowment = models.IntegerField(initial='')


# 玩家个人层面需要记录的数据：投资的时刻、选择的任务、投入的时间、剩余的禀赋、时间转化的点数


# PAGES
class MyPage(Page):
    timeout_seconds = 840

    @staticmethod
    def vars_for_template(player: Player):
        task_id = C.INDEX
        playerself = player.id_in_group
        endow = C.ENDOW
        return dict(task_id=task_id, playerself=playerself, endow=endow)

    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group
        group = player.group
        group_id = group.id_in_subsession

        countdown = int(data['countdown'])
        investment = int(data['investment'])
        task_choice = int(data['task_choice'])
        left_endowment = int(data['endowment']) - investment

        # 筛选该投资任务已有的人
        task_choice_data = Livedata.filter(group=group, group_id=group_id, task_choice=task_choice)
        task_choice_id_list = list(set(item.player_id for item in task_choice_data))
        member = len(task_choice_id_list)

        if member < C.LIMITED_NUM or my_id in task_choice_id_list:
            # 更新参与者的数据，剩余禀赋计算以及数据保存
            Livedata.create(player=player, group_id=group_id, remain_time=countdown,
                            investment=investment, task_choice=task_choice,
                            trans=investment * random.randint(7, 9),
                            left_endowment=left_endowment)

            # 投资记录完成后再次筛选该投资任务的成员
            task_choice_data_second = Livedata.filter(group=group, group_id=group_id, task_choice=task_choice)
            task_choice_id_list_second = list(set(item.player_id for item in task_choice_data_second))
            member_second = len(task_choice_id_list_second)

            # 筛选被试在此任务的所有投资并求和
            investment_data = Livedata.filter(player=player, task_choice=task_choice)
            investmented = sum([item.investment for item in investment_data]) if investment_data else 0

            # 筛选被试投资的任务的内容并返回需要返回给全体人员的数据
            total_trans = sum(list(item.trans for item in task_choice_data_second))
            if total_trans >= C.POINTS:
                return {
                    0: dict(my_id=my_id, membercheck=member_second, left_endowment=left_endowment,
                            task_choice=task_choice, total_trans=total_trans,
                            investmented=investmented, achieve=True)}
            else:
                return {
                    0: dict(my_id=my_id, membercheck=member_second, left_endowment=left_endowment,
                            task_choice=task_choice, total_trans=total_trans,
                            investmented=investmented)}
        else:
            return {my_id: dict(errormsg=True)}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        group_id = group.id_in_subsession
        player_score_dict = dict()
        for i in C.INDEX:
            task_data = Livedata.filter(group=group, group_id=group_id, task_choice=i)  # 筛选每个任务的结果
            player_data = Livedata.filter(player=player, task_choice=i)  # 筛选玩家的结果
            sum_trans = sum(list(item.trans for item in task_data))  # 求每个任务的所有玩家总投入
            player_trans = sum(list(item.trans for item in player_data))  # 玩家在这个任务的总投入
            if not task_data or not player_data:
                continue
            if sum_trans >= C.POINTS:
                player_score = C.SCORE1 * (player_trans / sum_trans)
            else:
                player_score = C.SCORE2 * (sum_trans / C.POINTS) * (player_trans / sum_trans)
            player_score_dict[i] = player_score
        player_alldata = Livedata.filter(player=player)
        # 如果返回的是空，那么说明被试没有进行任何投入，则该被试剩余禀赋为24
        min_endow = min(list(item.left_endowment for item in player_alldata)) if player_alldata else 24
        first_score = round(sum(player_score_dict.values()), 2)
        score_trans = round((first_score * C.ratio), 1)
        endow_trans = round((min_endow * C.endow_ratio), 1)
        first_income = round((score_trans + endow_trans), 1)
        if player_score_dict:
            r_task_score = round(random.choice(list(player_score_dict.values())), 2)
        else:
            r_task_score = 0
        if len(player_score_dict) == 1:
            left_task_score = 0
        else:
            left_task_score = round(((first_score - r_task_score) / (len(player_score_dict) - 1)), 2)
        player.first_score = first_score
        player.endow_trans = endow_trans
        player.first_income = first_income
        player.second_score2_r = r_task_score
        player.second_score2_left = left_task_score
        return dict(first_score=first_score, score_trans=score_trans, first_income=first_income,
                    endow_trans=endow_trans)


class WaitFirstPage(WaitPage):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results, WaitFirstPage]


def custom_export(players):
    """For data export page"""
    yield ['player_id', 'group_id', 'remain_time', 'task_choice', 'investment', 'trans', 'left_endowment']

    totaldata = Livedata.filter()
    for each in totaldata:
        yield [each.player_id, each.group_id, each.remain_time, each.task_choice, each.investment, each.trans,
               each.left_endowment]
