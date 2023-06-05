birthdays = {
    "Isis": " 24/10/2014",
    "Mario": " 04/01/1988",
    "Eu": "17/02/2989" }

print("welcome to birthday. We know the birthdays of:")
for name in birthdays:
    print(name)

print("Who birthday do you want to look up?")
name = input()
if name in birthdays:
      print(f"{name} birthdays is {birthdays[name]}")
else:
   print("Dont have this name")

