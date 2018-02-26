# -*- coding: utf-8 -*-
from datetime import datetime


sun = datetime(2018, 2, 18)
mon = datetime(2018, 2, 19)
tue = datetime(2018, 2, 20)
wed = datetime(2018, 2, 21)
thu = datetime(2018, 2, 22)


heb_days = {
    u'\u05d9\u05d5\u05dd \u05d0': sun,
    u'\u05d9\u05d5\u05dd \u05d1': mon,
    u'\u05d9\u05d5\u05dd \u05d2': tue,
    u'\u05d9\u05d5\u05dd \u05d3': wed,
    u'\u05d9\u05d5\u05dd \u05d4': thu
}


day_to_str = {
    sun: 'sun',
    mon: 'mon',
    tue: 'tue',
    wed: 'wed',
    thu: 'thu',
}