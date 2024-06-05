import sys
from gui.gui_main import gui
import time

def main():
    try:
        gui()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(50)
    

if __name__ == "__main__":
    main()
