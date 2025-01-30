import cx_Freeze  # pip install cx_freeze
        
# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('main.py', base="Win32GUI")]
excludes = []

cx_Freeze.setup(
    name="meditation",
    options={"build_exe":
                 {'include_msvcr': True,
                  "packages": ["Pygame", "random"], # прописываем все зависимости проекта
                  "zip_include_packages": ["Pygame", "random"],
                  "include_files": [".gitignore", "README.md", "main.py", "__pycache__",
                                    "data/", "img_balloon.png", "balloon2.png", "balloon3.png", "balloon4.png", "balloon5.png", "balloon6.png", "setup.py"
                                    "balloon7.png", "balloon8.png", "img_cloud.png", "img_heart.png", "image_func.py", "points_score.txt", "requirements.txt",
                                    "sprites/", "balloon.py", "cloud.py", "heart.py"], # папки, документы
                  "excludes": excludes}},
    executables=executables
)