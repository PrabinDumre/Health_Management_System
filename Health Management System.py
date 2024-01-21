""" Health Management System
3 clients - Prabin Arastu Somnath


total 6 files
write a function that when executes takes as input client name
function for diet or exercise

"""
def getdate():
    import datetime
    return datetime.datetime.now()

def log(q):
    if (q == 1):
        print("What do you want of Prabin's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("prabin-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("prabin-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u )
                print("Succesfully Written")
    elif (q == 2):
        print("What do you want of Arastu's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("Arastu-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("Arastu-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u)
                print("Successfully Written")
    else:
        print("What do you want of Somnath's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("Somnath-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("Somnath-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u )
                print("Successfully Written")

def retrieve(q):
    if (q == 1):
        print("What do you want to retrieve of Prabin's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("prabin-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("prabin-exercise.txt") as p:
                i = p.readlines()
                print(i)
    elif (q == 2):
        print("What do you want of Arastu's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("Arastu-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("Arastu-exercise.txt") as p:
                i = p.readlines()
                print(i)

    else:
        print("What do you want of Somnath's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("Somnath-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("Somnath-exercise.txt") as p:
                i = p.readlines()
                print(i)

print("HEALTH MANAGEMENT SYSTEM")
print("You want to log or retrieve the data?")
print("Press '1' to log or press '2' to retrieve")
p = int(input())
if(p==1):
    print("Whose Data you want to Log?")
    print("Press 1 for Prabin's "
          "Press 2 for Arastu's"
          "Press 3 for Somnath's")
    q = int(input())
    log(q)

else:
    print("Whose Data you want to Retrieve?")
    print("Press 1 for Prabin's "
          "Press 2 for Arastu's"
          "Press 3 for Somnath's")
    q = int(input())
    retrieve(q)


