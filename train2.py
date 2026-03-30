from tkinter import messagebox
import os

def Trainmodel():
    datadir = "DATA"

    if not os.path.exists(datadir):
        messagebox.showerror("Error", "DATA folder not found ❌")
        return

    images = [f for f in os.listdir(datadir) if f.endswith(".jpg")]

    if len(images) == 0:
        messagebox.showerror("Error", "No images found in DATA ❌")
        return

    messagebox.showinfo(
        "Success",
        f"Dataset Ready ✅\nTotal Images: {len(images)}\nDeepFace model will be used directly"
    )