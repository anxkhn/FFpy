from setuptools import setup, find_packages

setup(
    name="FFpy",
    version="1.6.1",
    packages=find_packages(),
    install_requires=[
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "ffpy = ffpy.timer:main",
        ],
    },
    description="Fast Python Script Execution Timer",
    long_description="""
FFpy - ⚡ Fast Python Script Execution Timer
============================================

FFpy is a command-line tool that measures the execution time of Python
scripts. It provides flexibility by allowing you to specify the time
unit (milliseconds or seconds) and the number of runs for more accurate
measurements.

Background 🚀
-------------

As an undergraduate software engineer with Python as my weapon of choice
for coding, I often found myself curious about the execution time of my
scripts. While solutions like ``timeit`` module exist, I wanted a
seamless way to measure execution time without adding another line of
code to my programs. This led to the creation of FFpy.

In my coding journey, especially while tackling Data Structures and
Algorithms problems and optimizing code, understanding the execution
time can provide valuable insights.

FFpy aims to be a simple yet powerful tool for easily benchmarking
performance without the need to modify your existing codebase. I believe
in keeping things straightforward. FFpy is designed to be a
minimalistic, no-nonsense module that integrates seamlessly into your
workflow, allowing you to focus on coding while effortlessly obtaining
execution time metrics.

Installation 🛠️
---------------

Install FFpy using ``pip``:

.. code:: bash

   pip install ffpy

Alternatively, you can clone this repository:

.. code:: bash

   git clone https://github.com/anxkhn/FFpy.git
   cd FFpy
   pip install .

Usage 🚨
--------

After installation, you can use FFpy to measure the execution time of
your Python scripts. Here’s the basic syntax:

.. code:: bash

   ffpy <filename.py/folder> <filename2.py> [-u <unit>] [-n <num_runs>] [-s] [-m <mode>] [-v] [-h]

-  ``<filename.py/folder>``: Replace with the actual filename or folder of your Python script(s) in the current directory.

-  ``<filename2.py>``: Optional second script for comparison.

-  ``-u, --unit``: Optional flag to specify the time unit (ms or s,
   default is ms).

-  ``-n, --number``: Optional flag to specify the number of runs
   (default is 1).

-  ``-s, --silent``: Optional flag to run the script silently (suppress
   output).

-  ``-m, --mode``: Optional flag to specify the threads (single or
   multi, default is single).

-  ``-v, --version``: Display script version.

-  ``-h, --help``: Display help message.

Examples 🌈
~~~~~~~~~~~

1. Measure the execution time of a script in milliseconds:

.. code:: bash

   ffpy script.py

2. Measure the execution time in seconds:

.. code:: bash

   ffpy script.py -u s

3. Run the script 10 times and measure the average execution time:

.. code:: bash

   ffpy script.py -n 10

4. Run the script silently:

.. code:: bash

   ffpy script.py -s

5. Run scripts concurrently using multithreading mode:

.. code:: bash

   ffpy script.py -m multi

**Note on Multithreading Mode:**

When using the multithreading mode (``-m multi``), the script will be
executed concurrently in a multithreaded fashion, leveraging multiple
cores on your system. It’s important to note that the average execution
time in multithreading mode may not be equal to running the program
once, as multithreading introduces parallelism and can lead to
variations in execution times. `Learn more [1] about
multithreading. <https://github.com/anxkhn/FFpy/blob/main/learn_more.md#1-learn-more-about-multithreading-and-how-it-works>`__

Types of Operation:
-------------------

-  **Single File:** Measure the execution time of a single script.

.. code:: bash

   ffpy script1.py -s

Output:

.. code:: bash

   Execution time: 30.1924 ms

-  **Double File (Comparison):** Compare the execution times of two
   scripts and determine the percentage difference.

2. Compare the execution times of two scripts:

.. code:: bash

   ffpy script1.py script2.py -s

Output:

.. code:: bash

   script1.py
   Execution time: 29.2735 ms
   script2.py
   Execution time: 533.9346 ms
   script1.py is 1723.95% faster than script2.py

-  **More Than Two Files (Detailed Table):** Compare execution times of
   multiple scripts and display a detailed table with filenames and
   average execution times.

3. Compare execution times of multiple scripts and display a detailed
   table:

.. code:: bash

   ffpy script1.py script2.py script3.py -s

or

.. code:: bash

   ffpy path/to/scripts

Output:

.. code:: bash

   script1.py
   Execution time: 30.0028 ms
   script2.py
   Execution time: 533.4799 ms
   script3.py
   Execution time: 1035.9304 ms
   ╒════════════╤═══════════════════════════════╕
   │ Filename   │   Average Execution Time (ms) │
   ╞════════════╪═══════════════════════════════╡
   │ script1.py │                       30.0028 │
   ├────────────┼───────────────────────────────┤
   │ script2.py │                      533.48   │
   ├────────────┼───────────────────────────────┤
   │ script3.py │                     1035.93   │
   ╘════════════╧═══════════════════════════════╛

How to Use 🤔
~~~~~~~~~~~~~

1. Start by including a simple ``hello.py`` Python script as an example:

.. code:: python

   print("Hello, FFpy!")

You can measure its execution time using FFpy:

.. code:: bash

   ffpy hello.py

This should yield the following output:

::

   Hello, FFpy!
   Execution time: XX.XX ms

2. Now, let’s examine the runtime of two different sorting algorithms.
   We have a list of 1000 integers, and we’ll use ``merge_sort.py`` and
   ``bubble_sort.py`` to sort them as examples:

.. code:: bash

   ffpy merge_sort.py bubble_sort.py --silent

This will produce the following output:

::

   merge_sort.py
   Execution time: 33.2839 ms
   bubble_sort.py
   Execution time: 65.3996 ms
   merge_sort.py is 96.49% faster than bubble_sort.py.

This difference in execution time is due to the fact that Merge sort is
faster than bubble sort, thanks to its efficient divide-and-conquer
approach, resulting in a time complexity of O(n log n). On the other
hand, bubble sort, with its quadratic time complexity of O(n^2), proves
to be less efficient for large datasets. We can clearly see the
execution time differences between two programs. `Learn more [2] about
time
complexity. <https://github.com/anxkhn/FFpy/blob/main/learn_more.md#2-learn-more-about-sorting-algorithms-their-time-complexity-and-efficiency>`__

Contributing 🤝
---------------

If you’d like to contribute to FFpy, feel free to fork the repository
and submit a pull request.

License 📜
----------

This project is licensed under the GPLv3 License - check out `this
website <https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3>`__
for more information.

""",
    long_description_content_type="text/x-rst",
    author="Anas Khan",
    author_email="anxkhn28@gmail.com",
    url="https://github.com/anxkhn/FFpy",
    license="GPL-3",
)
