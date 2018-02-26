from courses import alg_sets, log_sets, hed_sets
from events import Events, golden

MAX_LEN_OF_WEEK = 4
MIN_NUM_OF_RECOMMENDED = 4
MIN_LEN_OF_DAY = 2
MAX_WINDOW_LEN = 2  # lowering this is problematic
NUM_OF_GOLDEN = len(golden)


def get_all_options():
    all_options = []
    for alg_set in alg_sets:
        alg_set[0].name = alg_set[1].name = 'algebra lecture'
        alg_set[2].name = 'algebra tirgul'

        for log_set in log_sets:
            log_set[0].name = log_set[1].name = 'logika lecture'
            log_set[2].name = 'logika tirgul'

            for hed_set in hed_sets:
                hed_set[0].name = hed_set[1].name = 'hedva lecture'
                hed_set[2].name = 'hedva tirgul'
                events = Events(alg_set + log_set + hed_set)

                if not events.has_overlaps():
                    all_options.append(events)

    return all_options


def get_not_bad(_options):
    _not_bad = []
    for op in _options:
        for ev in op.events:
            if ev.bad():
                break
        else:
            _not_bad.append(op)
    return _not_bad


def get_golden(_options):
    # print 'in recomended'
    # print len(_options)
    _golden = []
    for op in _options:
        num_of_golden = 0
        for ev in op.events:
            if ev.golden():
                num_of_golden += 1

        if num_of_golden >= NUM_OF_GOLDEN:
            _golden.append(op)

    return _golden

def get_recommended(_options):
    # print 'in recomended'
    # print len(_options)
    _recommended = []
    for op in _options:
        num_of_recommended = 0
        for ev in op.events:
            if ev.recommended():
                num_of_recommended += 1

        if num_of_recommended >= MIN_NUM_OF_RECOMMENDED:
            _recommended.append(op)

    return _recommended


def get_short_week(_options):
    allowed = []
    for op in _options:
        days = [ev.day for ev in op.events]
        if len(set(days)) < MAX_LEN_OF_WEEK + 1:
            allowed.append(op)
    return allowed


def get_long_days(_options):
    _long_days = []
    for op in _options:
        op_list = op.to_list()
        shortest = 10
        for day in op_list:
            if day and len(day) < shortest:
                shortest = len(day)

        if shortest == MIN_LEN_OF_DAY:
            _long_days.append(op)
    return _long_days


def get_short_windows(_options):
    _short_windows = []
    for op in _options:
        max_windows = max(list(op.get_windows()) or [0])
        if max_windows <= MAX_WINDOW_LEN:
            _short_windows.append(op)
    return _short_windows


def print1(alist):
    for i, op in enumerate(alist):
        print i + 1
        print op
        print


options = get_all_options()
print 'all options', len(options)

# short_windows_ex = get_short_windows(options)
# print 'windows', len(short_windows_ex)
# # print short_windows_ex[0]
#
# not_bad_ex = get_not_bad(short_windows_ex)
# print 'notbad', len(not_bad_ex)
#
# recommended_ex = get_recommended(not_bad_ex)
# print 'rec', len(recommended_ex)
# print recommended_ex[0]
#
# print'--------------------'

not_bad = get_not_bad(options)
print 'without bad', len(not_bad)

# golden = get_golden(recommended)
golden = get_golden(not_bad)
print 'only golden', len(golden)

recommended = get_recommended(golden)
print 'recommended', len(recommended)

short_windows = get_short_windows(recommended)
print 'no big windows', len(short_windows)

short_week = get_short_week(short_windows)
print 'short week', len(short_week)

long_days = get_long_days(short_week)
print 'no long days', len(long_days)

if long_days:
    print1(long_days)

# four courses a day is not working
# print len(day3)
# for i, op in enumerate(day3):
#     if not op.four_courses_a_day:
#         print i
#         print op
#         print
