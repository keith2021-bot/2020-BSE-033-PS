
# SymptomTracker

SymptomTracker is a Python library for tracking and managing symptoms of patients in a healthcare setting.

## Installation on Windows

### 1. Install Python and pip

- Download Python: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for Windows. During installation, make sure to check the box that says "Add Python to PATH."

### 2. Set Up a Virtual Environment (Optional but Recommended)

Open a Command Prompt and navigate to the directory where you have the SymptomTracker code. Then, create a virtual environment:

On command Prompt (Click windows and type command prompt or cmd and run it)
`cd path\to\SymptomTracker
python -m venv venv`

#### Activate the virtual environment:
`venv\Scripts\activate`

### 3. Install SymptomTracker and Dependencies and run the tests
While in the virtual environment, install the SymptomTracker library and its dependencies and run the tests to ensure that the library is running correctly.
`pip install -e .`
`python -m unittest discover`

### Try to use the library and find out if it is working.

 "`from symptomtracker.tracker import SymptomTracker`

`tracker = SymptomTracker()` ..."
## Note 
-   Make sure to replace `path\to\SymptomTracker` with the actual path to the SymptomTracker directory.
-   If you're not using a virtual environment, you can skip steps 2 and 3 and directly install the library using `pip install -e .`.
-   Ensure that the Python executable and pip are in your system's PATH to run commands from any directory


This README.md file includes specific instructions for Windows users, taking into account the use of virtual environments and providing a clear guide on installing and running the SymptomTracker library on a Windows machine.

