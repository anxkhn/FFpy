from setuptools import setup, find_packages

setup(
    name='FFpy',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ffpy = ffpy.timer:main',
        ],
    },
    description='Fast Python Script Execution Timer',
    long_description="""
============
FFpy
============

FFpy is a command-line tool that measures the execution time of Python scripts. It provides flexibility by allowing you to specify the time unit (milliseconds or seconds) and the number of runs for more accurate measurements.

Installation
------------

Install FFpy using `pip`::

    pip install ffpy

Alternatively, you can clone this repository::

    git clone https://github.com/anxkhn/FFpy.git
    cd FFpy
    pip install .

Usage
-----

After installation, you can use FFpy to measure the execution time of your Python scripts. Here's the basic syntax::

    ffpy <script_filename> [-ms | -s] [-n <num_runs>]

- `<script_filename>`: Replace with the actual filename of your Python script.
- `-ms` or `-s`: Optional flag to specify the time unit (milliseconds or seconds, default is milliseconds).
- `-n <num_runs>`: Optional flag to specify the number of runs (default is 1).

Examples
~~~~~~~~

1. Measure the execution time of a script in milliseconds::

    ffpy my_script.py

2. Measure the execution time in seconds::

    ffpy my_script.py -s

3. Run the script 10 times and measure the average execution time::

    ffpy my_script.py -n 10

Contributing
------------

If you'd like to contribute to FFpy, feel free to fork the repository and submit a pull request.

License
-------

This project is licensed under the `GPLv3 License <https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3>`_ - check out `this website <https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3>`_ for more information.
""",
    long_description_content_type='text/x-rst',
    author='Anas Khan',
)
