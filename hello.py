import random
import platform 
import psutil 

# Static system info (runs once)
secret_pin = str(random.randint(1000, 9999))
machine_type = platform.machine()
os_name = platform.system()
version = platform.release()
network_name = platform.node()

print("\n--- INITIAL SYSTEM REPORT ---")
print(f"Architecture: {machine_type} | OS: {os_name} {version} | Session PIN: {secret_pin}")
print("-----------------------------\n")

while True:
    # Real-time RAM check (runs every time the loop repeats)
    ram_usage = psutil.virtual_memory().percent
    
    print(f"[Current RAM Usage: {ram_usage}%]")
    user_name = input("Enter your name (or type 'exit' to quit): ")

    if user_name.lower() == "exit":
        print("Goodbye, Master. Powering down.")
        break 
    if user_name == secret_pin:
        print("SECRET ADMIN ACCESS GRANTED. Accessing core files...")

    if user_name == "Big-John":
        print(f"Welcome back, Master {user_name}. Your iMac is ready.")
    else:
        print(f"Hello {user_name}, you are logged in as a guest.")
