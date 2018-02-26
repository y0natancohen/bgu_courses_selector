# -*- coding: utf-8 -*-


def _no_bads(op):
    for lesson in op:
        if lesson.prof.bad:
            return False
    return True


def num_of_goods(op):
    goods = 0
    for lesson in op:
        if lesson.prof.good:
            goods += 1
    return goods


def has(name, op):
    for lesson in op:
        if lesson.prof.name == name:
            return True
    return False


def legal(op):
    for lesson in op:
        if len(lesson.prof.name) <= 2:
            return False
    return True


def filter_courses(options):
    no_bads = [op for op in options if _no_bads(op)]
    no_illegal = [op for op in no_bads if legal(op)]
    only_denis = [op for op in no_illegal if has('denis', op)]
    only_mermel = [op for op in only_denis if has('mermel', op)]

    last = only_mermel
    return list(reversed(sorted(last, key=num_of_goods)))
