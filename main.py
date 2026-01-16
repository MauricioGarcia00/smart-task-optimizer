#It is importance to have a clear meaning for the following variables / words.

#Difficulty: Objectively speaking, HOW DIFFICULT is it, it doesn't mean the mental strain to get you to do something
# it means HOW COMPLEX is something, how many "trials and error"

# Importance:   How vital is this? How bad do I consider the consequences to be if I fail to do the task.
# Hours:        A main general idea on how long it will take
# Days Left:    Is the Deadline, this works as a passive multiplier that everyone has

def main_score (task): #Calculations to get the main score.
    base = task["importance"] * task["difficulty"] /  task["hours"]
    weight = days_left_weight(task["days_left"])
    return base + (weight * base)
    #return base * weight


def days_left_weight (days_left): # Passive Multiplier
    if days_left <= 2:
        return  1.3
    elif days_left <= 7:
        return 1.2
    elif days_left <= 14:
        return 1.1
    else:
        return 1        # By increasing THIS number we will increase the priority to tasks without time limits , Current Dev notes, rn at "1" works intended, but needs further testing to see if it should be 0, 0.5 or 1




#def final_score(task):
 #   base = main_score(task)
  #  weight = days_left_weight(task["days_left"])
   # return base + (weight * base)


def main ():
    print("Smart Task Optimizer Initializing\n")


    print("The following tasks are\n")



    task = [
        {"name": "homework",  "importance": 8, "difficulty": 6,  "hours": 4, "days_left": 4},
        {"name": "gym",       "importance":5 , "difficulty": 1,  "hours": 2, "days_left": 1},
        {"name": "drawing",   "importance":2 , "difficulty": 2,  "hours": 1, "days_left": 99},
        {"name": "gaming",        "importance": 3, "difficulty": 1, "hours": 2,  "days_left": 1},
        {"name": "call family",   "importance": 6, "difficulty": 1, "hours": 1,  "days_left": 7},
        {"name": "side project",  "importance": 7, "difficulty": 6, "hours": 4,  "days_left": 21},
        {"name": "grocery run",   "importance": 6, "difficulty": 1, "hours": 1,  "days_left": 2},

    ]

    for n in task:
        print (n)



    print("\n \nIf we order the task they will be")


    for t in task:
        score = main_score(t)
        print(t["name"], "->", score)


if (__name__ == "__main__"):
    main()