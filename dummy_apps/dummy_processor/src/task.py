import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dummy processor')
    parser.add_argument('sec', type=int,
                        help='Number of seconds to sleep')

    args = parser.parse_args()
    sleep_time = int(args.sec)
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
    print("Finished")
