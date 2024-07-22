import os
class Admin:
    def __enter__(self):
        self._current_user_ = os.environ["USER"]
        os.environ["USER"] = "admin"
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        os.environ["USER"] = self._current_user_


os.environ["USER"] = "regular_user"
print(os.environ["USER"])
with Admin():
   print(os.environ["USER"])
   #pozovi neke sistemske stvari sa admin pravima
print(os.environ["USER"])
   