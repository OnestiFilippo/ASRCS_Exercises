import argparse
import os
import sys
import time
import shutil

def archive(path, seconds):
    if os.path.isdir(path):
        for file in os.listdir(path):
            path_file = os.path.join(path, file)
            if os.path.isfile(path_file) and not os.path.isdir(path_file):
                file_mtime = os.path.getmtime(path_file)
                now = time.time()
                
                diff = now - file_mtime
                if diff >= seconds:
                    print(f"Archivio {path_file} che non viene modificato da {int(diff)} s")
                    #shutil.move(path_file, os.path.expanduser("~/archive"))
            else:
                archive(path_file, seconds)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=True)
    parser.add_argument('--seconds', type=int, required=True)
    args = parser.parse_args()
    
    path = args.path
    seconds = args.seconds
    
    if not os.path.isabs(path):
        print("Path non assoluto", file=stderr)
        sys.exit(1)
    if not os.path.exists(path):
        print("Path non esiste", file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(path):
        print("Path non è una directory", file=sys.stderr)
        sys.exit(1)
        
    if seconds <= 0:
        print("Seconds < 0", file=sys.stderr)
        sys.exit(1)
        
    if not os.path.exists(os.path.expanduser("~/archive")):
        print("Cartella archive non esistente. La creo")
        os.makedirs(os.path.expanduser("~/archive"))
        
    archive(path, seconds)
    
    pass

if __name__ == "__main__":
    main()
