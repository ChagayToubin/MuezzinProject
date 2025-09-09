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

## Services
- **read_meta_data** – Pulls the data and extracts all the data on it and sends it in a container.
- **Preprocessor** – cleans the text (remove symbols, lowercase, stop words, etc.) and publishes it back.  
- **Enricher** – adds more features like sentiment, weapons detection, and dates.  
- **Persister** – saves everything into the local MongoDB (two collections: antisemitic and not antisemitic).  
- **DataRetrieval** – simple API to return the data.





