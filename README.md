# ibm_datascience_capstone

In this capstone project the problem is to predict if the Falcon 9 first stage will land successfully. A Falcon first stage booster is a reusable rocket booster used on a Falcon9 and Falcon Heavy orbital launch vehicles manufactured. (https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters ).    

### Example of a successful landing             
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing\_1.gif)

### Examples of failures          
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)           

SpaceX has gained worldwide attention for a series of historic milestones. It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.            
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch. The historical data used in this capstone had information about the rocket, the payload, the payload’s mass, the launch and the landing. In other words, information about previous attempts to reuse the first stage and how successful those attempts have been.       

1.  Can we determine if the first stage will land? 
1.	What are the variables that have most impact on the landing success rate? 


## METHODOLOGY
### DATA COLLECTION

Historical data was collected from SpaceX REST API and web scraped from Wikipedia. The data has information about the rocket, the payload carried into outer space (people, cargo), the launch and landing. The data was stored into a csv. 

### EDA (EXPLORATORY DATA ANALYSIS)
To be able to make predictions, the status of the first stage, was converted into Training Labels. A PostgeSQL database was created, the raw data inserted into the database and SQL queries were performed to get information about the dataset. The csv data was also plotted visually with pandas and matplotlib to gain more preliminary insights.         

### VISUAL ANALYTICS
Spatial insights were gained with a Folium map. The previously classified training labels were used to pin colored markers on a map. Green for success and red for failure. Distances from nearest highway, city and coastline were calculated to gain understanding on the site locations.            
An interactive Dash Plotly dashboard was built to play around with different figures. A pie chart was created to show relative proportions of successful landings on sites. A scatter graph was also built to show the relationship between the successful landing and payload mass for booster versions. The scattergraph could be filtered with maximum and minimum payload mass. 

### PREDICTIONS 
The datasets created at the data collection and EDA phases were used to build a dataset which was then split into training and test sets. Training data was used to build a logistic regression model,  a support vector machine object, a decision tree classifier and a k nearest neighbours object. The test data was used to calculate accuracy for each model and visualize a confusion matrix. Finally the best performing method, the decision tree classification, was found based on the parameters. The model can be improved by tuning the algorithm or feature engineering. 

# CONCLUSIONS 

1. The best method for predicting the landing is the Tree classifier 
1. The launches success rate increases over time 
1. KSC LC-39A is the most successful site point 
1. Low payload mass increases the success rate 
1. Orbits GEO, SSO, ES-L1 and HEO increase the success rate
