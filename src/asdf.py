import os

def draw_folder_structure(root_folder, indent=""):
    print(f"{indent}|--{os.path.basename(root_folder)}")

    if os.path.isdir(root_folder):
        files = os.listdir(root_folder)
        for file in files:
            path = os.path.join(root_folder, file)
            if os.path.isdir(path):
                draw_folder_structure(path, indent + "   |")
            else:
                print(f"{indent}   |--{file}")

if __name__ == '__main__':
  draw_folder_structure("C:\Users\1234\Desktop\Git(ell)\000-Private\pythonStudy\src")

