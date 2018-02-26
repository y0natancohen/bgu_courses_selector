# -*- coding: utf-8 -*-
from htmls import combi, hed, alg, mivne
from html_parser import get_groups1
from utils import sun, mon, tue, wed, thu, day_to_str


def has_overrides(_lessons):
    lessons = sorted(_lessons, key=lambda x: x.start)
    for i, lesson in enumerate(lessons):
        next_lesson_i = i + 1
        if next_lesson_i == len(lessons):
            break
        next_lesson = lessons[next_lesson_i]
        if lesson.end > next_lesson.start:
            return True
    return False


comb_groups = list(get_groups1('combi', combi, ((1, 3), (6, 3), (11, 3), (16, 3))))
hed_groups = list(get_groups1('hed', hed, ((1, 3), (6, 3), (11, 3), (16, 3))))
alg_groups = list(get_groups1('alg', alg, ((1, 3), (6, 3), (12, 3))))
mivne_groups = list(get_groups1('mivne', mivne, ((1, 3), (6, 3), (11, 3), (16, 3), (21, 3))))


def get_valid_options():
    for comb_group in comb_groups:
        for comb_tirgul in comb_group.tirguls:
            for hed_group in hed_groups:
                for hed_tirgul in hed_group.tirguls:
                    for alg_group in alg_groups:
                        for alg_tirgul in alg_group.tirguls:
                            for mivne_group in mivne_groups:
                                for mivne_tirgul in mivne_group.tirguls:
                                    all = [comb_group.lectures[0], comb_group.lectures[1],
                                           hed_group.lectures[0], hed_group.lectures[1],
                                           alg_group.lectures[0], alg_group.lectures[1],
                                           mivne_group.lectures[0], mivne_group.lectures[1],
                                           comb_tirgul, hed_tirgul, alg_tirgul, mivne_tirgul]
                                    if not has_overrides(all):
                                        yield all


def display_week(week):
    week = sorted(week, key=lambda x: x.start)
    for day in (sun, mon, tue, wed, thu):
        print '{}:'.format(day_to_str[day])
        for lesson in week:
            if lesson.day == day:
                print lesson
