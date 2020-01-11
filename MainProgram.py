import addmodule
print(addmodule.add(10,20))
print(addmodule.msg)
#Two ways to add module. First is setting the env variale. Env VAr Name='PYTHONPATH' value: Path of lib
#Second Way
import sys
print(sys.path)
#sys.path.append(r'C:\Users\lab365\Desktop\PythonTraining\lib')

import addmodule as a
print(a.msg)
print(a.add(10,20))

from addmodule import msg,add
print(add(10,20))
print(msg)

from addmodule import msg as m,add as a
print(m)
print(a(10,20))

from addmodule import *
print(msg)
print(add(20,30))

import Project.net.addmodule
print(Project.net.addmodule.msg)

import Project.net.addmodule as a
print(a.msg)

from Project.net.addmodule import msg,add
print(msg)
print(add(10,70))

