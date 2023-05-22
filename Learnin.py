#basic print--------------------------------------

#print ('I like pizza!')
#print ("It's really good!")

#all variables------------------------------------

#first_name = 'Riley'
#last_name = 'Fowler'
#full_name = first_name +' '+ last_name
#print ('hello '+full_name)
#print (type(full_name))

#age = 20
#age += 1
#print('your age is ' +str(age))
#print(type(age))
#height = 250.5
#print ('your height is '+str(height)+'cm')
#print (type(height))

#human = True
#print (human)
#print (type(human))
#print('are you a human:'+str(human))

#Multiple assignment------------------------------

#name, age, attractive = 'Riley', 20, False

#print ('Name:' +str (name))
#print ('Age:'+str (age))
#print ('Are they attractive?: ' +str (attractive))

#Spongebob = Patrick = Squidward = Sandy = 30
#print (Spongebob)
#print (Patrick)
#print (Squidward)
#print (Sandy)

#string methods------------------------------------

#name = 'riLey'
#print (len(name))
#print (name.find('i'))
#print (name.capitalize())
#print (name.upper())
#print (name.lower())
#print (name.isdigit())
#print (name.isalpha())
#print(name.count('r'))
#print (name.replace('r','y'))
#print (name*5)

#type casting-------------------------------------

#x = 1   #int
#y = 2.0 #float
#z = '3' #str

#x = float(x)
#y = int(y)
#z = int(z)

#print(x)
#print(y)
#print(z)

#print(z*3)

#user input basic---------------------------------------

#name = input("What is your name?: ")
#print("Hello " +name)

#age = input("How old are you?: ")
#print(("You are " +age)+" years old")

#inputs with type casting below////////////////////////

#age = int(input("How old are you?: "))
#age = age + 1
#print("Next year you will be "+str(age)+" years old.")

#weight = float(input('How much do you weigh in pounds,exactly? '))
#weight = weight - 20
#print("Wowza! Lay off those cupcakes, and maybe you could weigh "+str(weight)+" pounds!")

#height = int(input('Okay, Okay. One last question...how tall are you in inches?: '))
#print(str(height) + " inches" + "...dang, look at this midget! Is your last name Gaylord?!?!")

#math functions----------------------------------------

#pi = 3.14
#import math

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))

#pi = -3.14
#print(abs(pi))

#x = 1
#y = 2
#z = 3

#print(max(x,y,z))
#print(min(x,y,z))

#string slicing-----------------------------------------

#name = "Riley Fowler"

#first_name = name[0] #starting index
#first_name = name[0:5]  # also [:5] #stopping index
#last_name = name[6:12]  # also [6:] #substring
#funky_name = name[0:12:2]  # also [::2] #step index
#reversed_name = name[::-1]  # reverse a string

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#slice function////////////////////////////////////////

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7,-4)

#print (website1[slice])
#print (website2[slice])

#if/elif/else statements------------------------------------------

#age = int(input("How old are you?: "))

#if age == 100:
    #print("You're a century old!")
#elif age >= 18:
    #print("You're an adult!")
#elif age < 0:
    #print("You haven't been born yet!")
#else:
    #print("You're a minor!")

#logical operators (and,or,not)------------------------------------

#temp = int(input("What is the temperature outside? "))

#if temp >= 32 and temp <= 86:
    #print("The temperature is good today!")
    #print("Go outside!")
#elif temp < 32 or temp > 86:
    #print("The temperature is bad today!")
    #print("Stay inside!")

#if not (temp >= 32 and temp <= 86):
    #print("The temperature is bad today!")
    #print("Stay inside!")
#elif not (temp < 32 or temp > 86):
    #print("The temperature is good today!")
    #print("Go outside!")

#while loops-------------------------------------------------------

#while 1==1:
    #print("Help! I'm stuck in an infinite loop!")

#name = ""
#while len(name) == 0:
    #name = input("Enter your name: ")

#print("Hello "+name)

#another way to write it//////////////////////////////////////////

#name = None

#while not name:
    #name = input("Enter your name: ")

#print("Hello "+name)

#for loops-------------------------------------------------------

#for i in range(10):
    #print(i+1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Riley Fowler":
    #print(i)

#import time

#for seconds in range(10,0,-1): #doesn't have to be "seconds" can be "i" or anything
    #print(seconds)
    #time.sleep(1)
#print("Countdown Complete!")

#nested loops------------------------------------------------------

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end= "")
    #print()

#loop control statements--------------------------------------------
#break = used to terminate the loop entirely.
#continue = skips to the next iteration of the loop.
#pass = does nothing, acts as a placeholder.

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):

    if i == 13:
        pass
    else:
        print(i)

#lists---------------------------------------------------