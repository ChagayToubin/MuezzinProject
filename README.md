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
     [ [  http://127.0.0.1:5601/app/lens?_g=%28filters%3A%21%28%28%27%24state%27%3A%28store%3AappState%29%2Cmeta%3A%28alias%3Amap%2Cdisabled%3A%21f%2Cfield%3Abds_threat_level%2Cindex%3A%278ef70a76-d3b1-44c0-ae62-199951f7dba4%27%2Ckey%3Abds_threat_level%2Cnegate%3A%21f%2Ctype%3Aexists%2Cvalue%3Aexists%29%2Cquery%3A%28exists%3A%28field%3Abds_threat_level%29%29%29%29%2Ctime%3A%28from%3Anow-15m%2Cto%3Anow%29%29#/?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))](http://127.0.0.1:5601/app/dashboards#/create?_g=(refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))&_a=(panels:!((embeddableConfig:(attributes:(description:'',references:!((id:'8ef70a76-d3b1-44c0-ae62-199951f7dba4',name:indexpattern-datasource-layer-845efff9-e2bc-49ce-afc3-6701a0843e42,type:index-pattern),(id:'8ef70a76-d3b1-44c0-ae62-199951f7dba4',name:ffab88fa-db90-4c57-b97c-f96ecf2d9a93,type:index-pattern)),state:(adHocDataViews:(),datasourceStates:(formBased:(layers:('845efff9-e2bc-49ce-afc3-6701a0843e42':(columnOrder:!(e606e12f-0120-4e98-a8c9-a16540922390,'33897f96-f41e-4ec8-908c-a16faf301af0'),columns:('33897f96-f41e-4ec8-908c-a16faf301af0':(dataType:number,isBucketed:!f,label:'Count%20of%20records',operationType:count,params:(emptyAsNull:!t),scale:ratio,sourceField:___records___),e606e12f-0120-4e98-a8c9-a16540922390:(dataType:string,isBucketed:!t,label:'Top%205%20values%20of%20bds_threat_level.keyword',operationType:terms,params:(exclude:!(),excludeIsRegex:!f,include:!(),includeIsRegex:!f,missingBucket:!f,orderBy:(columnId:'33897f96-f41e-4ec8-908c-a16faf301af0',type:column),orderDirection:desc,otherBucket:!t,parentFormat:(id:terms),size:5),scale:ordinal,sourceField:bds_threat_level.keyword)),incompleteColumns:(),sampling:1))),indexpattern:(layers:()),textBased:(layers:())),filters:!(('$state':(store:appState),meta:(alias:map,disabled:!f,field:bds_threat_level,index:ffab88fa-db90-4c57-b97c-f96ecf2d9a93,key:bds_threat_level,negate:!f,type:exists,value:exists),query:(exists:(field:bds_threat_level)))),internalReferences:!(),query:(language:kuery,query:''),visualization:(axisTitlesVisibilitySettings:(x:!t,yLeft:!t,yRight:!t),fittingFunction:None,gridlinesVisibilitySettings:(x:!t,yLeft:!t,yRight:!t),labelsOrientation:(x:0,yLeft:0,yRight:0),layers:!((accessors:!('33897f96-f41e-4ec8-908c-a16faf301af0'),colorMapping:(assignments:!(),colorMode:(type:categorical),paletteId:eui_amsterdam_color_blind,specialAssignments:!((color:(type:loop),rule:(type:other),touched:!f))),layerId:'845efff9-e2bc-49ce-afc3-6701a0843e42',layerType:data,seriesType:bar_stacked,xAccessor:e606e12f-0120-4e98-a8c9-a16540922390)),legend:(isVisible:!t,position:right),preferredSeriesType:bar_stacked,tickLabelsVisibilitySettings:(x:!t,yLeft:!t,yRight:!t),valueLabels:hide)),title:'count%20risk%20level',type:lens,visualizationType:lnsXY)),gridData:(h:15,i:'5ef6e0fb-2726-42f0-915b-b471ae82d14e',w:24,x:0,y:0),panelIndex:'5ef6e0fb-2726-42f0-915b-b471ae82d14e',type:lens)))))](http://127.0.0.1:5601/app/dashboards#/view/7e80fe16-c10e-4032-ae73-2886a6d23cfa?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now)))
       
     - **kafka** -Used for data traffic, sending by topic and distributing in an orderly and easy manner
     - 






