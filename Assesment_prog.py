import Assesment_function
#variables
v1= 0;v2 = 0; v3 = 0; v4 = 0; v5 = 0; Kind = 0;Premium = 0; fee = 0; Price =0; typePolicy = ["Car Insurance","Home Insurance","Mobile Phone Insurance"]; methodPayment = ["Bank transfer","Paypal","Credit Card"]

#Program

print('Welcome to Admiral Insurance')
Assesment_function.Welcome(v1)
print("Esteemed customer ! It is time to establish your profile !")
Assesment_function.fullName(v2)
print(typePolicy)
Kind = Assesment_function.policyType(v4)
v3 = Assesment_function.policyDuration(v3)
Premium = Assesment_function.policyPremium(Kind,Premium,v3)
fee,v5 = Assesment_function.paymentMethod(fee)
print()
print("You have completed your profile !")
Price = Premium*fee + Premium
print()
print(" Dear customer, you asked for a", v3,"years",Kind,"contract. The total cost using",v5,"is of £",Price)
print()

   
# à améliorer = FullName verification,
#               for PolicyType and paymentMethod need to block if answer never yes in loop
#               mixing Policy, 
#               adding sentences during the profil establishment
#               Allow user to choose in months to respect the phone Insurance policy