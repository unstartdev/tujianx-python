# -*- coding: UTF-8 -*-
import os
import sys
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def stop_program():
    sys.exit(0)