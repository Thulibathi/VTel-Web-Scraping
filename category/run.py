import subprocess
import os
import openpyxl
import re
import csv
import io

def run_python_scripts_and_save_to_excel(script_paths, output_folder="results"):
    """
    Runs multiple Python scripts in the command prompt and saves their output to individual Excel sheets.

    Args:
        script_paths (list): A list of paths to the Python scripts.
        output_folder (str): The folder where the Excel files will be saved.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for script_path in script_paths:
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        excel_file_path = os.path.join(output_folder, f"{script_name}.xlsx")

        try:
            process = subprocess.Popen(
                ["python", script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  # Ensure output is text
            )
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                print(f"Script '{script_name}' executed successfully.")
                save_output_to_excel(stdout, excel_file_path)
                print(f"Output saved to: {excel_file_path}")
            else:
                print(f"Error executing script '{script_name}':")
                print(stderr)

        except FileNotFoundError:
            print(f"Error: Python script '{script_path}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred while running '{script_name}': {e}")

def save_output_to_excel(output, excel_file_path):
    """
    Saves the output from a Python script to an Excel file.

    Args:
        output (str): The output from the script.
        excel_file_path (str): The path to the Excel file.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    lines = output.splitlines()
    for row_index, line in enumerate(lines, start=1):
        cells = line.split("\t") #if your data is tab seperated, otherwise split by comma or spaces
        for col_index, cell_value in enumerate(cells, start=1):
            sheet.cell(row=row_index, column=col_index, value=cell_value)

    workbook.save(excel_file_path)

# Example usage:
script_paths = ["category/cables.py", "category/cctv_camera.py", "category/desktop.py","category/flash_drive.py", 
                "category/hard_drives.py", "category/headset.py"]#"category/ink_cartridges.py", "category/keyboard.py",
                #"category/memory.py", "category/micro_sd_card.py", "category/monitor.py", "category/mouse.py",
                #"category/note_book.py", "category/power_supply.py", "category/printer.py","category/router.py",
                #"category/software.py", "category/ssd.py","category/uncategorized.py", "category/ups.py"]  # Replace with your script paths
run_python_scripts_and_save_to_excel(script_paths)