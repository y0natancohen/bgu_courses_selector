from events import Event

sun = (2017, 10, 22)
mon = (2017, 10, 23)
tue = (2017, 10, 24)
wed = (2017, 10, 25)
thu = (2017, 10, 26)

alg_sets = [
    [
        Event(sun, 10, 12, 'efrat'),
        Event(tue, 10, 12, 'efrat'),
        Event(sun, 14, 16, 'livne'),
    ], [
        Event(sun, 10, 12, 'efrat'),
        Event(tue, 10, 12, 'efrat'),
        Event(sun, 16, 18, 'livne'),
    ], [
        Event(sun, 10, 12, 'efrat'),
        Event(tue, 10, 12, 'efrat'),
        Event(tue, 16, 18, 'tal'),
    ], [
        Event(sun, 10, 12, 'efrat'),
        Event(tue, 10, 12, 'efrat'),
        Event(mon, 12, 14, 'porat'),
    ],

    [
        Event(thu, 10, 12, 'levin'),
        Event(tue, 10, 12, 'levin'),
        Event(tue, 12, 14, 'porat'),
    ], [
        Event(thu, 10, 12, 'levin'),
        Event(tue, 10, 12, 'levin'),
        Event(tue, 14, 16, 'porat'),
    ], [
        Event(thu, 10, 12, 'levin'),
        Event(tue, 10, 12, 'levin'),
        Event(tue, 8, 10, 'tal'),
    ],

    [
        Event(mon, 12, 14, 'mashvitski'),
        Event(wed, 10, 12, 'mashvitski'),
        Event(tue, 12, 14, 'tal'),
    ], [
        Event(mon, 12, 14, 'mashvitski'),
        Event(wed, 10, 12, 'mashvitski'),
        Event(sun, 14, 16, 'tal'),
    ], [
        Event(mon, 12, 14, 'mashvitski'),
        Event(wed, 10, 12, 'mashvitski'),
        Event(sun, 10, 12, 'tal'),
    ], [
        Event(mon, 12, 14, 'mashvitski'),
        Event(wed, 10, 12, 'mashvitski'),
        Event(tue, 10, 12, 'tal'),
    ],
]

log_sets = [

    # add here meizel?
    [
        Event(mon, 14, 16, 'meizel'),
        Event(wed, 15, 17, 'meizel'),
        Event(sun, 14, 16, 'vernik'),
    ], [
        Event(mon, 14, 16, 'meizel'),
        Event(wed, 15, 17, 'meizel'),
        Event(mon, 16, 18, 'shimrat'),
    ], [
        Event(mon, 14, 16, 'meizel'),
        Event(wed, 15, 17, 'meizel'),
        Event(mon, 16, 18, 'marmelstein'),
    ],

    [
        Event(wed, 8, 10, 'avraham'),
        Event(thu, 14, 16, 'avraham'),
        Event(sun, 16, 18, 'marmelstein'),
    ], [
        Event(wed, 8, 10, 'avraham'),
        Event(thu, 14, 16, 'avraham'),
        Event(mon, 8, 10, 'vernik'),
    ],

    [
        Event(tue, 8, 10, 'shkoop'),
        Event(wed, 8, 10, 'shkoop'),
        Event(tue, 16, 18, 'shimrat'),
    ], [
        Event(tue, 8, 10, 'shkoop'),
        Event(wed, 8, 10, 'shkoop'),
        Event(tue, 14, 16, 'shimrat'),
    ], [
        Event(tue, 8, 10, 'shkoop'),
        Event(wed, 8, 10, 'shkoop'),
        Event(mon, 10, 12, 'shimrat'),
    ],

    [
        Event(mon, 12, 14, 'kamenski'),
        Event(thu, 14, 16, 'kamenski'),
        Event(mon, 8, 10, 'gurion'),
    ], [
        Event(mon, 12, 14, 'kamenski'),
        Event(thu, 14, 16, 'kamenski'),
        Event(wed, 16, 18, 'gurion'),
    ], [
        Event(mon, 12, 14, 'kamenski'),
        Event(thu, 14, 16, 'kamenski'),
        Event(sun, 16, 18, 'gurion'),
    ],

    [
        Event(tue, 14, 16, 'smit'),
        Event(thu, 10, 12, 'smit'),
        Event(wed, 16, 18, 'marmelstein'),
    ], [
        Event(tue, 14, 16, 'smit'),
        Event(thu, 10, 12, 'smit'),
        Event(sun, 12, 14, 'marmelstein'),
    ], [
        Event(tue, 14, 16, 'smit'),
        Event(thu, 10, 12, 'smit'),
        Event(sun, 16, 18, 'vernik'),
    ]
]

hed_sets = [
    [
        Event(mon, 9, 12, 'goren'),
        Event(wed, 10, 12, 'goren'),
        Event(thu, 10, 12, 'shechter'),
    ], [
        Event(mon, 9, 12, 'goren'),
        Event(wed, 10, 12, 'goren'),
        Event(tue, 14, 16, 'nicolaivski'),
    ],

    [
        Event(mon, 12, 14, 'tiomkin'),
        Event(wed, 12, 15, 'tiomkin'),
        Event(sun, 10, 12, 'kalish'),
    ], [
        Event(mon, 12, 14, 'tiomkin'),
        Event(wed, 12, 15, 'tiomkin'),
        Event(tue, 14, 16, 'sharabi'),
    ], [
        Event(mon, 12, 14, 'tiomkin'),
        Event(wed, 12, 15, 'tiomkin'),
        Event(tue, 16, 18, 'sharabi'),
    ],

    [
        Event(mon, 14, 16, 'goren'),
        Event(wed, 14, 17, 'goren'),
        Event(sun, 14, 16, 'kalish'),
    ], [
        Event(mon, 14, 16, 'goren'),
        Event(wed, 14, 17, 'goren'),
        Event(thu, 12, 14, 'sharabi'),
    ],

    [
        Event(mon, 14, 16, 'ohlob'),
        Event(wed, 14, 17, 'ohlob'),
        Event(tue, 8, 10, 'nicolaivski'),
    ], [
        Event(mon, 14, 16, 'ohlob'),
        Event(wed, 14, 17, 'ohlob'),
        Event(wed, 10, 12, 'shechter'),
    ],

    [
        Event(mon, 8, 11, 'tiomkin'),
        Event(wed, 8, 10, 'tiomkin'),
        Event(tue, 12, 14, 'nicolaivski'),
    ], [
        Event(mon, 8, 11, 'tiomkin'),
        Event(wed, 8, 10, 'tiomkin'),
        Event(wed, 12, 14, 'nicolaivski'),
    ],

]