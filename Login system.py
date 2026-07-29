# Login system
correct_username="Hafsa"
correct_pass="python123"
user=input("Enter username: ")
passw=input("Enter password: ")

if user==correct_username and passw==correct_pass:
    print("Login successful.Welcome!")
elif user==correct_username:
    print("Incorrect password")
else:
   print("Try again")