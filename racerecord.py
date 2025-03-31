#SUBPROGRAMS
#====================================================================================================
#validates integer inputs (gender, number of athletes)
def validate_integer(detail, lower, higher):
    while True:
        try:
            item = int(input(f"Please enter the {detail} between {lower} and {higher}: "))
            if int(item) >=lower and int(item)<= higher:
                return item
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
#gets record times based on the gender
def get_records(gender):
    if gender == 1:
        world = 9.58
        euro = 9.86
        brit = 9.87
    else:
        world = 10.49
        euro = 10.73
        brit = 10.99
    return world, euro, brit

#validates any float input(scores)
def validate_size(detail, lower, higher):
    while True:
        try:
            item = float(input(f"Please enter the {detail} between {lower} and {higher}: "))
            if item >= lower and item <= higher:
                return item
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
#====================================================================================================
#GLOBAL VARIABLES/MAIN
#====================================================================================================
#global variables
times = []
time = 0
lane = 1
number_of_athletes = 0
gender = 0
#MAIN
print("Male (1), Female (2)")
gender = validate_integer("gender", 1, 2)
records = get_records(gender)
world, euro, brit = records[0], records[1], records[2]
number_of_athletes = validate_integer("number of athletes", 4, 8)
for i in range (0, number_of_athletes):
    time = validate_size("time", 0, 100)
    times.append((lane, time))
    lane += 1
    number_of_athletes -= 1
sorted_times = sorted(times,key=lambda X:X[1])
position = 0
for row in sorted_times:
    print(row)
    if sorted_times[position][1] <= world:
        print("A world record has been broken")
    elif sorted_times[position][1] <= euro:
        print("An european record has been beaten")
    elif sorted_times[position][1] <= brit:
        print("A british record has been broken")
    else:
        print("No record was broken here")
    position += 1
