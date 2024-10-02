# DHIS2 Data Transformation Scripts

A set of scripts that help transform and extracted DHIS2 JSON data from the DHIS2 API and convert to CSV if necessary.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [1. Install Python 3](#1-install-python-3)
  - [2. Create a Python Virtual Environment](#2-create-a-python-virtual-environment)
  - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
  - [4. Install Required Packages](#4-install-required-packages)
- [Usage](#usage)
  - [1. Run your prefered Conversion Scripts](#1-run-the-conversion-script)
  - [2. Output](#2-output)
- [Script Details](#script-details)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** Windows, macOS, or Linux
- **Python:** Version 3.6 or higher
- **Internet Connection:** Required to download dependencies
- **Basic Command-Line Knowledge:** Familiarity with terminal or command prompt operations

---

## Setup

Follow these steps to set up your environment and prepare the script for use.

## 1. Install Python 3

### Ensure Python 3 is installed on your system.

- **Check if Python is Installed:**

  Open your terminal or command prompt and run:

```bash
  python3 --version
```

If python is installed, you will see an output like:

```bash
Python 3.x.x
```

- Download and install Python
  If Python is not installed, download it from the [official website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

## 2. Create a Python Virtual Environment

Creating a virtual environment isolates your project's dependencies from other Python projects on your system.

### Clone the project from GitHub

```bash
git clone https://github.com/0xafrogeek/dhis2-json-to-csv
```

### Navigate to the clone project

```bash
cd /path/to/dhis2-json-to-csv
```

### Create the Python Virtual Environment

The following command creates a virtual environment names `venv`:

```bash
python3 -m venv venv
```

## 3. Activate the Virtual Environment

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

After successful activation, your terminal should be prefixed with `(venv)`

## 4. Install Required Packages

Run the following command to install the packages listed in `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

---

## Usage

## 1. Set the Correct JSON File Path

Open any of the scripts you intend to use and replace `"/path/to/your/CBS-Enrollments.json"` with the actual path to your JSON file.

```bash
json_file_path = "/path/to/your/CBS-Enrollments.json"
```

## 2. Run the script

```bash
python3 enrollments_json_csv.py
```

## Output

Upon successful execution, the script will:

- Parse the JSON file, handling both single and double-escaped JSON.
- Display debugging information in the terminal to trace the parsing process.
- Create a CSV file named `CBS-Enrollments.csv` in the project directory containing the enrollment data.
