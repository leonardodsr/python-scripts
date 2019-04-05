import subprocess
import sys
from datetime import datetime

data = datetime.now().strftime("%d-%m-%Y")

name_file = 'Aula-'+ str(data)+'.txt'

subprocess.Popen(['touch',name_file])
subprocess.Popen(['gedit', name_file])