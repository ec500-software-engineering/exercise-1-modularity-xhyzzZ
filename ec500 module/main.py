from inputModule import inputApi
from checkModule import Analyzer
import outputModule

def main():
    ##user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time
    data = {}
    ##user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time
    file = open("inputInformation.txt")
    for index, line in enumerate(file):
        words = line.split( )
        data[index] = inputApi(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8]).dic

    for key in data.keys():
        ##Systolic_BP, Diastolic_BP, Heart_Rate, Heart_Oxygen_Level, Body_temp
        res = Analyzer(data[key]["Systolic_BP"], data[key]["Diastolic_BP"], data[key]["heartrate"], data[key]["blood_oxygen"], data[key]["temperature"])
            ##Heart_Rate, Body_temp
        signal_Loss = res.Signal_Loss(data[key]["heartrate"], data[key]["temperature"])
            ##Heart_Rate, Body_temp
        shock_Alert = res.Shock_Alert(data[key]["heartrate"], data[key]["temperature"])
        ##Heart_Oxygen_Level
        oxygen_Supply = res.Oxygen_Supply(data[key]["blood_oxygen"])
        ##Body_temp
        fever = res.Fever(data[key]["temperature"])
        ##Systolic_BP, Diastolic_BP
        hypotension = res.Hypotension(data[key]["Systolic_BP"], data[key]["Diastolic_BP"])
        ##Systolic_BP, Diastolic_BP
        hypertension = res.Hypertension(data[key]["Systolic_BP"], data[key]["Diastolic_BP"])
        ##Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension
        output = outputModule.receive_basic_iuput_data(signal_Loss, shock_Alert, oxygen_Supply, fever, hypotension, hypertension)
        for alert in output.keys():
            print(data[key]["user_id"] + " " + alert + ":" + " " + (str)(output[alert]))

if __name__ == '__main__':
    main()