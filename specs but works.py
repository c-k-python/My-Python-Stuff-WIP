import psutil
import platform
import cpuinfo

def get_windows_version():
    try:
        version_info = platform.win32_ver()
        return f"Windows {version_info[0]} {version_info[1]} ({version_info[2]})"
    except Exception as e:
        print(f"Error getting Windows version: {e}")
        return "Unknown"

def get_cpu_temperature():
    try:
        # This part may vary based on your system and OS
        if platform.system() == "Linux":
            # Linux-specific code to get CPU temperature
            # This example assumes you have lm-sensors installed
            # You may need to install it using: sudo apt-get install lm-sensors
            import subprocess
            result = subprocess.check_output(['sensors'])
            temperature_lines = [line for line in result.decode().split('\n') if 'Core' in line]
            temperatures = [line.split('+')[1].split('°')[0].strip() for line in temperature_lines]
            return temperatures
        elif platform.system() == "Windows":
            # Windows-specific code to get CPU temperature using psutil
            cpu_info = cpuinfo.get_cpu_info()
            if 'Intel' in cpu_info['brand_raw']:
                # For Intel CPUs on Windows, try psutil
                cpu_temps = psutil.sensors_temperatures()
                if 'coretemp' in cpu_temps:
                    return [temp.current for temp in cpu_temps['coretemp']]
            elif 'AMD' in cpu_info['brand_raw']:
                # For AMD CPUs on Windows, try using psutil to get temperature
                # Note: This might not work for all AMD CPUs
                return [temp.current for temp in psutil.sensors_temperatures()['core']]

    except Exception as e:
        print(f"Error getting CPU temperature: {e}")
        return None

def print_computer_parts_and_temps():
    print("Computer Parts and Temperatures:")
    print("-------------------------------")

    # CPU temperature
    cpu_temps = get_cpu_temperature()
    if cpu_temps:
        print("CPU Temperatures:")
        for i, temp in enumerate(cpu_temps, start=1):
            print(f"Core {i}: {temp}°C")
        print("")

    # Other system information
    print("System Information:")
    print(f"OS: {get_windows_version()}")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print("")

if __name__ == "__main__":
    print_computer_parts_and_temps()

    # Add the following lines to wait for user input before exiting
    input("Press Enter to exit...")
