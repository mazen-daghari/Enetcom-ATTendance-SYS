import subprocess
import winsound



def run_main_script():
    while True:
        try:
            # Run the main.py script
            subprocess.run(["python", "main.py"], check=True)
        except subprocess.CalledProcessError as e:
            # Handle the error (e.g., log it, notify, etc.)
            print(f"Error occurred: {e}")

        winsound.PlaySound("alarm.wav", 0)

if __name__ == "__main__":
    run_main_script()
