import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime

class WeatherDataAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Data Analysis System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")

        # Data variable
        self.df = None
        self.csv_file = "weather_data.csv"

        # Create main frame
        self.create_widgets()

        # Auto-load data if file exists
        self.load_data()

    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X, pady=(0, 10))

        title_label = tk.Label(
            title_frame,
            text="Weather Data Analysis System",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=20)

        # Control Panel Frame
        control_frame = tk.Frame(self.root, bg="#ecf0f1", relief=tk.RAISED, borderwidth=2)
        control_frame.pack(fill=tk.X, padx=10, pady=5)

        # Buttons
        btn_load = tk.Button(
            control_frame,
            text="Load CSV File",
            command=self.load_csv_file,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_load.pack(side=tk.LEFT, padx=10, pady=10)

        btn_stats = tk.Button(
            control_frame,
            text="Show Statistics",
            command=self.show_statistics,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_stats.pack(side=tk.LEFT, padx=5, pady=10)

        btn_temp = tk.Button(
            control_frame,
            text="Temperature Trend",
            command=self.plot_temperature,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_temp.pack(side=tk.LEFT, padx=5, pady=10)

        btn_rain = tk.Button(
            control_frame,
            text="Rainfall Analysis",
            command=self.plot_rainfall,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_rain.pack(side=tk.LEFT, padx=5, pady=10)

        btn_conditions = tk.Button(
            control_frame,
            text="Weather Conditions",
            command=self.plot_conditions,
            bg="#f39c12",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_conditions.pack(side=tk.LEFT, padx=5, pady=10)

        btn_correlation = tk.Button(
            control_frame,
            text="Correlation Matrix",
            command=self.plot_correlation,
            bg="#16a085",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_correlation.pack(side=tk.LEFT, padx=5, pady=10)

        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Left Panel - Data Display
        left_panel = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, borderwidth=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        data_label = tk.Label(
            left_panel,
            text="Weather Data Preview",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        data_label.pack(pady=10)

        # Treeview for data display
        tree_frame = tk.Frame(left_panel)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar_y = tk.Scrollbar(tree_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            show="headings"
        )
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        # Right Panel - Visualization
        right_panel = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, borderwidth=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

        viz_label = tk.Label(
            right_panel,
            text="Data Visualization",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        viz_label.pack(pady=10)

        self.canvas_frame = tk.Frame(right_panel, bg="white")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Status Bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            bg="#34495e",
            fg="white",
            font=("Arial", 10),
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def load_csv_file(self):
        """Load CSV file from file dialog"""
        file_path = filedialog.askopenfilename(
            title="Select Weather Data CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if file_path:
            self.csv_file = file_path
            self.load_data()

    def load_data(self):
        """Load data from CSV file"""
        try:
            self.df = pd.read_csv(self.csv_file)
            self.display_data()
            self.status_bar.config(text=f"Data loaded successfully: {len(self.df)} records from {self.csv_file}")
            messagebox.showinfo("Success", f"Loaded {len(self.df)} weather records successfully!")
        except FileNotFoundError:
            self.status_bar.config(text=f"File not found: {self.csv_file}")
            messagebox.showerror("Error", f"CSV file not found: {self.csv_file}\nPlease select a valid file.")
        except Exception as e:
            self.status_bar.config(text=f"Error loading data: {str(e)}")
            messagebox.showerror("Error", f"Error loading data: {str(e)}")

    def display_data(self):
        """Display data in treeview"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Set up columns
        self.tree["columns"] = list(self.df.columns)
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Insert data (first 100 rows)
        for idx, row in self.df.head(100).iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def clear_canvas(self):
        """Clear the visualization canvas"""
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

    def show_statistics(self):
        """Show statistical summary"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load data first!")
            return

        stats_window = tk.Toplevel(self.root)
        stats_window.title("Weather Data Statistics")
        stats_window.geometry("800x600")

        # Create text widget with scrollbar
        text_frame = tk.Frame(stats_window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(text_frame, font=("Courier", 10), yscrollcommand=scrollbar.set)
        text_widget.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        # Generate statistics
        stats_text = "=" * 80 + "\n"
        stats_text += "WEATHER DATA STATISTICAL SUMMARY\n"
        stats_text += "=" * 80 + "\n\n"

        stats_text += f"Total Records: {len(self.df)}\n"
        stats_text += f"Date Range: {self.df['Date'].min()} to {self.df['Date'].max()}\n\n"

        stats_text += "Descriptive Statistics:\n"
        stats_text += "-" * 80 + "\n"
        stats_text += str(self.df.describe()) + "\n\n"

        stats_text += "Weather Condition Distribution:\n"
        stats_text += "-" * 80 + "\n"
        stats_text += str(self.df['Weather_Condition'].value_counts()) + "\n\n"

        # Temperature analysis
        stats_text += "Temperature Analysis:\n"
        stats_text += "-" * 80 + "\n"
        stats_text += f"Average Temperature: {self.df['Temperature_C'].mean():.2f}°C\n"
        stats_text += f"Hottest Day: {self.df.loc[self.df['Temperature_C'].idxmax(), 'Date']} "
        stats_text += f"({self.df['Temperature_C'].max():.2f}°C)\n"
        stats_text += f"Coldest Day: {self.df.loc[self.df['Temperature_C'].idxmin(), 'Date']} "
        stats_text += f"({self.df['Temperature_C'].min():.2f}°C)\n\n"

        # Rainfall analysis
        stats_text += "Rainfall Analysis:\n"
        stats_text += "-" * 80 + "\n"
        stats_text += f"Total Rainfall: {self.df['Rainfall_mm'].sum():.2f} mm\n"
        stats_text += f"Average Daily Rainfall: {self.df['Rainfall_mm'].mean():.2f} mm\n"
        stats_text += f"Rainy Days: {(self.df['Rainfall_mm'] > 0).sum()} days\n"
        stats_text += f"Maximum Rainfall: {self.df['Rainfall_mm'].max():.2f} mm "
        stats_text += f"on {self.df.loc[self.df['Rainfall_mm'].idxmax(), 'Date']}\n\n"

        # Wind analysis
        stats_text += "Wind Analysis:\n"
        stats_text += "-" * 80 + "\n"
        stats_text += f"Average Wind Speed: {self.df['Wind_Speed_kmh'].mean():.2f} km/h\n"
        stats_text += f"Maximum Wind Speed: {self.df['Wind_Speed_kmh'].max():.2f} km/h\n\n"

        text_widget.insert(tk.END, stats_text)
        text_widget.config(state=tk.DISABLED)

    def plot_temperature(self):
        """Plot temperature trend"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load data first!")
            return

        self.clear_canvas()

        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)

        # Convert date to datetime for better plotting
        dates = pd.to_datetime(self.df['Date'])

        ax.plot(dates, self.df['Temperature_C'], color='#e74c3c', linewidth=2, label='Temperature')
        ax.fill_between(dates, self.df['Temperature_C'], alpha=0.3, color='#e74c3c')

        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
        ax.set_title('Temperature Trend Over Time', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.autofmt_xdate()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.status_bar.config(text="Temperature trend displayed")

    def plot_rainfall(self):
        """Plot rainfall analysis"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load data first!")
            return

        self.clear_canvas()

        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)

        dates = pd.to_datetime(self.df['Date'])

        # Bar plot for rainfall
        ax.bar(dates, self.df['Rainfall_mm'], color='#3498db', alpha=0.7, label='Rainfall')

        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_ylabel('Rainfall (mm)', fontsize=12, fontweight='bold')
        ax.set_title('Daily Rainfall Analysis', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        ax.legend()
        fig.autofmt_xdate()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.status_bar.config(text="Rainfall analysis displayed")

    def plot_conditions(self):
        """Plot weather conditions distribution"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load data first!")
            return

        self.clear_canvas()

        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)

        condition_counts = self.df['Weather_Condition'].value_counts()
        colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']

        wedges, texts, autotexts = ax.pie(
            condition_counts.values,
            labels=condition_counts.index,
            autopct='%1.1f%%',
            colors=colors[:len(condition_counts)],
            startangle=90
        )

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax.set_title('Weather Conditions Distribution', fontsize=14, fontweight='bold')

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.status_bar.config(text="Weather conditions distribution displayed")

    def plot_correlation(self):
        """Plot correlation matrix"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load data first!")
            return

        self.clear_canvas()

        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)

        # Select numeric columns
        numeric_cols = ['Temperature_C', 'Humidity_%', 'Wind_Speed_kmh', 
                       'Pressure_hPa', 'Visibility_km', 'Rainfall_mm']
        corr_matrix = self.df[numeric_cols].corr()

        # Create heatmap
        im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)

        # Set ticks
        ax.set_xticks(np.arange(len(numeric_cols)))
        ax.set_yticks(np.arange(len(numeric_cols)))

        # Set labels
        labels = ['Temp', 'Humid', 'Wind', 'Press', 'Visib', 'Rain']
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_yticklabels(labels)

        # Add correlation values
        for i in range(len(numeric_cols)):
            for j in range(len(numeric_cols)):
                text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                             ha="center", va="center", color="black", fontsize=9)

        ax.set_title('Correlation Matrix of Weather Parameters', fontsize=12, fontweight='bold')
        fig.colorbar(im, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.status_bar.config(text="Correlation matrix displayed")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDataAnalyzer(root)
    root.mainloop()
