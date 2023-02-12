import time
from datetime import datetime as dt

# Define the hosts file path
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Define the temporary hosts file path
hosts_temp = "hosts"

# Define the websites you want to block
websites = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

# Function to block websites
def block_websites():
    print("Blocking websites...")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in websites:
            if website in content:
                pass
            else:
                file.write(f"127.0.0.1 {website}\n")

# Function to unblock websites
def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()
    print("Websites unblocked successfully!")

# Ask the user if they want to block or unblock websites
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