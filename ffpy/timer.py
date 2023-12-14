import subprocess
import time
import sys

def run_script(script_filename, time_unit='ms', num_runs=1):
    total_execution_time = 0

    for _ in range(num_runs):
        start_time = time.time()
        subprocess.run(['python', script_filename])
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000 if time_unit == 'ms' else end_time - start_time
        total_execution_time += execution_time

    average_execution_time = total_execution_time / num_runs if num_runs > 0 else 0
    print(f"Average execution time ({num_runs} runs): {average_execution_time:.4f} {time_unit}")

def main():
    if len(sys.argv) < 2:
        print("Usage: ffpy <script_filename> [-ms | -s] [-n <num_runs>]")
        sys.exit(1)

    script_filename = sys.argv[1]
    time_unit = 'ms' if '-s' not in sys.argv[2:] else 's'
    num_runs_index = sys.argv.index('-n') + 1 if '-n' in sys.argv else None
    num_runs = int(sys.argv[num_runs_index]) if num_runs_index is not None and num_runs_index < len(sys.argv) else 1

    run_script(script_filename, time_unit, num_runs)

if __name__ == "__main__":
    main()
