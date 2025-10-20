# Digital-Assistant-Project
This repository contains the implementation of a **modular digital assistant (DA)** developed as part of a **Master’s thesis** in Computer Science and Computer Engineering from ISEL.  
The assistant is built in **Python** and optimized for the **Windows desktop environment**, providing both **text** and **voice-based** interaction.  
It integrates **Large Language Models (LLMs)** to interpret user requests and dynamically choose between conversational responses and function execution — for example, retrieving weather data or launching applications.

---
## Project Overview

The system follows a **layered and modular architecture**, composed of:

- **Presentation Layer** – A responsive PyQt5 GUI supporting text and voice input/output.  
- **Core Layer** – The central reasoning engine that coordinates user input and backend logic.  
- **Module Layer** – Extensible modules that provide functionalities such as weather updates, OS automation, and speech processing.

This architecture ensures **modularity, extensibility, and maintainability**, allowing new modules to be added without altering the core.

---

## Questionnaire for Usability Testing

If you are participating in the **usability questionnaire**, please read this section carefully:
- The questionnaire will indicate the steps you need to execute while installing the Digital Assistant and testing it.  
- You do **not** need to modify or add any additional features — everything required for testing is already included.

---

## Installation Guide

### Install Python and pip

The assistant requires **Python 3.10.11** and **pip** (Python's package manager).

1. Download Python 3.10.11 from the [official Python website](https://www.python.org/downloads/release/python-31011/) and download the Windows installer (64 or 32-bit) under the Files section.
2. During installation, **check the box "Add Python to PATH"** - this is essential for enabling the python command in any location of the system.
3. After installation, open a terminal (Command Prompt or PowerShell) and type:
```bash
python --version
pip --version
```
Both commands should display a version number. If they don't, restart your computer and ensure that Python was added to the PATH.

### Download or Clone the Project

You can either:
- Download the ZIP file from the GitHub repository (by clicking the green Code button and selecting the Download ZIP option) and extract it,

    **or**
- Clone the repository using git:
```bash
git clone https://github.com/pataponjak3/Digital-Assistant-Project.git
cd Digital-Assistant-Project
```

### Create a Virtual Environment

A virtual environment isolates the dependencies of the project, the following command should be executed on the project's root folder (you can do this by being in the project's root folder, clicking the folder's path and writting `cmd`):

```bash
python -m venv venv
```
> 💡 **Tip:** To open a command window in the project folder:
> 1. Open the folder where you extracted or cloned the project
> 2. Click on the folder path bar at the top of File Explorer
> 3. Type `cmd` and press **Enter**.
>
> With this, a terminal will open directly in that folder

<figure align=center>
    <img src="https://github.com/user-attachments/assets/fe53e1b9-2e35-45fa-8533-745f9c1e7405" alt="Showing folder path" width="600"/>
    <figcaption>Showing folder path</figcaption>
</figure>
<figure align=center>
  <img src="https://github.com/user-attachments/assets/5e1798ff-af38-447c-bb8d-45aa7678a6cf" alt="Writting `cmd`" width="600"/>
  <figcaption>Writting "cmd"</figcaption>
</figure>

Then activate it:
```bash
venv\Scripts\activate
```
Once activated, your terminal prompt should start with `(venv)`, it's in this mode that you'll install the dependencies and start the assistant.

### Install Dependencies
Use pip to install all the required Python libraries:
```bash
pip install -r requirements.txt
```
If you see any warnings, they can usually be ignored unless the installation fails.

### Set Up Environment Variables

The assistant requires a few environment variables to function correctly.
1. Create a file named `.env` in the **root folder** of the project
    * This is a file without a name with the extension `.env`, to create such files, ensure that you can see file name extensions. This is possible by enabling the option by the same name on the File Explorer, under the View tab (on Windows 11, after clicking the View tab, you must also select the option Show).
2. Add the following content:
```env
PYTHONPATH=src
OPENWEATHERMAP_KEY=your_api_key_here
AWANLLM_KEY=your_api_key_here
GEMINI_KEY=your_api_key_here
GORILLA_KEY=EMPTY
HUGGINGFACE_KEY=your_api_key_here
```
* `PYTHONPATH` - Ensures that Python can locate the source files inside the src directory. This must always be set to src.
* `OPERNWEATHERMAP_KEY` - API key for [OpenWeatherMap](https://openweathermap.org/), used by the assistant to retrieve real-time weather data and air pollution information.
* `AWANLLM_KEY` - API key for accessing the [Awan LLM provider](https://www.awanllm.com/), one of the supported backends for large language model interactions.
* `GEMINI_KEY` - API key for [Google Gemini](https://aistudio.google.com/apikey), another supported LLM provider used for text understanding and reasoning.
* `GORILLA_KEY` - This key is kept for consistency, but the *Gorilla OpenFunctions v1* from the [University of California, Berkeley](https://gorilla.cs.berkeley.edu/) does **not require an API key**, as it is an open-access project. Leave this set to `EMPTY`.
* `HUGGINGFACE_KEY` - API key for [Hugging Face Inference API](https://huggingface.co/), used to access models such as *Llama 3.1 8B Instruct*.

> **For questionnaire participants:**
> You will only require to have the OpenWeatherMap and HuggingFace API key, which will be given/explained how to get on the next page of the questionnaire.
> Keep the remaining keys set as `EMPTY` or leave them unchanged

### Run the Digital Assistant

After creating the `.env` file, start the assistant by running:
```bash
python -m src.main
```
The graphical interface will open in a fixed **800x600** window.
You can then communicate with the assistant using text or voice, depending on your preference
> **For questionnaire participants:**
> After starting the Digital Assistant, please proceed with the tasks on the questionnaire

### (Optional) Deactivate the Virtual Environment

When you finish testing or developing, deactivate the virtual environment:
```bash
deactivate
```

---

## Testing the Digital Assitant

The Digital Assitant has a suit of test cases present in the test folder, under the `test_performance.py` file. These tests were implemented via `pytest`, and it's advised to also have the command added in the `PATH` environment variable. To run a single test, providing a log of the testing, run the following command on the project's root folder:

```bash
pytest tests/test_performance.py::test_to_execute --log-file=tests/logs/log_name.log --log-file-level=DEBUG -v
```