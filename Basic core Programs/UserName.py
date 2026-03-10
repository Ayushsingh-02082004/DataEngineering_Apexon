template = "Hello <<UserName>> , How are you?"

name = input("Enter user name: ")

if len(name) < 3:
    print("Name must have at least 3 characters")
else:
    result = template.replace("<<UserName>>" , name)
    print(result)
