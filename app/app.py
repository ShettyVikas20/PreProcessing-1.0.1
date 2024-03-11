from customtkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox,ttk
import pandas as pd



app = CTk()

app.geometry("1510x880")
set_appearance_mode('light')
app.title('ML')
app.pack_propagate(False)
app.resizable(0,0)



frame1 = tk.LabelFrame(app,text="Data",height=300,width=400 )
command_frame = tk.LabelFrame(app,text="Commands")
encoder_frame = tk.LabelFrame(app,text="Encoders",height=400,width=200)
file_frame = tk.LabelFrame(app,text="File Management",height=100,width=400)



def do_layout():
    frame1.pack(side="left", fill="both", expand=True)
    encoder_frame.pack(side="top", fill="both", expand=True)
    file_frame.pack(side="bottom", fill="both", expand=True)
    return None


do_layout()

#buttons at File Management
browse_button = tk.Button(file_frame,text="Browse The File",command=lambda: File_dialog())
browse_button.place(relx=0.10,rely=0.40)


loadfile_button = tk.Button(file_frame,text="   Load File   ",command=lambda:Load_csv_data())
loadfile_button.place(relx=0.10,rely=0.60)


lable_file=ttk.Label(file_frame,text="[-]No File Selected")
lable_file.place(relx=0.10,rely=0.10)







tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1,relwidth=1)


treescrolly = tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
treescrollx = tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")

def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/home/tamil/Documents/",
                                          title="Select A File",
                                          filetypes=(("csv files","*.csv"),("All Files","*.*")))
    lable_file["text"] = f"{filename}"
    return None

def Load_csv_data():
    file_path = lable_file["text"]
    try:
        csv_filename = r"{}".format(file_path)
        df = pd.read_csv(csv_filename)
    except ValueError:
        tk.messagebox.showerror("Information","The file you have choosen is Invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No Such file as {file_path}")
        return None
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)
    
    return None
    

def clear_data():
    tv1.delete(*tv1.get_children())







app.mainloop()











