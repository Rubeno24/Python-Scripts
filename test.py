import subprocess
import os

def open_vscode(folder_path):
    vscode_path = r"C:\Users\Ruben Ortega\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    
    try:
        subprocess.Popen([vscode_path, folder_path])
    except Exception as e:
        print(f"Error opening Visual Studio Code: {e}")

if __name__ == "__main__":
    folder_to_open = r"C:\Users\Ruben Ortega\OneDrive - California State University, Sacramento\Desktop\Leetcode"  # Replace with the actual path
    open_vscode(folder_to_open)

