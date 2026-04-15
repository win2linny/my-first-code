import platform 
import psutil  # <--- New toolbox!

machine_type = platform.machine()
os_name = platform.system()
version = platform.release()
network_name = platform.node()

# New Variable: This grabs the % of RAM being used right now
ram_usage = psutil.virtual_memory().percent

print("\n--- SYSTEM REPORT ---")
print(f"Processor Architecture: {machine_type}")
print(f"Operating System: {os_name}")
print(f"OS Version: {version}")
print(f"Network Name: {network_name}") 
print(f"RAM Usage: {ram_usage}%") # <--- Display the percentage
print("---------------------\n")

# Your loop stays exactly the same below this...
while True:
    user_name = input("Enter your name (or type 'exit' to quit): ")
    if user_name.lower() == "exit":
        print("Goodbye, Master. Powering down.")
        break 
    if user_name == "Big-John":
        print(f"Welcome back, Master {user_name}. Your iMac is ready.")
    else:
        print(f"Hello {user_name}, you are logged in as a guest.")
