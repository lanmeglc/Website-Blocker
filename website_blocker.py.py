import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

hosts_temp = "hosts"

websites = ["websites", "websites", "websites"]

def block_websites():
    print("Blocking websites...")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in websites:
            if website in content:
                pass
            else:
                file.write(f"127.0.0.1 {website}\n")

def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()
    print("Websites unblocked successfully!")

user_input = input("Do you want to block or unblock websites? (B/U): ").upper()
if user_input == "B":
    start_hour = int(input("Enter the hour at which you want to start blocking websites (0-23): "))
    end_hour = int(input("Enter the hour at which you want to stop blocking websites (0-23): "))
    block_websites()
elif user_input == "U":
    unblock_websites()
else:
    print("Invalid input. Exiting program.")
    exit()
