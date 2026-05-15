age = 20 ;
result = 80 ;
percentage =  "90%" ;

if age >= 18 :
    print("you are eligible for admission")
    if result >= 80 :
        print("eligible for top programs")
    if result >= 60 and result <= 79 :
        print("normal admission")
    else:
        print("not eligible")
        
if percentage >= "80%" :
    print("full eligible")
    if percentage >= "70%" and percentage <= "79%" :
        print("Conditional admission")
    else:
        print("rejected")

fees = str(input("enter the fees status"))
if fees == "paid" :
    print("admission confirmed")
    if fees == "not paid " :
        print("admission unhold")

