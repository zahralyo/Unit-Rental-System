print ("\t\tWELCOME TO UNITEN BUSINESS DEVELOPMENT UNIT RENTAL SYSTEM")

print ("\n\n")
print ("\t\t\t\t\t*~~~~~~~~~~~~~~~~*")
print ("\t\t|                    List Of Facilities                    |")
print ("\t\t\t\t\t*~~~~~~~~~~~~~~~~*")
print ("\t\t|   1.PBL Classroom (30pax)   |")
print ("\t\t|   2.Meeting Room (60pax)   |")
print ("\t\t|   3.Workstation Computer Lab ITMS (30pax)   |")
print ("\t\t|   4.Swimming Pool    |")



try:
    facility = int(input ("Please enter your option \n(Insert the choosen number only  :")) 
except ValueError:
        print("Please enter only numeric number) :) ")
        facility = int(input("Please enter your option \n(Insert the choosen number only  : "))


if facility == 1 :
    print("\nCOOL ! You choose PBL Classroom <3.")
elif facility == 2 :
        print ("\nCOOL ! You choose Meeting Room <3.")
elif facility == 3 :
        print ("\nCOOL ! You choose Workstation Computer Lab ITMS <3.")
elif facility == 4 :
        print ("\nCOOL ! You choose Swimming Pool <3.") 
else:
    print ("Oopss! Please re-enter the correct facility number given by the system ;) ")
    facility =int(input ("Please enter your option\n(Insert relevant number only)  : "))


user_identity = input("\nAre you a Uniten Student/Staff \n(Type Yes/No)          : ")


def day_of_booking():
    print("\nYou choose ",days," as option !\n")
    
if user_identity == "Yes" or user_identity == "YES" or user_identity == "yes" :
    id_card = input ("Please insert your Student/Staff ID : ")
    print ("\n\n(Monday - Sunday p/s: Kindly mention the day only ) ")
    days = input("\nHi UNITENOS!\nWhen would you like to book(Monday - Sunday) : ")
    day_of_booking()
elif user_identity == "No" or user_identity == "NO" or user_identity == "no":
    id_card = "NONE"
    days = input("\nHello There Fella!<3\nWhen would you like to book(Monday - Sunday) : ")
    day_of_booking()



hours_rent = int(input("\nHow many hours would you like to rent ( Please enter numbers only) : "))


def summary():
    print ("")
    print ("n\t\t\t\t<<<Rental Details>>> \n")
    print ("\t\t*~~~~~~*")
    print ("\n\t\t|Facilities           : ",fac)
    print ("\n\t\t|Uniten Student\Staff : ",user_identity)
    print ("\n\t\t|ID Card              : ",id_card)
    print ("\n\t\t|Day                  : ",days)
    print ("\n\t\t|Hours                : ",hours_rent)
    print ("\n\t\t*~~~~~~*")



    

if facility == 1:
    fac = "PBL Classroom"
elif facility == 2:
    fac = "Meeting Room"
elif facility == 3:
    fac = "Workstation Computer Lab ITMS"
elif facility == 4:
    fac = "Swimming Pool"


if user_identity == "Yes" or user_identity == "YES" or user_identity == "yes":
    identity ="Yes"
else:
    id_uniten = "No"


summary()
if days in ["Monday", "monday","Tuesday", "tuesday","Wednesday","wednesday","Thursday", "thursday","Friday" "friday"]:
    if user_identity=="Yes" or user_identity=="yes":
        if facility==1:
            total_pay = 100*hours_rent
            print("Total amount you need to pay : RM",total_pay)
        elif facility==2:
            total_pay = 100*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==3:
            total_pay = 200*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==4:
            total_pay = 30*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
    elif id_uniten == "No" or id_uniten=="no":
        if facility==1:
            total_pay = 150*hours_rent
            print("Total amount you need to pay : RM",total_pay)
        elif facility==2:
            total_pay = 150*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==3:
            total_pay = 250*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==4:
            total_pay = 60*hours_rent
            print ("Total amount you need to pay : RM",total_pay)


else:
    if id_uniten == "Yes" or id_uniten =="yes":
        if facility==1:
            total_pay = 150*hours_rent
            print("Total amount you need to pay : RM",total_pay)
        elif facility==2:
            total_pay = 150*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==3:
            total_pay = 250*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==4:
            total_pay = 35*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
    elif id_uniten == "No" or id_uniten =="no":
        if facility==1:
            total_pay = 200*hours_rent
            print("Total amount you need to pay : RM",total_pay)
        elif facility==2:
            total_pay = 200*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==3:
            total_pay = 300*hours_rent
            print ("Total amount you need to pay : RM",total_pay)
        elif facility==4:
            total_pay = 65*hours_rent
            print ("Total amount you need to pay : RM",total_pay)

pay_input = float(input("Please insert the amount of payment:RM "))

total = total_pay
while (total > pay_input):
    total = total - pay_input
    print("\n\t\tPlease continue your payment\n")
    print("Total amount you need to pay:RM ",total)
    pay_input = float(input("Please insert amount of payment that you would like to pay:RM "))

print("")
print("\t\t\t Your Payment Has Completed\n")
input("\t\t<<<Thank You For choosing Uniten Business Rental Service>>>")
print ("\n\n\nPress enter to quit program")
