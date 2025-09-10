  ### General description:

 The first part takes a folder of files and extracts the information they contain.

The second part takes the information and creates a unique ID, transfers it to Elasticsearch and from there to Monogo.

The Third part Write an external code that checks logs for working and non-working issues and reports the error.

The four part Take the transcription of the file and add it to the data in a neat and clean way.

For a good and beautiful search in a visually pleasing way, you can use the console at this link 

http://127.0.0.1:5601/app/dev_tools#/console


# To run the app

- First, enable metadata reading -(read_meta_data-service)
- Second, enable data reception and sending.-(Receiving_processing_data-service)
- Third, enable data updating. -(update-service)
- Fourth, enable endpoint.-(end poinr-servic)




# Folder structure

## project--
- ## config--
     -  **Setting** - System Settings (Environment Variables)
  
- ## data_file--
     -   **podcasts**- All audio files
  
- ## script--
     - **commend.bat**- All the necessary container installations 

- ## Services--
   -  **read_meta_data** – Pulls the data and extracts all the data on it and sends it in a container.
     
   -  **Receiving_processing_data** – Pulls data from Springboard, performs various processes and then updates to both Mongo and Elastic
      
   -  **update** -Calculates the amount of danger from the text and updates the appropriate fields 
                  Percentage of dangerous words , Determination of criminality ,And degree of risk
                 explain( average percentage of words is 0.30939176841270893, so that would be the threshold for determining criminality or danger level.)
      
      -**end_point** -fast api server that shows me data by risk level
      
      http://127.0.0.1:8000/high_risk
      
      http://127.0.0.1:8000/medium_risk

      http://127.0.0.1:8000/none_risk  


                      

        
    
                 
                  
                   
 - ## utillities--  
     - **elastic** -Used for easy and convenient data storage as well as crazy search capabilities
         (url to kibana visualization:
       http://127.0.0.1:5601/app/dashboards#/view/7e80fe16-c10e-4032-ae73-2886a6d23cfa?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))

     - **kafka** -Used for data traffic, sending by topic and distributing in an orderly and easy manament.
       
  
     - **mongo** -Used to store files
       
     - **decryption** -Used for base 64 encoding
  
     - **logger** -Used to track system logs

     - **transcription** -Transcribes the audio files
  
       
   ## Folder structure
  

- ├───data_files
  │   └───podcasts
  
├───scripts
├───services
│   ├───end_point
│   │   
│   ├───read_meta_data
│   │   
│   ├───Receiving_processing_data
│   
│   ├───update_data

- ├───utilities
  │   ├───decryption
  │   ├───elastic
  │   ├───kafka
  │   │   ├───kafka_consumer
  │   │   ├───kafka_producer
  │   ├───logger
  │   ├───mongo
  │   ├───transcription



     
<img width="860" height="537" alt="img" src="https://github.com/user-attachments/assets/37421db9-4077-4e38-9f37-a79f77a8a724" />






