  ### General description:

 The first part takes a folder of files and extracts the information they contain.

The second part takes the information and creates a unique ID, transfers it to Elasticsearch and from there to Monogo.

The Third part Write an external code that checks logs for working and non-working issues and reports the error.

The four part Take the transcription of the file and add it to the data in a neat and clean way.

For a good and beautiful search in a visually pleasing way, you can use the console at this link http://127.0.0.1:5601/app/dev_tools#/console

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
                      

        **explain**(The average percentage of words is 0.30939176841270893, so that would be the threshold for determining criminality or danger level.)
    
                 
                  
                   
 - ## utillities--  
     - **elastic** -Used for easy and convenient data storage as well as crazy search capabilities
         (url to kibana visualization:
        http://127.0.0.1:5601/app/lens?_g=%28filters%3A%21%28%28%27%24state%27%3A%28store%3AappState%29%2Cmeta%3A%28alias%3Amap%2Cdisabled%3A%21f%2Cfield%3Abds_threat_level%2Cindex%3A%278ef70a76-d3b1-44c0-ae62-199951f7dba4%27%2Ckey%3Abds_threat_level%2Cnegate%3A%21f%2Ctype%3Aexists%2Cvalue%3Aexists%29%2Cquery%3A%28exists%3A%28field%3Abds_threat_level%29%29%29%29%2Ctime%3A%28from%3Anow-15m%2Cto%3Anow%29%29#/?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now)))
       
     - **kafka** -Used for data traffic, sending by topic and distributing in an orderly and easy manner
     - 






