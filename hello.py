import platform 

machine_type = platform.machine()
os_name = platform.system()
version = platform.release()
network_name = platform.node() # I changed this to lowercase to match below

print("\n--- SYSTEM REPORT ---")

print(f"Processor Architecture: {machine_type}")
print(f"Operating System: {os_name}")
print(f"OS Version: {version}")
# Added the variable and fixed the closing quote/parenthesis
print(f"Network Name: {network_name}") 
print("---------------------\n")
# Part 2: Interactive Logic
# input() stops the program and waits for you to type something
user_name = input("Enter your name: ")

# The 'if' statement checks a condition
# We use '==' to compare (one '=' is for assigning, two '==' if for checking)
if user_name == "Big-John":
    print(f"Welcome back, Master {user_name}. Your iMac is ready.")
else:
    print(f"Hello {user_name}, you are logged in as a guest.")    
    
