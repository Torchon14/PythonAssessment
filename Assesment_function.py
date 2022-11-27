v1=0; v2 = 0; v3 = 0; v4 = 0; v5 = 0;Premium=0;v7 =0; typePolicy = ["Car Insurance","Home Insurance","Mobile Phone Insurance"]; methodPayment = ["Bank transfer","Paypal","Credit Card"]


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
    #float(v3)
    while  not v3.isnumeric():
        print("Incorrect ! Please enter a correct number (it needs to be an integer)")
        v3 = input("Please insert the requested duration of your policy (in years):\n")
def policyType(Premium):
    
   for type in typePolicy:
        print("Do you wish to select",type,"?")
        v4 = input ("Yes or No ?\n")
        if v4 == "Yes" or v4 == "yes":
            print("You have chosen", type, "as your policy")
            if type == typePolicy[0]:              
                Premium == 500
                break
            elif type == typePolicy[1]:
                v6 += 1000
                break
            elif type == typePolicy[2]:
                v6 += 120
                break 
        else:
            continue 

        
def paymentMethod(v5):
    for method in methodPayment:
        print("Do you wish to select",method,"?")
        v5 = input ("Yes or No ?\n")
        if v5 == "Yes" or v5 == "yes":
            v5 = method
            print("You have chosen", method, "as your payment method")
            print(v5)
            break       
        else: 
            continue

  

policyType(0)      
print(Premium)

