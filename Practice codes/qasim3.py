print("Car suggestions")
userinput=input("Which type of car do you want? (luxury car/sports car)").lower()
userinput2=input("Which brand will you chose for your car? (bmw /mercedes )").lower()
userinput3=input("Which colour do you want? (blue/black/red)").lower()

if userinput=="luxury car" and userinput2=="bmw" and userinput3=="blue":
    car="It should be BMW 8 series"
elif userinput=="luxury car" and userinput2=="bmw" and userinput3=="black":
    car="It should be BMW 7 series"
elif userinput=="sports car" and userinput2=="bmw" and userinput3=="black":
    car="It should be BMW i8"
elif userinput=="sports car" and userinput2=="bmw" and userinput3=="blue":
    car="It should be BMW M4 Coupe"
    
elif userinput=="sports car" and userinput2=="mercedes" and userinput3=="blue":
    car="It should be Mercedes-AMG GT"
elif userinput=="sports car" and userinput2=="mercedes" and userinput3=="black":
    car="It should be Mercedes-AMG C63s Coupe"
    
elif userinput=="luxury car" and userinput2=="mercedes" and userinput3=="black":
    car="It should be Mercedes Benz S Class"
elif userinput=="luxury car" and userinput2=="mercedes" and userinput3=="blue":
    car="It should be Mercedes Benz C Class"
    
else:
    car="Audi should be the best option for you then."

print(car)
