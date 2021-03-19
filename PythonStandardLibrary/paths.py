from pathlib import Path

Path("C:\\Program Files\\Microsoft")

# Raw String ('\' is not an escape character)
Path(r"C:\Program Files\Microsoft")
Path()
Path() / Path("ecommerce")
Path() / "ecommerce" / "__init__.py"
Path.home()

path = Path("ecommerce/__init__.py")
print(path.exists())
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# We are not renaming the file, we are just representing it
path = path.with_name("file.txt")
print(path)
print(path.absolute())
path = path.with_suffix(".txt")
print(path)
