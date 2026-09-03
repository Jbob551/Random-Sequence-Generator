Random Sequence Generator

A lightweight Python application for generating randomized assignments and sequences for controlled experimental procedures.

Features

Random assignment between two options:

1 — Left

2 — Right

Equal probability for both options.

Automatic generation of 5 randomized blocks.

Each block contains the values 1, 2, 3, 4 exactly once.

Random order within each block.

Unique sequential session numbers.

Automatic recording of generated randomizations.

CSV data storage.

Simple graphical interface built with Tkinter.

Windows executable support through PyInstaller.

Interface

The application provides a simple interface with:

A button to reveal the randomly assigned option.

Five blocks displaying their randomized sequences.

A button to start a new session.

A button to open the folder containing the generated data.

The assignment and block sequences are generated when a new session starts.

Clicking the assignment button only reveals the result that was already generated. It does not perform a new randomization.

Randomization

For each session, the application generates:

Assignment

One value is randomly selected:

1 — Left
2 — Right

Both options have the same probability of being selected.

Blocks

Five independent blocks are generated.

Each block contains the four values:

1 2 3 4

exactly once, with their order randomly shuffled.

For example:

Block 1: 4 1 3 2
Block 2: 3 2 4 1
Block 3: 1 4 3 2
Block 4: 2 3 1 4
Block 5: 4 2 1 3

The order is independently randomized for each block.

Sessions

Each time a new session is created, a new randomization is generated.

Sessions are automatically numbered sequentially:

0001
0002
0003
...

The session number makes it possible to associate a generated randomization with a specific session.

Data Storage

The application automatically records each generated session in:

dados/randomizacao.csv

The CSV file contains:

Session
Date/Time
Assignment
Block 1
Block 2
Block 3
Block 4
Block 5

Example:

0001;2026-09-03 11:30:00;2;4-1-3-2;3-2-4-1;1-4-3-2;2-3-1-4;4-2-1-3

The file uses ; as the delimiter, which provides better compatibility with spreadsheet software configured for Brazilian Portuguese.

Requirements

To run the source code, you need:

Python 3

Tkinter

Tkinter is included with standard Python installations on Windows.

Running the Application

Clone the repository:

git clone https://github.com/Jbob551/random-sequence-generator.git

Enter the project directory:

cd random-sequence-generator

Run the application:

python Sorteador_Mestrado.py

Creating a Windows Executable

The project includes a batch script that uses PyInstaller to create a standalone Windows executable.

Run:

CRIAR_EXE.bat

The executable will be generated in:

dist/Sorteador_Mestrado.exe

The resulting .exe can be opened directly on Windows without VS Code or a Python installation.

Project Structure

random-sequence-generator/
│
├── Sorteador_Mestrado.py
├── CRIAR_EXE.bat
├── README.md
│
├── dados/
│   └── randomizacao.csv
│
└── dist/
    └── Sorteador_Mestrado.exe

Implementation

The application is written in Python and uses the standard random module for randomization.

Block generation is performed by creating a list containing the four values:

[1, 2, 3, 4]

and independently shuffling the list for each block.

This ensures that every block contains all four values exactly once while their order is randomized.

Reproducibility and Data Tracking

Each session stores the generated assignment, timestamp, and five block sequences in the CSV file.

This allows previously generated randomizations to be reviewed after the application has been used.

License

This project is licensed under the MIT License.

See the LICENSE file for details.
