import os
class Fajl:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()
            


with Fajl("kontekst_menadzer.py") as f:
    print(f.readline())
   