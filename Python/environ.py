import os

#border = "#"
#if "BORDER" in os.environ:
#    border = os.environ["BORDER"]

border = os.environ.get("BORDER", "0")

print(border)