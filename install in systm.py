import os ,sys

try:
    import flet
except ImportError:
    os.system(f"{sys.executable} -m pip install flet")
    os.execv(sys.executable,[sys.executable]+ sys.argv)
print('programe is run')