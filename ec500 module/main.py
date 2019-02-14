from urllib3.connectionpool import xrange

from inputModule import inputApi
from checkModule import Analyzer
import outputModule
from datetime import datetime as dt
import threading
import time

# def main():
#     ##user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time
#     data = {}
#     ##user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time
#
#     for index, line in enumerate(file):
#         words = line.split( )
#         data[index] = inputApi(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], dt.now()).dic
#
#     for key in data.keys():
#         userID = data[key]["user_id"]
#         gender = data[key]["gender"]
#         age = data[key]["age"]
#         outputModule.print_title(userID, gender, age)
#         ##Systolic_BP, Diastolic_BP, Heart_Rate, Heart_Oxygen_Level, Body_temp
#         res = Analyzer(data[key]["Systolic_BP"], data[key]["Diastolic_BP"], data[key]["heartrate"], data[key]["blood_oxygen"], data[key]["temperature"])
#             ##Heart_Rate, Body_temp
#         signal_Loss = res.Signal_Loss(data[key]["heartrate"], data[key]["temperature"])
#             ##Heart_Rate, Body_temp
#         shock_Alert = res.Shock_Alert(data[key]["heartrate"], data[key]["temperature"])
#         ##Heart_Oxygen_Level
#         oxygen_Supply = res.Oxygen_Supply(data[key]["blood_oxygen"])
#         ##Body_temp
#         fever = res.Fever(data[key]["temperature"])
#         ##Systolic_BP, Diastolic_BP
#         hypotension = res.Hypotension(data[key]["Systolic_BP"], data[key]["Diastolic_BP"])
#         ##Systolic_BP, Diastolic_BP
#         hypertension = res.Hypertension(data[key]["Systolic_BP"], data[key]["Diastolic_BP"])
#         ##print patient basic data
#         outputModule.print_patient_data(data[key]['Systolic_BP'], data[key]['Diastolic_BP'], \
#                                         data[key]['heartrate'], data[key]['blood_oxygen'], data[key]['temperature'])
#         ##print alert
#         outputModule.print_system_or_body_alert(signal_Loss, shock_Alert, oxygen_Supply, fever, hypotension, hypertension)
#
# if __name__ == '__main__':
#     main()

import threading
import time
import sys

def action(arg):
    lock.acquire()
    time.sleep(1)
    sys.stdout.flush()
    print('the arg is:%s\r' %arg)
    print('Hello')
    lock.release()

lock = threading.Lock()

for i in xrange(10):
    t = threading.Thread(target=action, args=(i,))
    t.start()