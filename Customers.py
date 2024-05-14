import pandas as pd
import random
games = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\Games.csv")
male_names = ["Sebastian", "Luca", "Mateo", "Liam", "Gabriel", "Matteo", "Nikolai", "Enzo", "Alexander", "Hugo", 
              "Daniel", "Lucas", "David", "Benjamin", "Maximilian", "Samuel", "Noah", "Leon", "Lukas", "Antonio", 
              "Aaron", "Filip", "Vincent", "Elias", "Nico", "Jonas", "Milo", "Tom", "Oscar", "Hannah", "Tobias", 
              "Paul", "Emil", "Leonardo", "Marco", "Jonah", "Christian", "Nicolas", "Jacob", "Adrian", "Emanuel", 
              "Tim", "Bastian", "Raphael", "Sam", "Alex", "Dominic", "Michael", "Julian", "Fabian", "Nathan", 
              "Luca", "Rafael", "Mario", "Emilio", "Henry", "Kai", "Anton", "Thomas", "Erik", "Simon", "Bruno", 
              "Dylan", "Jasper", "Marius", "Ethan", "Timo", "Tommy", "Fabio", "Richard", "Peter", "Fritz", "Oskar", 
              "Louis", "Julius", "Julien", "Jonathan", "Andreas", "Jan", "Maksim", "Gustav", "Elias", "Christian", 
              "Severin", "Florian", "Leonard", "Valentin", "Karl", "Roman", "Nicolas", "Emil", "Fabian", "Jonas", 
              "Leander", "Hannes", "Mattias", "Markus", "Maximilian", "Leopold", "Marcel", "Alfred", "Jannik", 
              "Valentin", "Alexander", "Emanuel", "Benedikt", "Kilian", "Lars", "Fabio", "Philipp", "Florian", 
              "Dominik", "Jakob", "Malte", "Benedikt", "Paul", "Lukas", "Tim", "David", "Robin", "Valentin", 
              "Lennard", "Stefan", "Kevin", "Jannis", "Marvin", "Finn", "Fabian", "Julian", "Fabian", "Vincent", 
              "Levin", "Sebastian"]
female_names = ["Sophie", "Elena", "Isabella", "Ava", "Mia", "Eva", "Amelia", "Sofia", "Luna", "Julia", "Leah", 
                "Emma", "Lily", "Olivia", "Ella", "Chloe", "Sophia", "Isabelle", "Grace", "Emily", "Charlotte", 
                "Alice", "Zoe", "Anna", "Sophie", "Juliette", "Mila", "Victoria", "Alicia", "Amelie", "Nora", 
                "Eva", "Madison", "Eva", "Lea", "Grace", "Aurora", "Ivy", "Sarah", "Amelia", "Lucia", "Clara", 
                "Elena", "Lara", "Lia", "Ella", "Olivia", "Matilda", "Rose", "Elise", "Holly", "Daisy", "Ruby", 
                "Jasmine", "Layla", "Harper", "Gabriella", "Eliza", "Evelyn", "Jade", "Amber", "Leah", "Ellie", 
                "Isla", "Nina", "Hazel", "Luna", "Georgia", "Aria", "Molly", "Penelope", "Skye", "Mia", "Freya", 
                "Ella", "Poppy", "Avery", "Hannah", "Zara", "Niamh", "Sofia", "Aisha", "Tara", "Leila", "Phoebe", 
                "Cora", "Iris", "Natalie", "Sienna", "Esme", "Paige", "Lydia", "Fiona", "Harriet", "Imogen", 
                "Megan", "Lacey", "Nova", "Aria", "Sasha", "Eloise", "Angelina", "Gabrielle", "Aria", "Lilly", 
                "Sadie", "Alexa", "Delilah", "Catherine", "Anya", "Summer", "Juliana", "Eden", "Ayla", "Taylor", 
                "Leia", "Josephine", "Bella", "Adeline", "Daniela", "Alessandra", "Ariel", "Lillian", "Madeleine", 
                "Rebecca", "Anastasia", "Vanessa", "Holly", "Morgan", "Violet", "Rosie", "Lyla", "Adelaide", 
                "Isabel", "Alexandra", "Marina"]
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", 
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", 
    "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", 
    "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", 
    "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos"]
ratings = [1, 1, 2, 2, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
t = [int(random.normalvariate(16, 2)) for _ in range(4500)]
t = [age if 10 <= age <= 29 else random.randint(10, 19) for age in t]
r = [random.randint(30, 70) for _ in range(500)]
ages = t + r
genders = ['Male', 'Male', 'Male', 'Male', 'Female']
mh = [random.normalvariate(3.5, 0.5) for _ in range(4200)]
mh = [min(max(3, hour), 4) for hour in mh]
rh = [random.uniform(0, 10) for _ in range(800)]
rh = [hour for hour in rh if 3 <= hour <= 4]
hours_in_game = mh + rh
countries = ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
    "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Iceland", "Ireland", "Italy", "Kazakhstan", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", 
    "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", 
    "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City", "Kazakhstan", "Kyrgyzstan", "Tajikistan",
    "Turkmenistan", "Uzbekistan", "Canada", "United States", "China", "United States", "China", "United States", "China", 
    "United States", "China", "United States", "China", "United States", "China", "United States", "China", "Kazakhstan", 
    "Kyrgyzstan", "Uzbekistan", "Russia", "Russia", "Russia", "Russia", "Russia", "Russia", "Moldova", "Monaco", 
    "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", 
    "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine"]
df = pd.DataFrame(columns=['Name', 'Surname', 'Age', 'Gender', 'Daily Hours in Game', 'Game', 'Rating', 'Country'])
for i in range(5000):
    gender = random.choice(genders)
    if gender == 'Male':
        name = random.choice(male_names)
    else:
        name = random.choice(female_names)
    age = random.choice(ages)
    surname = random.choice(surnames)
    daily = random.choice(hours_in_game)
    rating = random.choice(ratings)
    country = random.choice(countries)
    game = random.choice(games["Title"])
    df.loc[len(df)] = [name, surname, age, gender, round(daily, 1), game, rating, country]
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\Customers.csv", index=False)