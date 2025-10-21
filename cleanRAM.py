import subprocess
import tkinter as tk
from tkinter import messagebox



#This function clean cache RAM in older PCs
def cleanCacheRAM():
    try:
        #This subprocess sync the memory RAM
        subprocess.run(["sudo sync"],shell=True ,check=True)   
    except subprocess.CalledProcessError as e: 
        #In case of error show message to the user why not working.     
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error",f"Fallo el comando:\n{e}")
        root.destroy()
        

def cleanCompleteRAM():
    try:
        #Clean the cache L1,L2,L3 . 
        subprocess.run("sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'", shell=True, check=True)
        subprocess.run("sudo sh -c 'echo 2 > /proc/sys/vm/drop_caches'", shell=True, check=True)
        subprocess.run("sudo sh -c 'echo 1 > /proc/sys/vm/drop_caches'", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        #In case of error show message to the user why not working.       
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error",f"Fallo el comando:\n{e}")
        root.destroy()
        
        
def showMessage(): 
        #When are fishing the task show one window said the memory has been cleaned.      
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("RAM limpiada", "✅ Se ha limpiado la caché de RAM correctamente.")
        root.destroy() 
        
      
cleanCacheRAM()
cleanCompleteRAM()
showMessage()