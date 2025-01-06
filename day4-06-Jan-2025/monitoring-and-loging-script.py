#Monitoring and loging
# if psutil library is not available or installed the use "pip install psutil" command to install psutil
import psutil
cpu_percent = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()

print(f'CPU Usage: {cpu_percent}') # Using f-string with placeholder and variable
print(f'Memory Usage: {memory_info}') # Using f-string with placeholder and variable