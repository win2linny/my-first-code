import platform  # This 'imports' the toolbox for system info

# We are creating 'variables' to store the info the toolbox finds
machine_type = platform.machine()
os_name = platform.system()
version = platform.release()

# This prints a blank line for looks
print("\n--- SYSTEM REPORT ---")

# We use 'f-strings' (the f before the quotes) to plug variables into text
print(f"Processor Architecture: {machine_type}")
print(f"Operating System: {os_name}")
print(f"OS Version: {version}")
print("---------------------\n")
