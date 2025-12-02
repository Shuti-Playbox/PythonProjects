import hashlib

#Takes hash from userinput
pswd = input("Enter your MD5 hash: ")

#Reads password list
pswd_file = open("password.txt", "r")

#takes each line in the password list makes an md5 hash of it and compares to it to the input from the user
for line in pswd_file:
    hashed_pswd = hashlib.md5(line.encode()).hexdigest()
    if hashed_pswd == pswd:
        print(f"{pswd} is equal to {line} ")
    else:
        break
print("No matches could be found")






