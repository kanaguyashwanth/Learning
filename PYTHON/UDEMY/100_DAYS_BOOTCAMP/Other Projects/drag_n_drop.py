import tkinter as tk
from tkinter import filedialog
import socket
import os

# Function to send file to a specified host and port
def send_file(filename, host, port):
    try:
        # Open the file in binary mode for reading
        with open(filename, "rb") as file:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Connect to the specified host and port
                s.connect((host, port))
                # Send file contents in chunks
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    s.sendall(data)
                print("File sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")

# Function to handle file selection and send file
def select_and_send_file():
    # Open file dialog to select a file
    filename = filedialog.askopenfilename()
    if filename:
        # Prompt user to enter host and port
        host = input("Enter the host IP: ")
        port = int(input("Enter the port number: "))
        # Send the selected file
        send_file(filename, host, port)

# Create tkinter window
window = tk.Tk()
window.title("File Transfer App")

# Create and configure a button for selecting and sending file
select_button = tk.Button(window, text="Select File", command=select_and_send_file)
select_button.pack(pady=20)

# Run the tkinter event loop
window.mainloop()
