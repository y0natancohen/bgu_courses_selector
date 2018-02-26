# -*- coding: utf-8 -*-
from classes import Lesson, Group, Professor
from bs4 import BeautifulSoup as BS
from datetime import datetime
from utils import heb_days


def _get_start_end(day, start_end_str):
    return datetime(day.year, day.month, day.day, int(start_end_str[:2])), \
           datetime(day.year, day.month, day.day, int(start_end_str[8:10]))


def load_tirgul(course, is_lecture, row):
    cells = row.find_all('td')
    prof = Professor(cells[2].text)
    data = cells[3].text
    day = heb_days[data[:5]]
    start, end = _get_start_end(day, data[6:19])
    return Lesson(course, is_lecture, prof, day, start, end)


def load_lectures(course, is_lecture, row):
    cells = row.find_all('td')
    prof = Professor(cells[2].text)
    data = cells[3].text
    day1 = heb_days[data[:5]]
    day2 = heb_days[data[19:24]]
    start1, end1 = _get_start_end(day1, data[6:19])
    start2, end2 = _get_start_end(day2, data[6:19])
    return [Lesson(course, is_lecture, prof, day1, start1, end1),
            Lesson(course, is_lecture, prof, day2, start2, end2)]


def get_groups1(course, html, profs_row_num):
    soup = BS(html, 'html.parser')
    rows = soup.find_all('tr')
    for row_num, num_of_tirguls in profs_row_num:
        group = Group()
        group.lectures = load_lectures(course, is_lecture=True, row=rows[row_num])
        for row in rows[row_num:row_num + num_of_tirguls]:
            group.tirguls.append(load_tirgul(course, is_lecture=False, row=row))
        yield group
