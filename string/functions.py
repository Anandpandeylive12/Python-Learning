chai = "Lemon Tea"
print(chai)
# using replace function
replaceed_chai = chai.replace("Lemon", "Ginger")
print(replaceed_chai)

chai = "    Lemon Tea    "
print(chai)
# using strip function
print(chai.strip())

chai = "Lemon, ginger, masala"
# using split fnction for converting into list
print(chai.split(","))

chai = "Lemon Tea"
# using find function
print(chai.find("Tea"))
# using upper function
print(chai.upper())
# using lower function
print(chai.lower())


# use of the formate function
chai_type = "Lemon"
quantity = 2
order = "I would like {} cups of {} tea."
print(order.format(quantity, chai_type))


for letter in chai_type:
    print(letter)

chai = "He said,\"Masala chai is awesome\""