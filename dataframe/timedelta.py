from datetime import date 
from datetime import timedelta 
import time
import inspect
 
def line_numb():
   '''Returns the current line number in our program'''
   return inspect.currentframe().f_back.f_lineno 

new_job = "grudge" 
with open("hello.log", "a") as fp:
    fp.write(time.strftime("%Y-%m-%d %I:%M:%S %p") + ',' + str(line_numb()) + ' INFO ' + 'Telegram_Bot '
                            + 'starting bot' + '\n')