#Justin Love
#Project 5
#Farm
#10/17/2022

import random
def welcome():
    print("Welcome to the chicken and eggs app!")
def get_chickens():
    while True :
       number = int(input("Enter the number of chickens (1-100):"))
       if (number < 0 or number > 100):
            print("Number of chicken must be in the range of 1 to 100")
       elif (number >= 0 and number <= 100):
           return number        

def get_eggs(number_of_chickens):
    
    egg_list = []
    while(number_of_chickens >0):
        egg_list.append(random.randint(0,7))
        number_of_chickens -= 1
    return egg_list
        
    
def print_stats(c,eggs):
    a = max(eggs)
    b = eggs.index(a)
    b=b+1
    print("Chicken # ",b,"is the champ with ",a,"eggs.")
    d = eggs.count(a)
    #g = g - 1
    print("There are ",d,"other chickens that are joint champions.")
    
def main():
    welcome()
    chicken = get_chickens()
    eggs = get_eggs(chicken)
    print(eggs)
    print_stats(chicken,eggs)
    
        
    
main()
