import os
import instaloader
import shutil
import time
import tkinter as tk
from tkinter import messagebox

def download_media(username, download_videos, base_folder):
    
    L = instaloader.Instaloader()

    
    profile = instaloader.Profile.from_username(L.context, username)

    
    user_folder = os.path.join(base_folder, username)
    os.makedirs(user_folder, exist_ok=True)

    
    L.download_profile(username, profile_pic=False)

    
    time.sleep(5)

    
    photos_folder = os.path.join(user_folder, 'fotos')
    os.makedirs(photos_folder, exist_ok=True)
    for file_name in os.listdir(user_folder):
        if file_name.endswith('.jpg'):
            shutil.move(os.path.join(user_folder, file_name), os.path.join(photos_folder, file_name))

    
    videos_folder = os.path.join(user_folder, 'vídeos')
    os.makedirs(videos_folder, exist_ok=True)
    for file_name in os.listdir(user_folder):
        if file_name.endswith('.mp4'):
            shutil.move(os.path.join(user_folder, file_name), os.path.join(videos_folder, file_name))

    
    txt_folder = os.path.join(user_folder, 'arquivos_txt')
    os.makedirs(txt_folder, exist_ok=True)
    for file_name in os.listdir(user_folder):
        if file_name.endswith('.txt'):
            shutil.move(os.path.join(user_folder, file_name), os.path.join(txt_folder, file_name))

    
    json_folder = os.path.join(user_folder, 'arquivos_json')
    os.makedirs(json_folder, exist_ok=True)
    for file_name in os.listdir(user_folder):
        if file_name.endswith('.xz'):
            shutil.move(os.path.join(user_folder, file_name), os.path.join(json_folder, file_name))

    print("Download concluído!")

def main():
    root = tk.Tk()
    root.title("Instagram Media Downloader")

    
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    
    username_label = tk.Label(frame, text="Nome de usuário:")
    username_label.pack(side=tk.LEFT)
    username_entry = tk.Entry(frame)
    username_entry.pack(side=tk.LEFT)

    
    download_videos_var = tk.BooleanVar()
    download_videos_check = tk.Checkbutton(frame, text="Baixar vídeos", variable=download_videos_var)
    download_videos_check.pack(side=tk.LEFT)

    
    def on_download_click():
        username = username_entry.get()
        download_videos = download_videos_var.get()
        base_folder = os.getcwd()
        download_media(username, download_videos, base_folder)
        messagebox.showinfo("Sucesso", "Download concluído!")

    
    download_button = tk.Button(root, text="Baixar", command=on_download_click)
    download_button.pack(pady=10)

    
    root.mainloop()

if __name__ == "__main__":
    main()
