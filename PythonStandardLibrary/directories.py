from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# This method returns a generator object and by using it we can iterate over it.
# This loop method returns both files and directories
for p in path.iterdir():
    print(p)

# We can use list comprehension to create a list of paths. However, these list elements will be WindowsPath objects
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# The glob() method lets us find directories with a pattern.
# We can also use rglob() method to recursively find file/directory paths.
py_files = [p for p in path.glob("*.py")]
print(py_files)
