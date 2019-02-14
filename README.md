## Design Architecture:

<img align = center src = "https://github.com/leonshen95/EC500/blob/master/EC500%20diagram%201.jpg?raw=true">

My data pipeline is: input --> check --> immediate output.  
I use random number to make 10 threads in a thread pool and let each thread select one random patient to detect and print it information out. Also, I make 10 threads sleep 1 second so that they can run concurrently.

## Outcome Display:
Run MultiThread.py and the data directory is PatientInformation, which has ten patient information.

      The thread is:0
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-009
      Age:  22
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:22.573508
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  120
      Heart Rate:  65
      Heart Oxygen Level 90
      Body Temperature:  38.5
      **Body Alert**
      Time:  2019-02-13 22:16:22.573707
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition True
      Blood Pressure condition:  True
      
      The thread is:1
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-005
      Age:  18
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:23.581066
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  121
      Heart Rate:  65
      Heart Oxygen Level 80
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:23.581239
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:2
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-007
      Age:  15
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:24.588691
      Systolic Blood Pressure:  90
      Diastolic Blood Pressure:  140
      Heart Rate:  70
      Heart Oxygen Level 90
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:24.588866
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:3
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-008
      Age:  23
      Gender: male
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:25.594116
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  400
      Heart Rate:  65
      Heart Oxygen Level 90
      Body Temperature:  38
      **Body Alert**
      Time:  2019-02-13 22:16:25.594173
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition True
      Blood Pressure condition:  True
      
      The thread is:4
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-007
      Age:  15
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:26.601460
      Systolic Blood Pressure:  90
      Diastolic Blood Pressure:  140
      Heart Rate:  70
      Heart Oxygen Level 90
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:26.601631
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:5
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-005
      Age:  18
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:27.606367
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  121
      Heart Rate:  65
      Heart Oxygen Level 80
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:27.606540
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:6
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-005
      Age:  18
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:28.613282
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  121
      Heart Rate:  65
      Heart Oxygen Level 80
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:28.613456
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      The thread is:7


      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-002
      Age:  22
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:29.620812
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  600
      Heart Rate:  65
      Heart Oxygen Level 90
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 22:16:29.620984
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:8
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-001
      Age:  20
      Gender: male
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:30.626516
      Systolic Blood Pressure:  90
      Diastolic Blood Pressure:  120
      Heart Rate:  70
      Heart Oxygen Level 100
      Body Temperature:  37
      **Body Alert**
      Time:  2019-02-13 22:16:30.626690
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:9
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-001
      Age:  20
      Gender: male
      ********************************************
      **Body Condition**
      Time:  2019-02-13 22:16:31.634314
      Systolic Blood Pressure:  90
      Diastolic Blood Pressure:  120
      Heart Rate:  70
      Heart Oxygen Level 100
      Body Temperature:  37
      **Body Alert**
      Time:  2019-02-13 22:16:31.634488
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True

## Pros and cons:
* Pros: This multithread process is thread-safe because I use **lock.acquire( )** and **lock.release( )** and **lock = threading.Lock()** method to make sure that subthread will not block main thread.
* Cons: This multi-threading is more like a queue, if a subthread is finished, then next thread can be excuted. We still want to realize multithread without queuing. That will be a bouns for this project.

## Some attention:
We should install [urllib3.connectionpool](https://urllib3.readthedocs.io/en/1.4/pools.html) to use xrange random method.  
```
# Read random file from PatientInformation directory
file_path = r'/Users/kobale/EC500/PatientInformation'
```
In this code, I import file in my local directory, if you want to run the code, you must change patient information directoty.
