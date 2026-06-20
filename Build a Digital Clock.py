import sys
from tkinter import Frame, Label, Tk
import time


def update_clock():
    # Fetch current time, day, and date
    current_time = time.strftime("%I:%M")  # Clean iOS style time (e.g., 04:15)
    current_seconds = time.strftime(":%S")  # Separate seconds
    am_pm = time.strftime("%p")
    current_date = time.strftime("%A, %B %d")  # e.g., Saturday, June 20

    # Update labels
    date_label.config(text=current_date)
    time_label.config(text=current_time)
    sec_label.config(text=current_seconds)
    ampm_label.config(text=am_pm.lower())  # Lowercase for modern iOS styling

    # Refresh loop
    time_label.after(1000, update_clock)


# Main window setup
root = Tk()
root.title("iOS Clock Widget")
root.configure(bg="#000000")  # True iOS Black background
root.geometry("450x250")
root.resizable(False, False)

# Main container to act like an iOS Widget panel
widget_frame = Frame(root, bg="#1C1C1E", bd=0)  # iOS Dark Gray widget color
widget_frame.place(relx=0.5, rely=0.5, anchor="center", width=410, height=210)

# Date Label (Top) - Changed "medium" to "normal"
date_label = Label(
    widget_frame,
    font=("SF Pro Display", 16, "normal"),
    bg="#1C1C1E",
    fg="#FF453A",  # iOS System Red
)
date_label.pack(pady=(35, 5))

# Time Container Frame
time_frame = Frame(widget_frame, bg="#1C1C1E")
time_frame.pack(pady=5)

# Main Time Label
time_label = Label(
    time_frame,
    font=("SF Pro Display", 54, "bold"),
    bg="#1C1C1E",
    fg="#FFFFFF",
)
time_label.pack(side="left")

# Sub-time container for Seconds and AM/PM
sub_time_frame = Frame(time_frame, bg="#1C1C1E")
sub_time_frame.pack(side="left", fill="y", padx=5, pady=10)

# Seconds Label
sec_label = Label(
    sub_time_frame,
    font=("SF Pro Display", 20, "normal"),
    bg="#1C1C1E",
    fg="#AEAEB2",
)
sec_label.pack(anchor="w")

# AM/PM Label - Changed "medium" to "normal"
ampm_label = Label(
    sub_time_frame,
    font=("SF Pro Display", 14, "normal"),
    bg="#1C1C1E",
    fg="#AEAEB2",
)
ampm_label.pack(anchor="w")

# Start the clock loop
update_clock()

# Run the app
root.mainloop()