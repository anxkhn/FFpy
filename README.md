# FFpy - ⚡ Fast Python Script Execution Timer

FFpy is a command-line tool that measures the execution time of Python scripts. It provides flexibility by allowing you to specify the time unit (milliseconds or seconds) and the number of runs for more accurate measurements.

## Background 🚀

As an undergraduate software engineer with Python as my weapon of choice for coding, I often found myself curious about the execution time of my scripts. While solutions like `timeit` module exist, I wanted a seamless way to measure execution time without adding another line of code to my programs. This led to the creation of FFpy. 

In my coding journey, especially while tackling Data Structures and Algorithms problems and optimizing code, understanding the execution time can provide valuable insights. 

FFpy aims to be a simple yet powerful tool for easily benchmarking performance without the need to modify your existing codebase. I believe in keeping things straightforward. FFpy is designed to be a minimalistic, no-nonsense module that integrates seamlessly into your workflow, allowing you to focus on coding while effortlessly obtaining execution time metrics.

## Installation 🛠️

Install FFpy using `pip`:

```bash
pip install ffpy
```

Alternatively, you can clone this repository:

```bash
git clone https://github.com/anxkhn/FFpy.git
cd FFpy
pip install .
```

## Usage 🚨

After installation, you can use FFpy to measure the execution time of your Python scripts. Here's the basic syntax:

```bash
ffpy <filename.py> <filename2.py> [-u <unit>] [-n <num_runs>] [-s] [-v] [-h]
```

- `<filename.py>`: Replace with the actual filename of your Python script in the current directory.
- `<filename2.py>`: Optional second script for comparison.
- `-u, --unit`: Optional flag to specify the time unit (ms or s, default is ms).
- `-n, --number`: Optional flag to specify the number of runs (default is 1).
- `-s, --silent`: Optional flag to run the script silently (suppress output).
- `-v, --version`: Display script version.
- `-h, --help`: Display help message.

### Examples 🌈

1. Measure the execution time of a script in milliseconds:

```bash
ffpy script.py
```

2. Measure the execution time in seconds:

```bash
ffpy script.py -u s
```

3. Run the script 10 times and measure the average execution time:

```bash
ffpy script.py -n 10
```

4. Run the script silently:

```bash
ffpy script.py -s
```

5. Compare the execution times of two scripts:

```bash
ffpy bubble_sort.py merge_sort.py
```

### Hello? 🤔

Let's include a simple "Hello FFpy" `hello.py` Python script as an example:

```python
print("Hello, FFpy!")
```

You can measure its execution time using FFpy:

```bash
ffpy hello.py
```

This should output:

```
Hello, FFpy!
Execution time: XX.XX ms
```

## Contributing 🤝

If you'd like to contribute to FFpy, feel free to fork the repository and submit a pull request.

## License 📜

This project is licensed under the GPLv3 License - check out [this website](https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3) for more information.