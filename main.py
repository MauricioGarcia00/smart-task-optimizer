def main_score (task):
    return task["importance"] / (task["difficulty"] * task["hours"])

def days_left_weight (days_left):
    if days_left <= 2:
        return  .3
    elif days_left <= 7:
        return 0.2
    elif days_left <= 14:
        return 0.1
    else:
        return 0




def final_score(task):
    base = main_score(task)
    weight = days_left_weight(task["days_left"])
    return base + (weight * base)


def main ():
    print("Smart Task Optimizer Initializing\n")


    print("The following tasks are\n")



    task = [
        {"name": "homework",  "importance": 8, "difficulty": 6,  "hours": 4, "days_left": 4},
        {"name": "gym",       "importance":5 , "difficulty": 1,  "hours": 2, "days_left": 1},
        {"name": "drawing",   "importance":2 , "difficulty": 2,  "hours": 1, "days_left": 99},

    ]

    for n in task:
        print (n)



    print("\n \nIf we order the task they will be")


    for t in task:
        score = final_score(t)
        print(t["name"], "->", score)


if (__name__ == "__main__"):
    main()