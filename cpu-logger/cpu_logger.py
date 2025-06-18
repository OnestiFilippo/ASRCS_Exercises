import psutil
import argparse
import sys

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(prog='CPU Logger')
        parser.add_argument('-i', '--interval', type=int, required=True)
        args = parser.parse_args()

        while True:
            print(str(psutil.cpu_percent(interval=args.interval)) + " %")

    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
