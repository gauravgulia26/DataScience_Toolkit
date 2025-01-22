import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plotly.express as px
import plotly.graph_objects as go


class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations GUI")
        self.root.geometry("900x700")

        # Matrix attributes
        self.matrix_a = None
        self.matrix_b = None

        # PCA results
        self.pca_data = None

        # Create UI components
        self.create_ui()

    def create_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Matrix Operations", font=("Arial", 20))
        title_label.pack(pady=10)

        # Input frames
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Matrix A (comma-separated rows):").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.matrix_a_entry = tk.Entry(input_frame, width=50)
        self.matrix_a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Matrix B (comma-separated rows):").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.matrix_b_entry = tk.Entry(input_frame, width=50)
        self.matrix_b_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons for file operations
        ttk.Button(
            input_frame, text="Load Matrix A from File", command=self.load_matrix_a
        ).grid(row=0, column=2, padx=5)
        ttk.Button(
            input_frame, text="Load Matrix B from File", command=self.load_matrix_b
        ).grid(row=1, column=2, padx=5)

        # Buttons for matrix operations
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Add", command=self.add_matrices).grid(
            row=0, column=0, padx=5, pady=5
        )
        ttk.Button(button_frame, text="Subtract", command=self.subtract_matrices).grid(
            row=0, column=1, padx=5, pady=5
        )
        ttk.Button(button_frame, text="Multiply", command=self.multiply_matrices).grid(
            row=0, column=2, padx=5, pady=5
        )
        ttk.Button(
            button_frame, text="Transpose A", command=self.transpose_matrix_a
        ).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(
            button_frame, text="Determinant A", command=self.determinant_matrix_a
        ).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(button_frame, text="Inverse A", command=self.inverse_matrix_a).grid(
            row=0, column=5, padx=5, pady=5
        )

        # Visualization buttons
        ttk.Button(
            button_frame, text="Matplotlib Heatmap", command=self.plot_with_matplotlib
        ).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(
            button_frame, text="Plotly Heatmap", command=self.plot_with_plotly
        ).grid(row=1, column=2, padx=5, pady=5)

        # PCA section
        pca_frame = tk.Frame(self.root)
        pca_frame.pack(pady=10)

        ttk.Button(
            pca_frame, text="Calculate PCA (2D)", command=lambda: self.calculate_pca(2)
        ).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(
            pca_frame, text="Calculate PCA (3D)", command=lambda: self.calculate_pca(3)
        ).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(
            pca_frame, text="Visualize PCA (3D)", command=self.visualize_pca_3d
        ).grid(row=0, column=2, padx=5, pady=5)

        # Save matrix button
        ttk.Button(self.root, text="Save Result to CSV", command=self.save_result).pack(
            pady=10
        )

        # Output frame
        self.output_text = tk.Text(self.root, height=10, width=100, wrap=tk.WORD)
        self.output_text.pack(pady=10)

    def parse_matrix(self, matrix_str):
        """Parses a comma-separated matrix string into a NumPy array."""
        try:
            rows = matrix_str.strip().split("\n")
            matrix = [list(map(float, row.split(","))) for row in rows]
            return np.array(matrix)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid matrix input: {e}")
            return None

    def load_matrix_a(self):
        """Loads matrix A from a CSV file."""
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                self.matrix_a = pd.read_csv(filepath, header=None).values
                self.matrix_a_entry.delete(0, tk.END)
                self.matrix_a_entry.insert(0, str(self.matrix_a.tolist()))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load Matrix A: {e}")

    def load_matrix_b(self):
        """Loads matrix B from a CSV file."""
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                self.matrix_b = pd.read_csv(filepath, header=None).values
                self.matrix_b_entry.delete(0, tk.END)
                self.matrix_b_entry.insert(0, str(self.matrix_b.tolist()))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load Matrix B: {e}")

    def add_matrices(self):
        self.load_matrices()
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = self.matrix_a + self.matrix_b
                self.display_result("Addition", result)
            except Exception as e:
                messagebox.showerror("Error", f"Addition failed: {e}")

    def subtract_matrices(self):
        self.load_matrices()
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = self.matrix_a - self.matrix_b
                self.display_result("Subtraction", result)
            except Exception as e:
                messagebox.showerror("Error", f"Subtraction failed: {e}")

    def multiply_matrices(self):
        self.load_matrices()
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = np.dot(self.matrix_a, self.matrix_b)
                self.display_result("Multiplication", result)
            except Exception as e:
                messagebox.showerror("Error", f"Multiplication failed: {e}")

    def transpose_matrix_a(self):
        self.load_matrices()
        if self.matrix_a is not None:
            result = self.matrix_a.T
            self.display_result("Transpose of A", result)

    def determinant_matrix_a(self):
        self.load_matrices()
        if self.matrix_a is not None:
            if self.matrix_a.shape[0] == self.matrix_a.shape[1]:
                result = np.linalg.det(self.matrix_a)
                self.display_result("Determinant of A", result)
            else:
                messagebox.showerror(
                    "Error", "Matrix A must be square for determinant."
                )

    def inverse_matrix_a(self):
        self.load_matrices()
        if self.matrix_a is not None:
            if self.matrix_a.shape[0] == self.matrix_a.shape[1]:
                try:
                    result = np.linalg.inv(self.matrix_a)
                    self.display_result("Inverse of A", result)
                except np.linalg.LinAlgError:
                    messagebox.showerror(
                        "Error", "Matrix A is singular and cannot be inverted."
                    )
            else:
                messagebox.showerror("Error", "Matrix A must be square for inversion.")

    def calculate_pca(self, n_components):
        self.load_matrices()
        if self.matrix_a is not None:
            try:
                pca = PCA(n_components=n_components)
                self.pca_data = pca.fit_transform(self.matrix_a)
                self.display_result(f"PCA ({n_components}D)", self.pca_data)
            except Exception as e:
                messagebox.showerror("Error", f"PCA calculation failed: {e}")

    def visualize_pca_3d(self):
        if self.pca_data is not None and self.pca_data.shape[1] == 3:
            fig = go.Figure(
                data=[
                    go.Scatter3d(
                        x=self.pca_data[:, 0],
                        y=self.pca_data[:, 1],
                        z=self.pca_data[:, 2],
                        mode="markers",
                        marker=dict(
                            size=5,
                            color=self.pca_data[:, 2],
                            colorscale="Viridis",
                            opacity=0.8,
                        ),
                    )
                ]
            )
            fig.update_layout(
                title="3D PCA Visualization",
                scene=dict(xaxis_title="PC1", yaxis_title="PC2", zaxis_title="PC3"),
            )
            fig.show()
        else:
            messagebox.showerror(
                "Error", "PCA data is not 3D. Perform PCA with 3 components first."
            )

    def plot_with_matplotlib(self):
        self.load_matrices()
        if self.matrix_a is not None:
            plt.imshow(self.matrix_a, cmap="viridis", interpolation="none")
            plt.colorbar()
            plt.title("Matrix A - Matplotlib Visualization")
            plt.show()

    def plot_with_plotly(self):
        self.load_matrices()
        if self.matrix_a is not None:
            df = pd.DataFrame(self.matrix_a)
            fig = px.imshow(df, text_auto=True, title="Matrix A - Plotly Heatmap")
            fig.show()

    def load_matrices(self):
        """Loads matrices A and B from the input fields."""
        self.matrix_a = self.parse_matrix(self.matrix_a_entry.get())
        self.matrix_b = self.parse_matrix(self.matrix_b_entry.get())

    def display_result(self, operation, result):
        """Displays the result of an operation in the output text box."""
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"{operation} Result:\n{result}\n")

    def save_result(self):
        """Saves the result matrix to a CSV file."""
        result_text = self.output_text.get(1.0, tk.END).strip()
        if result_text:
            filepath = filedialog.asksaveasfilename(
                defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
            )
            if filepath:
                try:
                    result_matrix = eval(result_text.split("Result:")[-1].strip())
                    pd.DataFrame(result_matrix).to_csv(
                        filepath, index=False, header=False
                    )
                    messagebox.showinfo("Success", f"Result saved to {filepath}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save result: {e}")
        else:
            messagebox.showerror("Error", "No result to save!")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
