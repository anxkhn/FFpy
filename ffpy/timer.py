#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
from tabulate import tabulate

SCRIPT_VERSION = "1.6.0"


def execute_python(script_filename, silent):
    if not silent:
        subprocess.run([sys.executable, script_filename])
    else:
        subprocess.run(
            [sys.executable, script_filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


def run_script(script_filename, mode, time_unit="ms", num_runs=1, silent=False):
    if mode == "multi":
        print("multi")
        start_time = time.time()
        with ThreadPoolExecutor() as executor:
            executor.map(
                lambda _: execute_python(script_filename, silent), range(num_runs)
            )
        end_time = time.time()
        execution_time = end_time - start_time
    else:
        start_time = time.time()
        for _ in range(num_runs):
            execute_python(script_filename, silent)
        end_time = time.time()
        execution_time = end_time - start_time

    if time_unit == "ms":
        execution_time = execution_time * 1000
    elif time_unit == "s":
        pass
    else:
        print("Invalid time unit: {}".format(time_unit))
        sys.exit(1)

    if num_runs == 1:
        print("Execution time: {:.4f} {}".format(execution_time, time_unit))
    else:
        average_execution_time = execution_time / num_runs
        print(
            "Average execution time ({} runs): {:.4f} {}".format(
                num_runs, average_execution_time, time_unit
            )
        )

    return execution_time


def list_files(folder_path):
    script_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".py") and os.path.isfile(os.path.join(folder_path, f))
    ]
    return script_files


def display_help():
    print(
        "Usage: {} <filename/folder> [filename_2] [...] [-u <unit>] [-n <number>] [-s] [-m <mode>] [-V] [-H]".format(
            sys.argv[0]
        )
    )
    print("Options:")
    print("  -u, --unit    Specify time unit (ms or s, default is ms)")
    print("  -n, --number  Number of runs (default is 1)")
    print("  -s, --silent  Run script silently (suppress output)")
    print("  -m, --mode    Execution mode (single or multi, default is single)")
    print("  -V, --ver Display script version")
    print("  -H, --help    Display this help message")
    sys.exit(0)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-H", "--help"):
        display_help()

    script_filenames = []
    time_unit = "ms"
    num_runs = 1
    silent = False
    mode = "single"

    i = 1
    while i < len(sys.argv):
        if sys.argv[i].startswith("-"):
            if sys.argv[i] in ("-u", "--unit"):
                time_unit = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] in ("-n", "--number"):
                num_runs = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] in ("-s", "--silent"):
                silent = True
                i += 1
            elif sys.argv[i] in ("-m", "--mode"):
                mode = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] in ("-V", "--ver"):
                print("{} {}".format(sys.argv[0], SCRIPT_VERSION))
                sys.exit(0)
            else:
                print("Invalid option: {}".format(sys.argv[i]))
                sys.exit(1)
        else:
            script_input = sys.argv[i]

            if os.path.isdir(script_input):
                script_filenames.extend(list_files(script_input))
            else:
                script_filenames.append(script_input)

            i += 1

    if len(script_filenames) > 2:
        table_data = []
        for script_filename in script_filenames:
            print(script_filename)
            execution_time = run_script(
                script_filename, mode, time_unit, num_runs, silent
            )
            table_data.append([script_filename, execution_time / num_runs])

        sorted_table = sorted(table_data, key=lambda x: x[1])
        headers = ["Filename", "Average Execution Time ({})".format(time_unit)]
        print(tabulate(sorted_table, headers, tablefmt="fancy_grid"))

    elif len(script_filenames) == 2:
        print(script_filenames[0])
        time_file_1 = run_script(script_filenames[0], mode, time_unit, num_runs, silent)
        print(script_filenames[1])
        time_file_2 = run_script(script_filenames[1], mode, time_unit, num_runs, silent)
        percentage_difference = ((time_file_2 - time_file_1) / time_file_1) * 100

        if percentage_difference > 5:
            print(
                "{} is {:.2f}% faster than {}".format(
                    script_filenames[0], abs(percentage_difference), script_filenames[1]
                )
            )
        elif percentage_difference < -5:
            print(
                "{} is {:.2f}% slower than {}".format(
                    script_filenames[0], abs(percentage_difference), script_filenames[1]
                )
            )
        else:
            print(
                "{} and {} have almost the same execution time.".format(
                    script_filenames[0], script_filenames[1]
                )
            )

    else:
        run_script(script_filenames[0], mode, time_unit, num_runs, silent)


if __name__ == "__main__":
    main()