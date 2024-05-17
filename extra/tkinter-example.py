import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt


class CSVGrapherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Grapher")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="No file selected")
        self.label.pack(pady=20)

        self.open_button = tk.Button(root, text="Open CSV", command=self.open_file)
        self.open_button.pack(pady=10)

        self.plot_button = tk.Button(root, text="Plot Graph", command=self.plot_graph, state=tk.DISABLED)
        self.plot_button.pack(pady=10)

        self.filepath = ""

    def open_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filepath:
            self.label.config(text=self.filepath)
            self.plot_button.config(state=tk.NORMAL)
        else:
            self.label.config(text="No file selected")
            self.plot_button.config(state=tk.DISABLED)

    def plot_graph(self):
        if self.filepath:
            try:
                df = pd.read_csv(self.filepath)
                if df.empty:
                    messagebox.showerror("Error", "The selected file is empty.")
                    return

                # Plotting the graph (assuming the CSV has at least two columns)
                df.plot()
                plt.xlabel('Index')
                plt.ylabel('Values')
                plt.title('CSV Data Plot')
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read or plot CSV file.\n{e}")
        else:
            messagebox.showerror("Error", "No file selected to plot.")


def main():
    root = tk.Tk()
    app = CSVGrapherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
