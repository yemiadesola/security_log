#Name: Adeyemi Adesola
#Github Address: https://github.com/yourgithubusername
#Code snipet and output in Python - Security log analysis 
#Installing the 3 libraries below
#libraries pip install pandas -- instal library for reading csv
#pip install matplotlib- install library for plotting of graph
#pip install seaborn - install library for plotting graph


import pandas as pd #library for reading csv
import matplotlib.pyplot as plt #library for plotting of graph
import seaborn as sns #library for plotting graph
from tkinter import Tk, filedialog #library for the GUI to import csv 

# GUI prompt to upload CSV file
Tk().withdraw()  # Hide Tkinter root window
csv_filepath = filedialog.askopenfilename(title="Select CSV file")

#load and display data from selected csv file
data_frame = pd.read_csv(csv_filepath)

# Manage data types using timestamp for accurate time-based analysis 
# and categorized type for better memory usage
data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'])
data_frame['severity'] = pd.Categorical(data_frame['severity'])

# My function to count each event occurrence and output it on the terminal 
def summary_of_log_events(logs):
    return logs['event_type'].value_counts()

# Analyze data by summarizing the frequency of each security event
event_summary = summary_of_log_events(data_frame)
print(event_summary)

# This create a bar chat to visualize the data from the csv file
plt.figure(figsize=(8, 4))
sns.countplot(data=data_frame, x='event_type', order=data_frame['event_type'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Security Event Frequency Bar Chat')
plt.tight_layout()
plt.show()
