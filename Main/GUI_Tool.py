'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - GUI_Tool.py
24 Oct 2024
**
'''
#This is the main script for the GUI tool that integrates all the scripts developed by the group members
#Required Libraries for the GUI Tool to work
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import pandas as pd
import Insurance_Prediction  #correct import for insurance prediction

#import the updated scripts from the extracted folder
import sys #import sys to add the path to the extracted folder
#import the project .py files from the extracted folder
import best_model_selection
import Data_Exploration
import feature_selection
import finished
import get_dummies
import missing_values
import outlier_analysis
import Reading_The_Dataset
import regression
import train_data_split
import Visual_Exploratory
import visualization

#Create a class for the GUI tool
class CSVToolGUI:
    def __init__(self, root): #initialize the GUI window and variables
        self.root = root
        self.root.title("DAT") #set the title of the window, DAT stands for Dataset Analysis Tool
        self.root.geometry("1000x800") #set the size of the window in pixels
        self.root.configure(bg='#f0f0f0') #set the background color of the window
        
        #variables
        self.csv_path = None #initialize the csv path variable
        self.df = None #initialize the dataframe variable
        
        #create the widgets for the GUI
        self.create_widgets()

    def create_widgets(self):
        #title label for the GUI
        title_label = tk.Label(self.root, text="Dataset Analysis Tool", font=("Helvetica", 20, "bold"), bg='#4a90e2', fg='white') #set the title label text, font, and color
        title_label.pack(fill=tk.X, pady=10) #pack the title label to the window

        #create a frame for buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10, fill=tk.X)

        #create a "load csv" button
        load_button = tk.Button(button_frame, text="Load CSV File", command=self.load_csv, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        load_button.grid(row=0, column=0, padx=10, pady=5)

        #create the gui functionality buttons
        explore_button = tk.Button(button_frame, text="Data Exploration", command=self.data_exploration, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        explore_button.grid(row=0, column=1, padx=10, pady=5)
        #add a button for handling missing values
        missing_values_button = tk.Button(button_frame, text="Handle Missing Values", command=self.handle_missing_values, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        missing_values_button.grid(row=0, column=2, padx=10, pady=5)
        #add a button for outlier analysis
        outlier_button = tk.Button(button_frame, text="Outlier Analysis", command=self.outlier_analysis, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        outlier_button.grid(row=1, column=0, padx=10, pady=5)
        #add a button for feature selection
        feature_button = tk.Button(button_frame, text="Feature Selection", command=self.feature_selection, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        feature_button.grid(row=1, column=1, padx=10, pady=5)
        #add a button for running regression
        regression_button = tk.Button(button_frame, text="Run Regression", command=self.run_regression, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        regression_button.grid(row=1, column=2, padx=10, pady=5)
        #add a button for visualization
        visualization_button = tk.Button(button_frame, text="Visualization", command=self.visualization, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        visualization_button.grid(row=2, column=0, padx=10, pady=5)
        #add a new button for predicting insurance cost
        predict_button = tk.Button(button_frame, text="Predict Insurance Cost", command=self.predict_insurance, bg='#4a90e2', fg='white', font=("Helvetica", 12, "bold"), width=20)
        predict_button.grid(row=2, column=1, padx=10, pady=5)
        #add a button to clear the text output
        clear_button = tk.Button(button_frame, text="Clear Output", command=self.clear_output, bg='#d9534f', fg='white', font=("Helvetica", 12, "bold"), width=20)
        clear_button.grid(row=2, column=2, padx=10, pady=5)
        #output box
        self.output_text = scrolledtext.ScrolledText(self.root, width=100, height=20, wrap=tk.WORD, font=("Courier", 10))
        self.output_text.pack(pady=10)
    #function to load the csv file and display a success message
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")]) #open a file dialog to select a csv file to load
        if file_path:#if a file is selected
            try:
                self.df = pd.read_csv(file_path)
                self.csv_path = file_path
                self.output_text.insert(tk.END, "CSV file loaded successfully!\n")
                messagebox.showinfo("Success", "CSV file loaded successfully!")
            #display an error message if the file fails to load
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV file: {e}")
    #function to run the data exploration script
    def data_exploration(self):
        #check if a csv file is loaded
        if self.df is not None:
            output = Data_Exploration.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")
            messagebox.showinfo("Success", "Data Exploration completed!")
        #display an error message if no csv file is loaded
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to handle missing values
    def handle_missing_values(self):
        #check if a csv file is loaded
        if self.df is not None:
            output = missing_values.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")#insert the output message to the text box
            #display a success message
            messagebox.showinfo("Success", "Missing values handled!")
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to run the outlier analysis script
    def outlier_analysis(self):
        if self.df is not None:
            output = outlier_analysis.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")
            messagebox.showinfo("Success", "Outlier analysis completed!")
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to run the feature selection script
    def feature_selection(self):
        if self.df is not None:
            output = feature_selection.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")
            messagebox.showinfo("Success", "Feature selection completed!")
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to run the regression script
    def run_regression(self):
        if self.df is not None:
            output = regression.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")
            messagebox.showinfo("Success", "Regression analysis completed!")
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to run the visualization script
    def visualization(self):
        if self.df is not None:
            output = visualization.run(self.df)
            if output:
                self.output_text.insert(tk.END, output + "\n")
            messagebox.showinfo("Success", "Visualization completed!")
            self.plot_histograms()
        else:
            messagebox.showerror("Error", "Please load a CSV file first.")
    #function to predict insurance cost
    def predict_insurance(self):
        #create a new window for user inputs
        predict_window = tk.Toplevel(self.root)
        predict_window.title("Predict Insurance Cost")
        predict_window.geometry("400x400")#set the size of the window in pixels

        #Create input fields for "age"
        tk.Label(predict_window, text="Age:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        age_entry = tk.Entry(predict_window)
        age_entry.grid(row=0, column=1, padx=10, pady=5)

        #create input fields for "Sex"
        tk.Label(predict_window, text="Sex:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        sex_combobox = ttk.Combobox(predict_window, values=["male", "female"])
        sex_combobox.grid(row=1, column=1, padx=10, pady=5)
        sex_combobox.current(0)

        #Create input fields for "BMI"
        tk.Label(predict_window, text="BMI:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        bmi_entry = tk.Entry(predict_window)
        bmi_entry.grid(row=2, column=1, padx=10, pady=5)

        #create input fields for "Children"
        tk.Label(predict_window, text="Children:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        children_entry = tk.Entry(predict_window)
        children_entry.grid(row=3, column=1, padx=10, pady=5)

        #Create input fields for "Smoker"
        tk.Label(predict_window, text="Smoker:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        smoker_combobox = ttk.Combobox(predict_window, values=["yes", "no"])
        smoker_combobox.grid(row=4, column=1, padx=10, pady=5)
        smoker_combobox.current(1)

        #create input fields for "Region"
        tk.Label(predict_window, text="Region:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        region_combobox = ttk.Combobox(predict_window, values=["northeast", "northwest", "southeast", "southwest"])
        region_combobox.grid(row=5, column=1, padx=10, pady=5) #set the position of the region combobox
        region_combobox.current(0)
        #function to make the prediction based on user inputs
        def on_predict():
            try:
                #get values from entry fields
                age_str = age_entry.get()#get the value from the age entry field
                bmi_str = bmi_entry.get()#get the value from the bmi entry field
                children_str = children_entry.get()#get the value from the children entry field

                #check if all fields are filled
                if not age_str or not bmi_str or not children_str:
                    raise ValueError("All fields must be filled.")

                #convert inputs
                age = int(age_str)
                bmi = float(bmi_str)
                children = int(children_str)
                sex = sex_combobox.get()
                smoker = smoker_combobox.get()
                region = region_combobox.get()

                #make prediction
                prediction = Insurance_Prediction.predict_insurance(age, sex, bmi, children, smoker, region)

                #display prediction
                messagebox.showinfo("Prediction Result", prediction)
            except ValueError as e:
                messagebox.showerror("Input Error", f"Please enter valid inputs.\n{e}")

        #predict button
        predict_button = tk.Button(predict_window, text="Predict", command=on_predict, bg='#5cb85c', fg='white', font=("Helvetica", 12, "bold"))
        predict_button.grid(row=6, column=0, columnspan=2, pady=20)
    #function to clear the output text box
    def clear_output(self):
        self.output_text.delete('1.0', tk.END)

    #def plot_histograms(self):
        #import matplotlib.pyplot as plt
        #import seaborn as sns
        #from io import BytesIO
        import PIL.Image, PIL.ImageTk
        #check if a csv file is loaded
        if self.df is not None:
            numerical_columns = self.df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            for column in numerical_columns:
                plt.figure(figsize=(8, 5))#set the figure size
                sns.histplot(self.df[column], bins=30, kde=True, color='skyblue')#create a histogram plot
                plt.title(f'Distribution of {column}') #set the title of the plot
                plt.xlabel(column) #set the x-axis label
                plt.ylabel('Frequency') #set the y-axis label
                plt.grid(True) #display grid lines
                
                #save plot to a buffer
                buffer = BytesIO() #create a buffer to save the plot
                plt.savefig(buffer, format='png') #save the plot to the buffer
                buffer.seek(0) #reset the buffer position to the start
                plt.close() #close the plot to free memory
                
                #display the image in the gui
                image = PIL.Image.open(buffer)
                photo = PIL.ImageTk.PhotoImage(image)
                image_label = tk.Label(self.root, image=photo)
                image_label.image = photo  #keep a reference to avoid garbage collection
                image_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVToolGUI(root)
    root.mainloop()