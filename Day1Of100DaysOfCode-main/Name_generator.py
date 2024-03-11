#This is a python file that generates a band name.

def generate_band_name():
    print("Let's generate a name for your band!")
    birth_city = input("Where were you born?: ")
    pet_name = input("What is the name of your first pet?: ")
    num_siblings = input("In digits, how many sibligs do you have?: ")
    
    print("Yaaay! Your band name is: "+ birth_city +" "+pet_name+num_siblings+"'s")
    
generate_band_name()