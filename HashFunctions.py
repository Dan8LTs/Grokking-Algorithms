# dict is based on a hash table
# 5.5
phone_numbers = {}
phone_numbers["Ivan"] = 89318342312
phone_numbers["Alexey"] = 81239238343
print(phone_numbers.get("Alexey"))


voted = {}
for i in range(4):
    print("My name is: ", end='')
    name = input()
    if voted.get(name) == None:
        voted[name] = True
    else:
        print("You can't vote!")
print(voted)


# 5.7
books = {"Robinsone Crusoe": "Daniel Defo", "Who will cry when you die?": "Robin Sharma"}


def return_name(author):
    for key, value in books.items():
        if value == author:
            return key


print(return_name("Daniel Defo"))
