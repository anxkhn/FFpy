import subprocess
import time
import sys

SCRIPT_VERSION = "1.1.0"

def run_script(script_filename, time_unit='ms', num_runs=1):
    total_execution_time = 0

    for _ in range(num_runs):
        start_time = time.time()
        subprocess.run(['python', script_filename])
        end_time = time.time()

        if time_unit == 'ms':
            execution_time = (end_time - start_time) * 1000
        else:
            execution_time = end_time - start_time

        total_execution_time += execution_time

    if num_runs == 1:
        print(f"Execution time: {total_execution_time:.4f} {time_unit}")
    else:
        average_execution_time = total_execution_time / num_runs
        print(f"Average execution time ({num_runs} runs): {average_execution_time:.4f} {time_unit}")

def display_help():
    print("Usage: ffpy <script_filename> [-ms | -s] [-n <num_runs>]")
    print("Options:")
    print("  -ms          Measure time in milliseconds (default)")
    print("  -s           Measure time in seconds")
    print("  -n <num_runs> Number of runs (default is 1)")
    print("  --help       Display this help message")
    print("  --version    Display script version")
    sys.exit(0)

def display_version():
    print(f"ffpy v{SCRIPT_VERSION}")
    sys.exit(0)

def main():
    if len(sys.argv) < 2 or '--help' in sys.argv:
        display_help()
    elif '--version' in sys.argv:
        display_version()
    else:
        script_filename = sys.argv[1]

        if '-s' not in sys.argv[2:]:
            time_unit = 'ms'
        else:
            time_unit = 's'

        num_runs_index = (
            sys.argv.index('-n') + 1
            if '-n' in sys.argv and sys.argv.index('-n') + 1 < len(sys.argv)
            else None
        )
        if num_runs_index is not None:
            num_runs = int(sys.argv[num_runs_index])
        else:
            num_runs = 1

        run_script(script_filename, time_unit, num_runs)

if __name__ == "__main__":
    main()
