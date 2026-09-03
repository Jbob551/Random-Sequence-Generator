import csv
import random
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


class RandomSequenceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Sequence Generator")
        self.root.geometry("1050x650")
        self.root.minsize(900, 600)

        self.session_number = self.next_session_number()
        self.assignment = None
        self.blocks = []
        self.session_saved = False

        self.build_interface()
        self.new_session(initial=True)

    # -------------------------------------------------
    # FILES
    # -------------------------------------------------

    def data_dir(self):
        folder = Path(__file__).resolve().parent / "data"
        folder.mkdir(exist_ok=True)
        return folder

    def csv_path(self):
        return self.data_dir() / "randomization.csv"

    def next_session_number(self):
        path = self.csv_path()

        if not path.exists():
            return 1

        try:
            with path.open("r", encoding="utf-8-sig", newline="") as file:
                rows = list(csv.DictReader(file))

            numbers = []

            for row in rows:
                value = row.get("Session", "")

                if value.isdigit():
                    numbers.append(int(value))

            return max(numbers, default=0) + 1

        except Exception:
            return 1

    # -------------------------------------------------
    # INTERFACE
    # -------------------------------------------------

    def build_interface(self):
        root = self.root

        tk.Label(
            root,
            text="RANDOM SEQUENCE GENERATOR",
            font=("Arial", 24, "bold")
        ).pack(pady=(18, 4))

        tk.Label(
            root,
            text="Randomized assignment and block sequence generator",
            font=("Arial", 11)
        ).pack(pady=(0, 10))

        self.session_label = tk.Label(
            root,
            text="Session: ---",
            font=("Arial", 12, "bold")
        )
        self.session_label.pack()

        # -------------------------------------------------
        # ASSIGNMENT
        # -------------------------------------------------

        assignment_frame = tk.LabelFrame(
            root,
            text="Assignment",
            font=("Arial", 13, "bold"),
            padx=35,
            pady=12
        )
        assignment_frame.pack(pady=18)

        self.assignment_result = tk.Label(
            assignment_frame,
            text="-",
            font=("Arial", 25, "bold"),
            width=18,
            height=2
        )
        self.assignment_result.pack()

        tk.Button(
            assignment_frame,
            text="REVEAL ASSIGNMENT",
            font=("Arial", 12, "bold"),
            command=self.reveal_assignment,
            width=20
        ).pack(pady=5)

        # -------------------------------------------------
        # BLOCKS
        # -------------------------------------------------

        tk.Label(
            root,
            text="RANDOMIZED BLOCK SEQUENCES",
            font=("Arial", 16, "bold")
        ).pack(pady=(5, 8))

        self.blocks_frame = tk.Frame(root)
        self.blocks_frame.pack(pady=5)

        self.block_labels = []

        for i in range(5):
            frame = tk.LabelFrame(
                self.blocks_frame,
                text=f"Block {i + 1}",
                font=("Arial", 12, "bold"),
                padx=12,
                pady=8
            )
            frame.grid(row=0, column=i, padx=7)

            labels = []

            for _ in range(4):
                label = tk.Label(
                    frame,
                    text="-",
                    font=("Arial", 20, "bold"),
                    width=4,
                    height=1,
                    relief="solid",
                    bd=1
                )
                label.pack(pady=3)
                labels.append(label)

            self.block_labels.append(labels)

        # -------------------------------------------------
        # CONTROLS
        # -------------------------------------------------

        controls = tk.Frame(root)
        controls.pack(pady=25)

        tk.Button(
            controls,
            text="NEW SESSION",
            font=("Arial", 13, "bold"),
            command=self.new_session,
            width=18,
            height=2
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            controls,
            text="OPEN DATA FOLDER",
            font=("Arial", 13, "bold"),
            command=self.open_data_folder,
            width=22,
            height=2
        ).grid(row=0, column=1, padx=10)

        self.save_status = tk.Label(
            root,
            text="",
            font=("Arial", 10)
        )
        self.save_status.pack()

        tk.Label(
            root,
            text="Assignment: 1 or 2  •  Each block contains 1, 2, 3 and 4 exactly once.",
            font=("Arial", 9)
        ).pack(side="bottom", pady=10)

    # -------------------------------------------------
    # NEW SESSION
    # -------------------------------------------------

    def new_session(self, initial=False):
        if not initial:
            self.session_number += 1

        # Random assignment between 1 and 2.
        self.assignment = random.randint(1, 2)

        # Generate five independent randomized blocks.
        self.blocks = []

        for _ in range(5):
            block = [1, 2, 3, 4]
            random.shuffle(block)
            self.blocks.append(block)

        self.session_saved = False

        self.assignment_result.config(text="-")
        self.show_blocks()

        self.session_label.config(
            text=f"Session: {self.session_number:04d}"
        )

        # Record the randomization automatically.
        self.save_csv()

        self.save_status.config(
            text="Randomization generated and recorded automatically."
        )

    # -------------------------------------------------
    # ASSIGNMENT
    # -------------------------------------------------

    def reveal_assignment(self):
        # The assignment was already generated when the session started.
        # This button only reveals the existing result.
        self.assignment_result.config(text=str(self.assignment))

    # -------------------------------------------------
    # BLOCKS
    # -------------------------------------------------

    def show_blocks(self):
        for i, block in enumerate(self.blocks):
            for j, number in enumerate(block):
                self.block_labels[i][j].config(text=str(number))

    # -------------------------------------------------
    # CSV
    # -------------------------------------------------

    def save_csv(self):
        if self.session_saved:
            return

        path = self.csv_path()
        new_file = not path.exists()

        with path.open(
            "a",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            writer = csv.writer(file, delimiter=";")

            if new_file:
                writer.writerow([
                    "Session",
                    "Date/Time",
                    "Assignment",
                    "Block 1",
                    "Block 2",
                    "Block 3",
                    "Block 4",
                    "Block 5"
                ])

            writer.writerow([
                f"{self.session_number:04d}",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                self.assignment,
                "-".join(map(str, self.blocks[0])),
                "-".join(map(str, self.blocks[1])),
                "-".join(map(str, self.blocks[2])),
                "-".join(map(str, self.blocks[3])),
                "-".join(map(str, self.blocks[4]))
            ])

        self.session_saved = True

    # -------------------------------------------------
    # OPEN DATA FOLDER
    # -------------------------------------------------

    def open_data_folder(self):
        folder = self.data_dir()

        try:
            import os
            os.startfile(folder)
        except Exception:
            messagebox.showinfo(
                "Data Folder",
                f"Data folder:\n{folder}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomSequenceGenerator(root)
    root.mainloop()
