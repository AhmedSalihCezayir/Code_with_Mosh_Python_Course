from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink() # To delete

# Creation time of this file
print(ctime(path.stat().st_ctime))

# All these methods take care of opening and closing of the files
# path.read_bytes()
# print(path.read_text())
# path.write_text("pass")
# path.write_bytes()

# To copy data from one file to another
target = Path() / "__init__.py"
# target.write_text(path.read_text())
shutil.copy(path, target)
