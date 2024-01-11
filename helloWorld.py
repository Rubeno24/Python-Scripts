import webbrowser
import subprocess

def open_browser(url):
    webbrowser.open(url)

# This code block will only run if the script is executed directly

def open_program(program_path):
    try:
        subprocess.Popen(program_path, shell=True)
    except Exception as e:
        print(f"Error opening the program: {e}")

if __name__ == "__main__":
    # Specify the URL you want to open
    url_to_open = "https://github.com/"

    # Open the web browser
    open_browser(url_to_open)

    # Specify the program path you want to open
    program_path_to_open = vscode_path = r"C:\Users\Ruben Ortega\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    




    # Open the program
    open_program(program_path_to_open)
