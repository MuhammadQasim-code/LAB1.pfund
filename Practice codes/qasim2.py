print("Clothes suggestions")

userinput=input("Which type of clothes you want to wear? (western/desi)").lower()
userinput2=input("What should be the fabric of your cloth? (cotton/silk)").lower()

if userinput=="desi" and userinput2=="cotton":
    cloth="It should be Cotton Kurta Shalwar"
    
elif userinput=="desi" and userinput2=="silk":
    cloth="It should be silky Kurta Shalwar"
    
elif userinput=="western" and userinput2=="cotton":
    cloth="It should be casual T-shirt and Jeans"
    
elif userinput=="western" and userinput2=="silk":
    cloth="It should be some wedding dress"
    
else:
    cloth="You should consider denim for western or khaddar for desi "
    
print(cloth)

