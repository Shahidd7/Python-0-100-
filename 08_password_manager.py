import hashlib
import base64
import os
def setup_master_pass():
    password = input("Create a master password:")
    hashed = password.encode()
    secure_hash = hashlib.sha256(hashed).hexdigest()
    with open("master.hash" , "w") as f:
        f.write(secure_hash) 
    print("Master Password set successfully!")

def login():
    master_pass = input("Enter the your password:")
    hashed_m = master_pass.encode()
    master_hash = hashlib.sha256(hashed_m).hexdigest()
    try:
        with open("master.hash" , "r") as f:
            user_hash = f.read()
            if master_hash == user_hash:
                print("access granted")
            else:
                print("access denied")
    except FileNotFoundError:
        print("No master password set!please set one")

def add_password():
    password = input("Enter password:")
    website = input("Enter website:")
    username = input("Enter username:")
    encoded_pass = base64.b64encode(password.encode()).decode()
    with open("password.txt" , "a") as f:
        f.write(f"{website},{username},{encoded_pass}\n")
    print(f"Password for {website} set successfully")

def view_password():
    try:
        with open("password.txt" , "r") as f:
            for line in f:
                website, username, encoded_pass = line.strip().split(",")

                decoded_pass = base64.b64decode(encoded_pass).decode()
                print(f"website : {website} | Username : {username} | Password : {decoded_pass}")
    except FileNotFoundError:
        print("No password Saved Yet")

def main():
    if not os.path.exists("master.hash"):
        print("first time setup detected")
        setup_master_pass()
    for attempt in range(3):
         master_pass = input("Enter the your password:")
         master_hash = hashlib.sha256(master_pass.encode()).hexdigest()
         try:
             with open("master.hash" , "r") as f:
                 saved_hash = f.read()
                 if master_hash == saved_hash:
                     print("Access Granted")
                     break
                 else:
                     print(f"Access denied!!  {2 - attempt} remaining")
         except FileNotFoundError:
             print("Error: Master password file missing!")
             return
    else:  # <-- This belongs to the FOR loop. Only runs if they fail 3 times.
            print("Too many failed attempts. Goodbye.")
            return  # Kills the program!
         
    while True:
             print("\n--- Password Manager ---")
             print("1. Add a Password")
             print("2. View Passwords")
             print("3. Quit")
             choice = input("Choice: ")

             if (choice == "1"):
                 add_password()
             elif(choice == "2"):
                 view_password()
             elif(choice == "3"):
                 print("Goodbye")
                 break

main()        
        

 