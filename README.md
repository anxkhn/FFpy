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
ffpy <filename.py> [-ms | -s] [-n <num_runs>]
```

- `<filename.py>`: Replace with the actual filename of your Python script in the current directory.
- `-ms` or `-s`: Optional flag to specify the time unit (milliseconds or seconds, default is milliseconds).
- `-n <num_runs>`: Optional flag to specify the number of runs (default is 1).

### Examples 🌈

1. Measure the execution time of a script in milliseconds:

```bash
ffpy script.py
```

2. Measure the execution time in seconds:

```bash
ffpy script.py -s
```

3. Run the script 10 times and measure the average execution time:

```bash
ffpy script.py -n 10
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
Execution time: XX.XX milliseconds
```

## Contributing 🤝

If you'd like to contribute to FFpy, feel free to fork the repository and submit a pull request.

## License 📜

This project is licensed under the GPLv3 License - check out [this website](https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3) for more information.