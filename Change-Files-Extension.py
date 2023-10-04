import tkinter as tk

class Window:

    def __init__(self, appName, lableInputName, labelInputExtension, labelOutputExtension):
    
        self = tk.Tk()
        self.title(appName)
        self.geometry("400x300")

        inputLabel = tk.Label(self, text=lableInputName)
        inputLabel.pack()

        operationPath = tk.Entry(self)
        operationPath.pack()

        inputExtensionLabel = tk.Label(self, text=labelInputExtension)
        inputExtensionLabel.pack()
        
        inputExtension = tk.Entry(self)
        inputExtension.pack()
        
        outputExtensionLabel = tk.Label(self, text=labelOutputExtension)
        outputExtensionLabel.pack()
        
        outputExtension = tk.Entry(self)
        outputExtension.pack()

        #submit_button = tk.Button(text="Submit", command=on_submit)
        #submit_button.pack()

        self.mainloop()

# Variables to change name of labels

appName = "Change extension of files"

lableInputName = "Folder with input files:"

labelInputExtension = "Input Extension"

labelOutputExtension="Output Extension"

###############################            
w = Window(appName, lableInputName, labelInputExtension, labelOutputExtension)