import os
import shutil

# pasta_downloads = __file__.replace(r"Desenvolvimento\Projetos\.venv\src\main.py","Downloads")

folder_downloads = r"C:\Users\RN\Downloads"

for file in os.listdir(folder_downloads):
    file_name, file_extension = os.path.splitext(file)

    folder_organizacao = f"{folder_downloads}/{file_extension[1:]}"
    
    if not os.path.isdir(folder_organizacao):
        os.mkdir(folder_organizacao)
    shutil.move(f"{folder_downloads}/{file}",f"{folder_organizacao}/{file}")
    
