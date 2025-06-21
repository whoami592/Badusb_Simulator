import keyboard
import time
import os

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║       BadUSB Firmware Simulator                      ║
    ║       Coded by Pakistani Ethical Hacker              ║
    ║       Mr Sabaz Ali Khan                             ║
    ║       For Educational Purposes Only                  ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)

def simulate_badusb_payload(payload):
    print("Simulating BadUSB payload execution...")
    print("WARNING: This will simulate keyboard input on your system.")
    print("Ensure you are running this in a controlled environment (e.g., VM).")
    confirm = input("Type 'yes' to proceed, any other key to cancel: ")
    if confirm.lower() != 'yes':
        print("Simulation cancelled.")
        return

    print("Starting payload simulation in 5 seconds...")
    time.sleep(5)  # Delay to allow user to prepare

    for command in payload:
        keyboard.write(command)  # Simulate typing the command
        time.sleep(0.1)  # Small delay between characters for reliability
        keyboard.press_and_release('enter')  # Simulate pressing Enter
        time.sleep(1)  # Delay between commands to mimic real BadUSB

    print("Payload simulation completed.")

def main():
    print_banner()
    print("This is a BadUSB firmware simulator designed for educational purposes.")
    print("It simulates keystroke injection as a USB Rubber Ducky would.")
    print("Use responsibly and only on systems you own or have permission to test.\n")

    # Example payload: Open a terminal and run a harmless command
    payload = [
        "cmd + t",  # Open terminal (macOS example, adjust for your OS)
        "whoami",   # Run a simple command
        "echo Hello from BadUSB Simulator!"
    ]

    # For Windows, you might use:
    # payload = [
    #     "win + r",  # Open Run dialog
    #     "cmd",      # Type cmd to open Command Prompt
    #     "whoami"    # Run a command
    # ]

    simulate_badusb_payload(payload)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure you have the 'keyboard' library installed and sufficient permissions.")