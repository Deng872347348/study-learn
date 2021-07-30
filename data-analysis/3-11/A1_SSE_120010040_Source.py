import random
import math

print("Welcome to the sliding puzzle game!")
print("In this game, you need to use your wisdom to finish this game! ")

def gettingSize():
    while True:
        size = input("Please input the desired dimension of game:")
        try:
            size = int(size)
            if size < 3 or size > 10:
                print("Invalid Input")
                continue
            else:
                break
        except:
            print("Invalid Input")
            continue
    return size


def constrMatrix(size):
    list1 = []
    list2 = []
    for i in range(size**2):
        list1.append(i)

    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(list1.pop(random.randint(0, len(list1) - 1)))
        list2.append(temp)
    return list2

def solvable(list2):
    if len(list2) % 2 == 0:
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                if list2[i][j] == 0:
                    if i % 2 ==0:
                        return False
                    else:
                        return True
    else:
        return True

def win(list2):
    A_list2 = []
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            A_list2.append(list2[i][j])
    win_list2 = A_list2.copy()
    win_list2.sort()
    win_list2.append(win_list2[0])
    win_list2.remove(0)
    if A_list2 == win_list2:
        return True
    else:
        return False

def Moving():
    while True:
        move = input("Please enter your desired move button [l, r, u, d]")
        if move == "exit":
            print("exit game")
            return move
        if move != "l" and move != "r" and move != "d" and move != "u":
            print("Invalid Input")
            continue
        else:
            return move 

#def Moving():
    #while True:
        #moving = input("Please input your desired move buttons:")
        #if moving == "exit":
            #print("Exit Game")
            #return move
        #else:
            #return move


def movingRight(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] == 0:
                if j != 0:
                    list2[i][j] = list2[i][j-1]
                    list2[i][j-1] = 0
                    return list2

def movingDown(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] == 0:
                if i != 0:
                    list2[i][j] = list2[i-1][j]
                    list2[i - 1][j] = 0
                    return list2

def movingLeft(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] == 0:
                if j != len(list2[i]) - 1:
                    list2[i][j] = list2[i][j+1]
                    list2[i][j + 1] = 0
                    return list2

def movingUp(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if list2[i][j] == 0:
                if i != len(list2) - 1:
                    list2[i][j] = list2[i + 1][j]
                    list2[i + 1][j] = 0
                    return list2

def make_move(move, list2):
    if move == "r":
        movingRight(list2)
    if move == "d":
        movingDown(list2)
    if move == "l":
        movingLeft(list2)
    if move == "u":
        movingUp(list2)

def print_list2(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            spacing = int(math.sqrt(size)) - len(str(list2[i][j]))
            if list2[i][j] == 0:
                print(" " * spacing + " ", end=" ")
            else:
                print(" " * spacing + str(list2[i][j]), end=" ")
        print()

def response():
    while True:
        response = input("Do you want to play again or not? :")
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid Input")
            continue
#-----------------------------------------------
while True:
    size = gettingSize()
    list2 = constrMatrix(size)
    print("If you want to exit this puzzle game, just input 'exit'")

    print("In order to solve this puzzle game, you need to order the random numbers in numerical order from left to right or top to bottom")

    print_list2(list2)
    movingNumber = 0
    while True:
        move = Moving()
        if move == "exit":
            break
        make_move(move, list2)
        movingNumber += 1
        print_list2(list2)
        if win(list2):
            print("Great! You win this game!" + "You used " + str(movingNumber) + "moves in total.")
            break
    if win(list2) == True:
        break
    if response():
        continue
    else:
        print("exit game")
        break



