import random

subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "A mumbai cat",
    "Nirmala",
    "A group of monkeys",
    "Prime minister modi",
    "Auto rickshaw Driver",

]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_things = [

    "at red fort",
    "in mumbai locak train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during ipl match",
    "at india gate",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_things = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_things}"
    print("/n"+ headline)


    user_input = input("\nDo you want another headline? (yes/no)").strip().lower
    if user_input =="no":
        break

    print("\n thanks for using the fake news headline generator. have a fun day")