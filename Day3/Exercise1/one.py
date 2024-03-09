country_density={"China":143,"India":136,"USA":32,"Pakistan":21}

user=int(input("Make a choice\n1. Print Countries and their population\n2. Add country and population\n3. Remove country\n4. Query\n"))

if user == 1:
    for key,value in country_density.items():
        print(f'{key}==>{value}')

elif user ==2:
    new_country=input("Enter new country\n")
    if new_country in country_density:
        print("It already exists")
    else: 
        new_population = int(input(f'Enter the population size of {new_country}\n'))
        country_density[new_country]=new_population
        print(country_density)
elif user ==3:
    remove_country=input("Enter the country you want to remove\n")
    if remove_country in country_density:
        del country_density[remove_country]
        print(country_density)
    else:print("The country does not exist")

elif user == 4:
    query = input("Which country do you want to see the population\n")
    if query in country_density:
        print(f'The population of the country is {country_density[query]}')
    else:print("The country does not exist")
    
else:print("The option does not exist")
                