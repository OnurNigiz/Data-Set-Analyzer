# Data-Set-Analyzer
### A simple analyzer for statistic class in ITU.

* Create a data set with "data-set-creator.py", the code will give you a txt file that is named as "big-data.txt", which has the created datas. You can change the size of the set if you play with the codes (default size: 100 values). To do this, follow the comment lines!
* Run "run.py". You will receive some informations about the data-set like max./min. number, avarage, mode, median etc.

#### Notes:
* First you have to run the "data-set-creator.py" file. Otherwise you will get an error like ".txt file does not exist". After the first run, the file won't go anywhere if you don't delete it, but will change for every "data-set-creator.py" run.
* "create_sqldatabase.py" is used to fetch data from txt and write it to database. (It must have sqlite on the computer for it to run smoothly!)
* When the program is run for the first time, a file named "database.sqlite" will be created. If the dataset changes, the database will be automatically updated on subsequent runs.

