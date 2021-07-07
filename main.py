import ctypes
import os
from PyQt5.QtCore import *

p = QProcess()
env = QProcessEnvironment.systemEnvironment()
env.insert("TEST", "TEST_NAME")
p.setProcessEnvironment(env)
p.start()

# 2 вариант через os (тоже не работат)
# os.environ["TEST"] = "TEST_NAME"

lib = ctypes.cdll.LoadLibrary(os.path.join(os.getcwd(),"libtest.dll"))
lib.print_getenv()
