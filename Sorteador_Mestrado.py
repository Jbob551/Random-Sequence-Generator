import csv
import random
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


class SorteadorMestrado:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteador do Experimento")
        self.root.geometry("1050x650")
        self.root.minsize(900, 600)

        self.session_number = self.next_session_number()
        self.braco = None
        self.blocos = []
        self.session_saved = False

        self.build_interface()
        self.nova_sessao(initial=True)

    # -------------------------------------------------
    # ARQUIVOS
    # -------------------------------------------------

    def data_dir(self):
        pasta = Path(__file__).resolve().parent / "dados"
        pasta.mkdir(exist_ok=True)
        return pasta

    def csv_path(self):
        return self.data_dir() / "randomizacao.csv"

    def next_session_number(self):
        path = self.csv_path()

        if not path.exists():
            return 1

        try:
            with path.open("r", encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))

            nums = []
            for row in rows:
                valor = row.get("Sessão", "")
                if valor.isdigit():
                    nums.append(int(valor))

            return max(nums, default=0) + 1

        except Exception:
            return 1

    # -------------------------------------------------
    # INTERFACE
    # -------------------------------------------------

    def build_interface(self):
        root = self.root

        tk.Label(
            root,
            text="SORTEADOR DO EXPERIMENTO",
            font=("Arial", 24, "bold")
        ).pack(pady=(18, 4))

        tk.Label(
            root,
            text="Realimentação sensorial de força por corrente elétrica senoidal",
            font=("Arial", 11)
        ).pack(pady=(0, 10))

        self.session_label = tk.Label(
            root,
            text="Sessão: ---",
            font=("Arial", 12, "bold")
        )
        self.session_label.pack()

        # -------------------------------------------------
        # SORTEIO DO BRAÇO
        # -------------------------------------------------

        arm_frame = tk.LabelFrame(
            root,
            text="Sorteio do braço",
            font=("Arial", 13, "bold"),
            padx=35,
            pady=12
        )
        arm_frame.pack(pady=18)

        self.arm_result = tk.Label(
            arm_frame,
            text="-",
            font=("Arial", 25, "bold"),
            width=18,
            height=2
        )
        self.arm_result.pack()

        tk.Button(
            arm_frame,
            text="SORTEAR BRAÇO",
            font=("Arial", 12, "bold"),
            command=self.sortear_braco,
            width=18
        ).pack(pady=5)

        # -------------------------------------------------
        # BLOCOS
        # -------------------------------------------------

        tk.Label(
            root,
            text="SEQUÊNCIA DOS 5 BLOCOS",
            font=("Arial", 16, "bold")
        ).pack(pady=(5, 8))

        self.blocks_frame = tk.Frame(root)
        self.blocks_frame.pack(pady=5)

        self.block_labels = []

        for i in range(5):
            frame = tk.LabelFrame(
                self.blocks_frame,
                text=f"Bloco {i + 1}",
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
        # CONTROLES
        # -------------------------------------------------

        controls = tk.Frame(root)
        controls.pack(pady=25)

        tk.Button(
            controls,
            text="NOVA SESSÃO",
            font=("Arial", 13, "bold"),
            command=self.nova_sessao,
            width=18,
            height=2
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            controls,
            text="ABRIR PASTA DOS DADOS",
            font=("Arial", 13, "bold"),
            command=self.abrir_pasta_dados,
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
            text="Braço: 1 = esquerdo | 2 = direito",
            font=("Arial", 9)
        ).pack(side="bottom", pady=10)

    # -------------------------------------------------
    # NOVA SESSÃO
    # -------------------------------------------------

    def nova_sessao(self, initial=False):
        if not initial:
            self.session_number += 1

        # Sorteio do braço: 1 = esquerdo, 2 = direito.
        self.braco = random.randint(1, 2)

        # Geração automática dos cinco blocos.
        # Cada bloco contém 1, 2, 3 e 4 exatamente uma vez,
        # em ordem aleatória.
        self.blocos = []

        for _ in range(5):
            bloco = [1, 2, 3, 4]
            random.shuffle(bloco)
            self.blocos.append(bloco)

        self.session_saved = False

        self.arm_result.config(text="-")
        self.mostrar_blocos()

        self.session_label.config(
            text=f"Sessão: {self.session_number:04d}"
        )

        # A randomização é registrada automaticamente.
        self.salvar_csv()

        self.save_status.config(
            text="Randomização criada e registrada automaticamente."
        )

    # -------------------------------------------------
    # SORTEIO DO BRAÇO
    # -------------------------------------------------

    def sortear_braco(self):
        # O braço já foi sorteado na criação da sessão.
        # Este botão apenas revela o resultado.
        if self.braco == 1:
            self.arm_result.config(text="1 — ESQUERDO")
        else:
            self.arm_result.config(text="2 — DIREITO")

    # -------------------------------------------------
    # MOSTRAR BLOCOS
    # -------------------------------------------------

    def mostrar_blocos(self):
        for i, bloco in enumerate(self.blocos):
            for j, numero in enumerate(bloco):
                self.block_labels[i][j].config(text=str(numero))

    # -------------------------------------------------
    # CSV
    # -------------------------------------------------

    def salvar_csv(self):
        if self.session_saved:
            return

        path = self.csv_path()
        novo_arquivo = not path.exists()

        with path.open(
            "a",
            encoding="utf-8-sig",
            newline=""
        ) as f:

            writer = csv.writer(f, delimiter=";")

            if novo_arquivo:
                writer.writerow([
                    "Sessão",
                    "Data/Hora",
                    "Braço",
                    "Bloco 1",
                    "Bloco 2",
                    "Bloco 3",
                    "Bloco 4",
                    "Bloco 5"
                ])

            writer.writerow([
                f"{self.session_number:04d}",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                self.braco,
                "-".join(map(str, self.blocos[0])),
                "-".join(map(str, self.blocos[1])),
                "-".join(map(str, self.blocos[2])),
                "-".join(map(str, self.blocos[3])),
                "-".join(map(str, self.blocos[4]))
            ])

        self.session_saved = True

    # -------------------------------------------------
    # ABRIR PASTA DOS DADOS
    # -------------------------------------------------

    def abrir_pasta_dados(self):
        pasta = self.data_dir()

        try:
            import os
            os.startfile(pasta)
        except Exception:
            messagebox.showinfo(
                "Pasta dos dados",
                f"Os dados estão em:\n{pasta}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorMestrado(root)
    root.mainloop()
