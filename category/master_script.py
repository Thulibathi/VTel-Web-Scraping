# master_script.py
import subprocess

def run_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
        print(f"Script '{script_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{script_path}': {e}")
    except FileNotFoundError:
        print(f"Error: Python executable not found.")
    except Exception as general_error:
        print(f"An unexpected error occured: {general_error}")

# List of scripts to run
scripts_to_run = ["category/cables.py", "category/cctv_camera.py", "category/desktop.py","category/flash_drive.py", 
                "category/hard_drives.py", "category/headset.py","category/ink_cartridges.py", "category/keyboard.py",
                "category/memory.py", "category/micro_sd_card.py", "category/monitor.py", "category/mouse.py",
                "category/note_book.py", "category/power_supply.py", "category/printer.py","category/router.py",
                "category/software.py", "category/ssd.py","category/uncategorized.py", "category/ups.py"]

for script in scripts_to_run:
    run_script(script)