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
        
                