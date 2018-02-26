# -*- coding: utf-8 -*-
from utils import day_to_str


class Lesson:
    def __init__(self, course, is_lecture, prof, day, start, end):
        if start.hour < 8 or start.hour > 20:
            raise Exception('start at' + str(start.hour))
        if end.hour < 8 or end.hour > 20:
            raise Exception('end at' + str(end.hour))

        self.course = course
        self.is_lecture = is_lecture
        self.prof = prof
        self.day = day
        self.start = start
        self.end = end

    def __repr__(self):
        return u'{} {} {} {} {}-{}'.format(
            self.prof.name, self.course, 'lecture' if self.is_lecture else 'tirgul',
            day_to_str[self.day], self.start.hour, self.end.hour)


class Group:
    def __init__(self, ):
        self.lectures = []
        self.tirguls = []

    @property
    def prof(self):
        return self.lectures[0].prof


class Professor:
    bads = {'smit', 'zur', 'vernik'}
    goods = {'denis', 'ido efrat', 'stein', 'niman',
             'peter', 'revayev', 'sidi', 'shnep',
             'mermel', 'motke', 'segev', 'perl'}

    def __init__(self, name):
        self.name = name
        if self.name == u'\xa0':  # weird I know
            self.name = ' '

        if name in self.bads:
            self.bad = True
        else:
            self.bad = False

        if name in self.goods:
            self.good = True
        else:
            self.good = False

    def __repr__(self):
        return self.name
