import os

# путь к папке с файлами
folder_path = r"C:\Users\a553x\PycharmProjects\thirdLab\static\Якудза_files"

# список файлов, которые нужно переименовать
files = [os.path.join(folder_path, "medium.png")] + [os.path.join(folder_path, f"medium_{i:03}.png") for i in range(2, 26)]

# список новых имен файлов
new_names = [os.path.join(folder_path, f"medium_{i:03}.png") for i in range(26, 51)]

# переименование файлов
for old_name, new_name in zip(files, new_names):
    os.rename(old_name, new_name)