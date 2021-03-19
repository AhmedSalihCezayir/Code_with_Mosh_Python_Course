# Module is a file that contains some Python code.
# We name the modules like variables (by using lowercase and '_')

# We can import specific objects from this module
# from sales import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

# We can import the entire module as an object
# import sales
# sales.calc_shipping()

# ----------------------------------------------------------------------------------------------

# If we add __init__.py to ecommerce directory, Python treats this directory as a package.
# A package is a container for one or more modules.
# A package is mapped to a directory and a module is mapped to a file.

# import ecommerce.sales
# ecommerce.sales.calc_shipping()

# from ecommerce.sales import calc_shipping(), calc_tax()
# calc_tax()

# from ecommerce import sales
# sales.calc_tax()

# ----------------------------------------------------------------------------------------------

# To create a sub-package, we can repeat the same process. However, do not forget to add the
# __init__.py to make the directory a package.
# from ecommerce.shopping import sales

# ----------------------------------------------------------------------------------------------

# In the sales module:
# This is absolute import (Generally use this/PEP8 recom.)
# from ecommerce.customer import contact
# contact.contact_customer()

# This is relative import (Use this if the import is getting messy)
# from ..customer import contact

# ----------------------------------------------------------------------------------------------

from ecommerce.shopping import sales

# This method returns all the attributes and methods of an object
print(dir(sales))

# These methods returns the module/package/file names of an object
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
