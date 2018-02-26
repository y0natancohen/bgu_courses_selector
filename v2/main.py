

def main():
    from logic import get_valid_options, display_week
    from filter import filter_courses, num_of_goods

    valid_options = list(get_valid_options())
    print len(valid_options)
    new_options = filter_courses(valid_options)
    print len(new_options)

    for op in new_options:
        print 'goods: ', num_of_goods(op)
        display_week(op)
        print


if __name__ == '__main__':
    main()