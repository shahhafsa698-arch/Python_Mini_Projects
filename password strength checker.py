# Password strength checker
def check_pass_strength(password):
    if len(password) == 8:
        return "Strong"
    elif len(password)>=5:
        return "Medium"
    else:
        return "Weak"

password=(input("Enter password: "))
#function call
ch_pass=check_pass_strength(password)

print("Password level is:",ch_pass)

