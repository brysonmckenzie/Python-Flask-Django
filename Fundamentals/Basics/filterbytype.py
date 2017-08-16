def chance(value):


    if type(value)is int:
        if value >= 100:
            print "that is a big number"
        elif value < 100:
            print "that is a small number"

    elif type(value)is str:

        if len(value) >= 50:
            print "that is a big sentence"
        elif len(value) < 50:
            print "that is a small sentence"
    elif type(value) is list:

        if len(value) >= 10:
            print "that is a big list"
        elif len(value) < 10:
            print "that is a small list"

    return value

chance ([1,2,3,4,5,6,7,8,9,10])







