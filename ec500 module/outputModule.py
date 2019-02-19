from datetime import datetime as dt


def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
    ##Boolean Parameters
    ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {'Signal_Loss': False, 'Shock_Alert': False, 'Oxygen_Supply': False, 'Fever': False,
                   'Hypotension': False, 'Hypertension': False}
    if (Singal_Loss is True):
        BasicResult['Signal Loss'] = True
    if (Shock_Alert is True):
        BasicResult['Shock_Alert'] = True
    if (Oxygen_Supply is True):
        BasicResult['Oxygen_Supply'] = True
    if (Fever is True):
        BasicResult['Fever'] = True
    if (Hypotension is True):
        BasicResult['Hypotension'] = True
    if (Hypertension is True):
        BasicResult['Hypertension'] = True

def print_system_or_body_alert(signal_Loss, shock_Alert, oxygen_Supply, fever, hypotension, hypertension):
    print("**Body Alert**")
    print("Time: ", dt.now())
    print('Signal Loss condition: ', signal_Loss)
    print('Shock Alert condition: ', shock_Alert)
    print('Oxygen Supply condition: ', oxygen_Supply)
    print('Fever condition', fever)
    print('Blood Pressure condition: ', hypotension or hypertension)


def print_patient_data(Systolic_BP, Diastolic_BP, Heart_Rate, Oxygen_Supply, Body_temp):
    print("Time: ", dt.now())
    print('Systolic Blood Pressure: ', Systolic_BP)
    print('Diastolic Blood Pressure: ', Diastolic_BP)
    print('Heart Rate: ', Heart_Rate)
    print('Heart Oxygen Level', Oxygen_Supply)
    print('Body Temperature: ', Body_temp)

def print_title(patientID, gender, age):
    print("\n\nWelcome to the Patient Montitoring System")
    print("********************************************")
    print('Patient ID: ', patientID)
    print('Age: ', age)
    print('Gender:', gender)
    print("********************************************")
    print("**Body Condition**")

# def send_basic_input_data(BasicResult, BasicData):
## Receive the result and show it on terminal or web page
#   sentData = analyze(BasicResult)
#   return sentData, BasicData


# def send_AI_input_data(AIResult):
## Receive the result and show it on terminal or web page
#   sentData = analyze(AIResult)
#   return sentData
