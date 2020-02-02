import subprocess
import sys
import os

def install_packages():
    """Fetches required modules for project in ./, then installs them
    """
    os.system('python -m pip install --upgrade pip')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pipreqs'])
    os.system('pipreqs --force ./') 
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    #os.remove("requirements.txt") 

install_packages()

input("\nAll required  modules installed.\nPress enter to contiue or close...")
