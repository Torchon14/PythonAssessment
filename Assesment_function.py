v1=0; v2 = 0; v3 = 0; v4 = 0;Kind= 0;v6=0; v5 = 0;Premium=0;v7 =0; typePolicy = ["Car Insurance","Home Insurance","Mobile Phone Insurance"]; methodPayment = ["Bank transfer","Paypal","Credit Card"]; fee = 0
counter =0

def Welcome(v1):
    v1 = input("Do you wish to create an Insurance Policy : Yes or No\n")
    if  v1 != "Yes" and v1 != "yes":
        print("Feel free to visit our website or ask the chatbot for any information")
        print("if you wish to create an Insurance Policy later then refresh the page")
        exit()
def fullName(v2) :
    v2 = input("Please insert your full name: \n")
    while v2[0] != v2[0].upper() or v2.isdigit() :
        print("Wrong name, please enter your true name")
        v2 = input("Please insert your full name: \n")
def policyDuration(v3):
    v3 = input("Please insert the requested duration of your policy (in years):\n")
    while  not v3.isnumeric():
        print("Incorrect ! Please enter a correct number (it needs to be an integer)")
        v3 = input("Please insert the requested duration of your policy (in years):\n")
    if v3.isnumeric():
        v3 = int(v3)
        return v3
def policyType(v4,v6):
     for type in typePolicy:
        print("Do you wish to select",type,"?")
        v4 = input ("Yes or No ?\n")
        if v4 == "Yes" or v4 == "yes":
            print("You have chosen", type, "as your policy")
            return type 
        else:
            continue
def policyPremium(kind,Premium,v3):
    if kind == typePolicy[0]:              
                Premium += 500*v3
                return Premium
    elif kind == typePolicy[1]:
                Premium += 1000*v3
                return Premium
    elif kind == typePolicy[2]:
                Premium += 120*v3
                return Premium       
def paymentMethod(fee,v5):
    for method in methodPayment:
        print("Do you wish to select",method,"?")
        v5 = input ("Yes or No ?\n")
        if v5 == "Yes" or v5 == "yes":
            v5 = method
            print("You have chosen", method, "as your payment method")
            if method == methodPayment[0]:              
                fee = 0
                return fee
            elif method == methodPayment[1]:
                fee = 0.10
                return fee
            elif method == methodPayment[2]:
                fee = 0.20
                return fee
        else: 
            continue


while True:
    if counter ==0:
        print("a policy")
    elif counter >0:
        v8 = input("another policy policy: Yes or No?\n")
        if v8 !="Yes" or v8 !="yes":
            exit()
    Kind = policyType(v4)
    v3 = policyDuration(v3)
    Premium = policyPremium(Kind,Premium,v3)
    fee = paymentMethod(fee)
    print()
    print("You have completed your profile !")
    Price = Premium*fee + Premium
    print()
    print(" Dear customer, you asked for a", v3,"years",Kind,"contract. The total cost using",v5,"is of £",Price)
    print()    
    counter += 1
    

    

 
