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
      
      -             !!(Because the scope of the words that are being used is negligible and low, I saw the origin of the things and therefore I set a threshold of risk and                           criminalization that is relatively low.)
    
                 
                  
                   
 - ## utillities--  
     - **elastic** -Used for easy and convenient data storage as well as crazy search capabilities
     - **kafka** -Used for data traffic, sending by topic and distributing in an orderly and easy manner
     - 






