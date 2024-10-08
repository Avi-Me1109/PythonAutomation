from tkinter import *
import download

root = Tk()
root.title("File Cleaner")
#root.geometry("500x500")
# Configure rows to grow dynamically
root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

EnterL = Label(root, text="Enter Location: ", font=("Arial", 10))
EnterL.grid(row=0, column=0)

start = Entry(root, width=30)
start.grid(row=0, column=1)


def entryclicked():
    root.update_idletasks()
    if len(extensionLabels) == 0:
        ExtensionL = Label(root, text="Files: ", font=("Arial", 10))
        ExtensionL.grid(row=EnterL.grid_info()['row'] + 1, column=0)
        extensionLabels.append(ExtensionL)
        DestinationL = Label(root, text="Enter Destination: ", font=("Arial", 10))
        DestinationL.grid(row=ExtensionL.grid_info()['row'] + 1, column=0)
        destinationLabels.append(DestinationL)


        extension = Entry(root, width=40)
        extension.grid(row=ExtensionL.grid_info()['row'], column=1)
        extensionEntries.append(extension)
        end = Entry(root, width=40)
        end.grid(row=DestinationL.grid_info()['row'], column=1)
        destinationEntries.append(end)

        root.update_idletasks()
    
    else:
        ExtensionL = Label(root, text="Files: ", font=("Arial", 10))
        ExtensionL.grid(row=destinationLabels[len(destinationLabels) - 1].grid_info()['row'] + 1, column=0)
        extensionLabels.append(ExtensionL)
        DestinationL = Label(root, text="Enter Destination: ", font=("Arial", 10))
        DestinationL.grid(row=ExtensionL.grid_info()['row'] + 1, column=0)
        destinationLabels.append(DestinationL)

        extension = Entry(root, width=40)
        extension.grid(row=extensionLabels[len(extensionLabels) - 1].grid_info()['row'], column=1)
        extensionEntries.append(extension)
        end = Entry(root, width=40)
        end.grid(row=DestinationL.grid_info()['row'], column=1)
        destinationEntries.append(end)

        root.update_idletasks()
    root.update_idletasks()
    
extensionLabels = []
destinationLabels = []

extensionEntries = []
destinationEntries = []


directory = ""
end_directory = ""

def mainclicked():
    download.files.clear()
    directory = start.get()
    for i in range(len(extensionEntries)):
        extension = extensionEntries[i].get()
        end = destinationEntries[i].get()
        download.find_files(directory)
        res = download.move_files(end, extension)

        if res != "":
            print("Error moving file: " + extension)
            openPopup("File Exists: " + res)
            break

        else:
            print("Moved file: " + extension)
            openPopup("Successful!")

def deleteclicked():
    download.files.clear()
    directory = start.get()
    for i in range(len(extensionEntries)):
        ex = extensionEntries[i].get()
        download.find_files(directory)
        download.delete_files(ex)

def entryDelete():
    if(len(extensionLabels) > 0):
        extensionLabels[len(extensionLabels) - 1].destroy()
        destinationLabels[len(destinationLabels) - 1].destroy()
        extensionEntries[len(extensionEntries) - 1].destroy()
        destinationEntries[len(destinationEntries) - 1].destroy()
        extensionLabels.pop()
        destinationLabels.pop()
        extensionEntries.pop()
        destinationEntries.pop()
        root.update_idletasks()

def openPopup(label):
    popup = Toplevel(root)
    popup.title("Error")
    ErrorLabel = Label(popup, text=label, font=("Arial", 10))
    ErrorLabel.pack()

    Button(popup, text="Okay", command=popup.destroy).pack()
    

btn = Button(root, text="MOVE", command=mainclicked)
btn.grid(row=0, column=3) 

btn2 = Button(root, text="ADD", command=entryclicked)
btn2.grid(row=0, column=4)

btn3 = Button(root, text="DELETE", command=deleteclicked)
btn3.grid(row=0, column=5)

btn4 = Button(root, text="DELETE ENTRY", command=entryDelete)
btn4.grid(row=0, column=6)

root.mainloop()