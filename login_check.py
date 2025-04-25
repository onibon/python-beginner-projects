print("Log into your account")
attempts = 0
while attempts < 3:
    username = input("type in your username here: ").lower()
    password = input("password: ")
    if username == "admin" and password == "pass123":
     print("welcome admin")
     break   
    else:
     attempts += 1
     print(f"wrong username or password. {3 - attempts} attempt(s) left.")

if attempts == 3:
     print("too many failed attemppts. try again later.")
