user_name = "Joey"
query = input("Please enter the user name: ").title().strip()
if query == user_name:
    print("Hello, {}! The password is: W@12".format(query))
else:
    print("Hello, {}! See you later.".format(query))
