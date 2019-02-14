## Design Architecture:

<img align = center src = "https://github.com/leonshen95/EC500/blob/master/EC500%20diagram%201.jpg?raw=true">
My data pipeline is: input --> check --> immediate output.  
I use random number to make 10 threads in a thread pool and let each thread select one random patient to detect and print it information out. Also, I make 10 threads sleep 1 second so that they can run concurrently.

## Outcome Display:
Run MultiThread.py and the data directory is PatientInformation, which has ten patient information.

      The thread is:0
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-005
      Age:  18
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 21:56:12.291830
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  121
      Heart Rate:  65
      Heart Oxygen Level 80
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 21:56:12.292021
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:1
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-0010
      Age:  22
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 21:56:13.297296
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  120
      Heart Rate:  65
      Heart Oxygen Level 85
      Body Temperature:  36.3
      **Body Alert**
      Time:  2019-02-13 21:56:13.297471
      Signal Loss condition:  False
      Shock Alert condition:  False
      Oxygen Supply condition:  False
      Fever condition False
      Blood Pressure condition:  True
      
      The thread is:2
      Welcome to the Patient Montitoring System
      ********************************************
      Patient ID:  patient-002
      Age:  22
      Gender: female
      ********************************************
      **Body Condition**
      Time:  2019-02-13 21:56:14.301908
      Systolic Blood Pressure:  95
      Diastolic Blood Pressure:  600
      Heart Rate:  65
      Heart Oxygen Level 90
      Body Temperature:  36.5
      **Body Alert**
      Time:  2019-02-13 21:56:14.302083
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
