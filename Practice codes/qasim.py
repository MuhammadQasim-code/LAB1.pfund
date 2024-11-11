print("Movies Suggestions")
userinput=input("Which type of Movie do you want to watch : (hollywood/bollywood)").lower()
userinput2=input("Which type of movie genre do you like : (thriller/sci-fi)").lower()
userinput3=input("Which period of movie do you like to watch : (new/old)").lower()

if userinput=="hollywood" and userinput2=="thriller" and userinput3=="new" :
    movie="It should be \"Rebel Ridge\""
    
elif userinput=="hollywood" and userinput2=="sci-fi" and userinput3=="new" :
    movie="It should be \"Venom The Last Dance\" "
elif userinput=="hollywood" and userinput2=="sci-fi" and userinput3=="old" :
    movie="It should be \"Interstellar\" "
elif userinput=="hollywood" and userinput2=="thriller" and userinput3=="old" :
    movie=("It should be \"Mission Impossible\" ")
elif userinput=="bollywood" and userinput2=="thriller" and userinput3=="new" :
    movie=("It should be \"Salaar\" ")
elif userinput=="bollywood" and userinput2=="thriller" and userinput3=="old" :
    movie=("It should be \"Tiger Zinda Hai\" ")
    
else:
    movie="You should watch any series then"
    
print(movie)