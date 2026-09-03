# Random Sequence Generator

A lightweight Python application for generating randomized assignments and sequences for controlled experimental procedures.

## Features

- Random assignment between two options: `1` and `2`
- Equal probability for both assignment options
- Automatic generation of 5 randomized blocks
- Each block contains `1`, `2`, `3`, and `4` exactly once
- Random order within each block
- Unique sequential session numbers
- Automatic CSV recording
- Simple graphical interface built with Tkinter
- Standalone Windows executable support through PyInstaller

## How It Works

When a new session is created, the application automatically:

1. Generates a random assignment between `1` and `2`.
2. Generates five independent randomized blocks.
3. Displays the five block sequences.
4. Records the generated randomization in a CSV file.

The assignment is generated once per session. The **Reveal Assignment** button only displays the previously generated result and does not perform a new randomization.

## Randomized Blocks

Each block contains the four values:

```text
1 2 3 4
```

exactly once, with their order randomly shuffled.

Example:

```text
Block 1: 4 1 3 2
Block 2: 3 2 4 1
Block 3: 1 4 3 2
Block 4: 2 3 1 4
Block 5: 4 2 1 3
```

Each block is randomized independently.

## Sessions

Every new session receives a sequential identifier:

```text
0001
0002
0003
...
```

A new randomization is generated for every session.

## Data Storage

Generated sessions are automatically stored in:

```text
data/randomization.csv
```

The CSV contains:

- Session
- Date/Time
- Assignment
- Block 1
- Block 2
- Block 3
- Block 4
- Block 5

The file uses `;` as the delimiter.

## Requirements

To run the Python source code:

- Python 3
- Tkinter

Tkinter is included with standard Python installations on Windows.

## Running the Application

Run:

```bash
python random_sequence_generator.py
```

## Creating a Windows Executable

The repository includes:

```text
build_executable.bat
```

Run the batch file on Windows.

It uses PyInstaller to generate:

```text
dist/RandomSequenceGenerator.exe
```

The resulting executable can be opened directly on Windows without VS Code or a Python installation.

## Project Structure

```text
random-sequence-generator/
│
├── random_sequence_generator.py
├── build_executable.bat
├── README.md
│
├── data/
│   └── randomization.csv
│
└── dist/
    └── RandomSequenceGenerator.exe
```

## Implementation

The application uses Python's standard `random` module.

For each block, the application creates:

```python
[1, 2, 3, 4]
```

and independently applies `random.shuffle()`.

This guarantees that every block contains all four values exactly once while randomizing their order.

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
