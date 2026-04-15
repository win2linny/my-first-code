from colorama import Fore, Back, Style, init  # 1. Added 'Back' here
import random
import platform 
import psutil 

# 2. Initialize colorama IMMEDIATELY so it's ready to go
init(autoreset=True)

# 3. Gather your static data
secret_pin = str(random.randint(1000, 9999))
machine_type = platform.machine()
os_name = platform.system()
version = platform.release()
network_name = platform.node()

print("\n--- INITIAL SYSTEM REPORT ---")
print(f"Architecture: {machine_type} | OS: {os_name} {version} | Session PIN: {secret_pin}")
print("-----------------------------\n")

while True:
    ram_usage = psutil.virtual_memory().percent
    print(f"[Current RAM Usage: {ram_usage}%]")
    
    user_name = input("Enter your name (or type 'exit' to quit): ")

    if user_name.lower() == "exit":
        print(Fore.RED + Style.BRIGHT + "Goodbye, Master. Powering down.")
        break 

    if user_name == secret_pin:
        # Now 'Back' will work because we added it to the import at the top!
        print(Fore.GREEN + Back.BLACK + "--- SECRET ADMIN ACCESS GRANTED ---")

    if user_name == "Big-John":
        print(Fore.CYAN + f"Welcome back, Master {user_name}.")
    
    # Optional: Add an 'else' for guests if you want!
    elif user_name.lower() != "exit" and user_name != secret_pin:
        print(Fore.YELLOW + f"Hello {user_name}, you are logged in as a guest.")
