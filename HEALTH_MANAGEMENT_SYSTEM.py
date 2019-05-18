def GetDate():
    import datetime
    return datetime.datetime.now()


def GetName():

    """This function will give the name to the file which you will enter!!"""

    name = input("Enter the Name of Person:")
    f = open(name, "x")
    print("The New file has been created successfully with Name of", name)
    f.close()


def doExercise(name):

    """It will Add the Exercise in file!!"""

    Exc = input("Enter the Name of Exercise:")
    f = open(name, "a")
    f.write(Exc)
    f.close()


def addfood(name):

    """It will add the food or diet chart!!!"""

    food = input("Enter the food name:")
    f = open(name, "a")
    f.write(food)
    f.close()

def add_date(name):

    """It will add the date and time for exercise and food!!"""
    f = open(name, "a")
    ad = str(GetDate())
    f.write(ad)
    f.close()

def display(name):
    """It will show the all details of the person!!!"""

    file = open(name, "r")
    for i in file:
        print(i, end=" ")
    file.close()


n = 1
while n >= 1:
    print("Press 1 => Add New Member", "Press 2 => Add Food and Exercise in existing File", end="\n")
    num = int(input("Enter the value:"))
    if num == 1:
        print("Name of the New file:")
        filename = input()
        add_date(filename)
        print("Add Food to eat:")
        addfood(filename)
        print("Food added successfully!!")
        print()
        print("Add the Exercise:")
        doExercise(filename)
        print("Exercise added Successfully!!")
        print()
        print("Press 1 if you want to display")
        num1 = int(input())
        if num1 == 1:
            print(display(filename))
    elif num == 2:
        print("Enter the name of file:")
        name_of_file = input()
        print("Press 1 for add food & Exercise ", "Press 2 for Display", end="\n")
        number = int(input("Enter your choice:"))
        if number == 1:
            add_date(name_of_file)
            addfood(name_of_file)
            doExercise(name_of_file)
        elif number == 2:
            print(display(name_of_file))
        else:
            print("You select the wrong choice!!")
    else:
        print("Please enter the correct choice!!")

    print("Do you want to continue? press = 1", "Do you want to Exit? press = 0")
    press = int(input())
    n = press



