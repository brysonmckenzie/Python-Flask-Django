def Scores_and_Grades():
    import random
    
    one = "A"
    two = "B"
    three = "C"
    four = "D"
    five = "F"

    print "Scores and Grades"

    for index in range(1,11):
        
        random_num = random.randrange(60,101)
        
        if random_num < 69:
            print "Score: ",random_num, "Your grade is ",four
        elif random_num < 79:
            print "Score: ",random_num, "Your grade is ",three
        elif random_num < 89:
            print "Score: ",random_num, "Your grade is ",two
        elif random_num <= 100:
            print "Score: ",random_num, "Your grade is ",one 
        else:
            print " F!!!!!"
    print "End of program. Bye!!"

Scores_and_Grades()