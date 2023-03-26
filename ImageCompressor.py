import tkinter as tk
from tkinter import filedialog
import cv2
import os

class ImageCompressorGUI:
    def __init__(main, master):
        main.master = master
        main.input_folder_path = tk.StringVar()
        main.output_folder_path = tk.StringVar()
        main.quality = tk.StringVar(value="70")
        main.master.title("Image Compressor GUI")
        window.resizable(False,False)
        window.configure(bg='black')
        
        input_label = tk.Label(master, 
                               font=('Consolas light', '10'),
                               text="Input Folder:",
                               bg='black',
                               fg='white')
        
        input_button = tk.Button(master, 
                                 text="Browse", 
                                 bg='#efc8ff',
                                 command=main.browse_input_folder)
        
        main.input_folder_entry = tk.Entry(master, 
                                           bg='black', 
                                           fg='#f0cdff',
                                           font=('Consolas light', '10'), 
                                           textvariable=main.input_folder_path, 
                                           width=30)
        
        output_label = tk.Label(master, 
                                bg='black',
                                fg='white',
                                font=('Consolas light', '10'),
                                text="Output Folder:")
        
        main.output_folder_entry = tk.Entry(master, 
                                            textvariable=main.output_folder_path,
                                            font=('Consolas light', '10'),
                                            bg='black',
                                            fg='#f0cdff',
                                            width=30)
        
        output_button = tk.Button(master, 
                                  text="Browse",
                                  bg='#efc8ff', 
                                  command=main.browse_output_folder)
        
        quality_label = tk.Label(master, 
                                 bg='black',
                                 fg='white',
                                 font=('Consolas light', '10'),
                                 text="Compression Quality (0-100):")
        
        main.quality_entry = tk.Entry(master, 
                                      bg='black',
                                      fg='magenta',
                                      textvariable=main.quality, 
                                      width=35)
        
        compress_button = tk.Button(master, 
                                    text="Compress Images", 
                                    bg='#9c2bcc', 
                                    fg='white', 
                                    command=main.compress_images)
       
        owner_label = tk.Label(window, 
                               text="@fxrdhan_", 
                               font=('arial', '10'),                                 
                               fg="#2abcff", 
                               bg="black")
        
        owner_label.place(relx=0, 
                          rely=1, 
                          anchor="sw")
        
        input_label.grid(row=0, 
                         column=0, 
                         padx=5, 
                         pady=5)
        
        input_button.grid(row=0, 
                          column=2, 
                          padx=5, 
                          pady=5)
        
        main.input_folder_entry.grid(row=0, 
                                     column=1, 
                                     padx=5, 
                                     pady=5)
        
        output_label.grid(row=1, 
                          column=0, 
                          padx=5, 
                          pady=5)
        
        main.output_folder_entry.grid(row=1, 
                                      column=1, 
                                      padx=5, 
                                      pady=5)
        
        output_button.grid(row=1, 
                           column=2, 
                           padx=5, 
                           pady=5)
        
        quality_label.grid(row=2, 
                           column=0, 
                           padx=5, 
                           pady=5)
        
        main.quality_entry.grid(row=2, 
                                column=1, 
                                padx=5, 
                                pady=5)
        
        compress_button.grid(row=3, 
                             column=1, 
                             padx=5, 
                             pady=5)
        
    def browse_input_folder(self):
        folder_path = filedialog.askdirectory()
        self.input_folder_path.set(folder_path)
        
    def browse_output_folder(self):
        folder_path = filedialog.askdirectory()
        self.output_folder_path.set(folder_path)
        
    def compress_images(self):
        input_folder = self.input_folder_path.get()
        output_folder = self.output_folder_path.get()
        quality = int(self.quality.get())
        
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.JPG', '.PNG', '.jpeg', '.JPEG', '.png')):
                image = cv2.imread(os.path.join(input_folder, filename))
                output_filename = os.path.splitext(filename)[0] + '-compress-quality=' + str(quality) + os.path.splitext(filename)[1]
                output_path = os.path.join(output_folder, output_filename)
                
                cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
                
        tk.messagebox.showinfo("Notification", "Image compression complete!")

window = tk.Tk()
app = ImageCompressorGUI(window)
window.mainloop()