import pyperclip
import datetime

pyperclip.copy('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' GMT')




