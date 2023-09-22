from lib.info import VERSION
import requests
import zipfile
import os, subprocess
import tkinter as tk
from tkinter import ttk
from threading import Thread


version = "nbi-v0.0.1"
window = tk.Tk()
window.geometry("700x320")
window.title(f"Nebula installer - {version}")
window.grid()

pb = ttk.Progressbar(
    window,
    orient = "horizontal",
    mode = "determinate",
    length=280
)
log_text = tk.Text(window, height=5)
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
log_text.grid(column=1, row=1, columnspan=2, padx=10, pady=20)

def log(string : str):
    log_text.insert(tk.END, string + "\n")
    log_text.see("end")
def _download():
    URL = f"https://github.com/TheHerowither/Nebula-lang/releases/download/AlphaRelease/{VERSION}.zip"
    log(f"Dowloading: {URL}")
    download = requests.get(URL)

    open(f"{VERSION}.zip", "wb").write(download.content)
    log("Dowload complete")
    log("Extracting")
    with zipfile.ZipFile(f"{VERSION}.zip", "r") as zip:
        zip.extractall(f"{VERSION}")
    #os.system(f'setx /M PATH "%path%;{os.path.join(os.getcwd(), VERSION)}"')
    log("Extraction complete")
    log(subprocess.getoutput(f".\\setsys.bat \\{VERSION}"))
    log(subprocess.getoutput(f"{VERSION}\\nebula --version"))
    pb.stop()
def download():
    th = Thread(target=_download)
    pb.start(3)
    th.start()

start_button = ttk.Button(
    window,
    text='Start',
    command=download
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)
window.mainloop()