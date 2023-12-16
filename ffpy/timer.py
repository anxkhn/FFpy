import subprocess
import time
import sys

SCRIPT_VERSION = "1.3.0"


def run_script(script_filename, time_unit="ms", num_runs=1, silent=False):
    total_execution_time = 0

    for _ in range(num_runs):
        start_time = time.time()

        if not silent:
            subprocess.run(["python", script_filename])
        else:
            subprocess.run(
                ["python", script_filename],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        end_time = time.time()

        if time_unit == "ms":
            execution_time = (end_time - start_time) * 1000
        elif time_unit == "s":
            execution_time = end_time - start_time
        else:
            print("Invalid time unit: {}".format(time_unit))
            sys.exit(1)

        total_execution_time += execution_time

    if num_runs == 1:
        print("Execution time: {:.4f} {}".format(total_execution_time, time_unit))
    else:
        average_execution_time = total_execution_time / num_runs
        print(
            "Average execution time ({} runs): {:.4f} {}".format(
                num_runs, average_execution_time, time_unit
            )
        )


def display_help():
    print(
        "Usage: {} <script_filename_1> [script_filename_2] [-u <unit>] [-n <number>] [-s] [-V] [-H]".format(
            sys.argv[0]
        )
    )
    print("Options:")
    print("  -u, --unit    Specify time unit (ms or s, default is ms)")
    print("  -n, --number  Number of runs (default is 1)")
    print("  -s, --silent  Run script silently (suppress output)")
    print("  -V, --ver Display script version")
    print("  -H, --help    Display this help message")
    sys.exit(0)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-H", "--help"):
        display_help()

    script_filename_1 = sys.argv[1]
    script_filename_2 = None
    time_unit = "ms"
    num_runs = 1
    silent = False

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] in ("-u", "--unit"):
            time_unit = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] in ("-n", "--number"):
            num_runs = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] in ("-s", "--silent"):
            silent = True
            i += 1
        elif sys.argv[i] in ("-V", "--ver"):
            print("{} {}".format(sys.argv[0], SCRIPT_VERSION))
            sys.exit(0)
        else:
            if script_filename_2 is None:
                script_filename_2 = sys.argv[i]
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)

            i += 1

    print(script_filename_1)
    run_script(script_filename_1, time_unit, num_runs, silent)

    if script_filename_2:
        print(script_filename_2)
        run_script(script_filename_2, time_unit, num_runs, silent)


if __name__ == "__main__":
    main()
