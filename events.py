from datetime import datetime

n_to_d = {
            22: 'sun',
            23: 'mon',
            24: 'tue',
            25: 'wed',
            26: 'thu',
        }

recommended = {'gurion', 'marmelstein', 'tal', 'efrat', 'shechter', 'tiomkin', 'avraham'}
golden = {'shkoop'}
bad = {'smit'}
# bad = {}


def overlaps(ev1, ev2):
    return ev1.day == ev2.day and \
           (ev2.start < ev1.finish < ev2.finish or
            ev1.start < ev2.finish < ev1.finish)


class Event:
    def __init__(self, day, start, fin, name, lecture=True):
        y, m, d = day
        self.day = d
        self.name = ''
        self.start = datetime(y, m, d, start)
        self.finish = datetime(y, m, d, fin)
        self.prof = name
        self.is_lecture = lecture

    def __repr__(self):

        return '{} {}-{}: {}, {} {}{}{}'.format(
            n_to_d[self.day], self.start.hour, self.finish.hour, self.name, self.prof,
            ('(recommended)' if self.recommended() else ''), ('(BAD)' if self.bad() else ''),
            ('(GOLD)' if self.golden() else ''))

    def recommended(self):
        return self.prof in recommended

    def golden(self):
        return self.prof in golden

    def bad(self):
        return self.prof in bad


class Events:
    def __init__(self, _events=None):
        self.events = _events or []
        self.four_courses_a_day = False

    def sorted(self):
        return sorted(self.events, key=lambda x: x.start)

    def to_list(self):
        evs = self.sorted()
        return [[x for x in evs if n_to_d[x.day] == 'sun'],
             [x for x in evs if n_to_d[x.day] == 'mon'],
             [x for x in evs if n_to_d[x.day] == 'tue'],
             [x for x in evs if n_to_d[x.day] == 'wed'],
             [x for x in evs if n_to_d[x.day] == 'thu']]

    def __repr__(self):
        evs = self.sorted()
        l = [[x for x in evs if n_to_d[x.day] == 'sun'],
             [x for x in evs if n_to_d[x.day] == 'mon'],
             [x for x in evs if n_to_d[x.day] == 'tue'],
             [x for x in evs if n_to_d[x.day] == 'wed'],
             [x for x in evs if n_to_d[x.day] == 'thu']]

        # for l1 in l:
        #     print l1
        #     if len(l1) > 3:
        #         print l1
        #         self.four_courses_a_day = True

        l1 = [str(_i) for _i in l if _i]
        return '\n'.join(l1)

    def add(self, _ev):
        if isinstance(_ev, Event):
            self.events.append(_ev)
        elif isinstance(_ev, Events):
            self.events.extend(_ev.events)

    def has_overlaps(self):
        days = self.to_list()
        for day in days:
            if len(day) not in (0, 1):
                for i, ev in enumerate(day[:-1]):
                    ev1, ev2 = day[i], day[i + 1]
                    if ev1.finish > ev2.start:
                        return True
        return False

                # for _i, ev1 in enumerate(self.events):
        #     new_events = [_ for _ in self.events]
        #     new_events.pop(_i)
        #     for ev2 in new_events:
        #         if overlaps(ev1, ev2):
        #             return True
        # return False

    def get_windows(self):
        days = self.to_list()
        for d in days:
            windows = []
            if len(d) not in (1, 0):
                for i, ev in enumerate(d[:-1]):
                    delta = d[i + 1].start - d[i].finish
                    hours = delta.seconds / 3600
                    windows.append(hours)
            if windows:
                for window in windows:
                    if window:
                        yield window

