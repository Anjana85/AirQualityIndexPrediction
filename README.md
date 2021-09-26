# AirQualityIndexPrediction (Machine Learning App with Flask)
![AirQualityUnderStanding](https://user-images.githubusercontent.com/53623131/134787469-0a0ab7e4-83aa-496a-880a-e24fc93bfa64.png)
![air-quality-index-with-color-scales-showing-from-good-harzardous_1308-41131](https://user-images.githubusercontent.com/53623131/134787842-516c72c7-9cfe-4bc6-bae9-3949509fc371.jpg)


App to predict AirQuality for given climate condition. It is a Machine Learning App with Flask.
(I Followed the whole life cycle of DataScience Project)


  1. Collect Data: I used webscraping to collect data(climate data from 2013-2015) from 
     the website https://en.tutiempo.net/ . And then I have created HTML file for Each month.

  2. Data Processing: Data was taken from Krish Naik's project as it was from a paid API.
     Reference: https://github.com/krishnaik06/AQI-Project/tree/master/Data/AQI.
     This data containes hourly measurements of AQI.
     This data was converted into a dictionary format where the dictionary key is the year and values are the daily AQI values.
     Then, the data in step1 were combined to create a new CSV file. 
  
  3. Cleaning the Data: A new CSV file is created by removing the Null values and improper data.

  4. Feature Engineering and Model Creation:
     Used various Machine Learning Algorithms like Linear Regression, Lasso and Ridge Regression, 
     Decision Tree Regressor, KNN Regressor, Random Forest Regressor, XGBoost Regressor.
     Random Forest gave best performance. 
     Finally, I used RandomForest to perform predictions.
  5. Deployment of the Model: I used Heroku platform to deploy the model.
     Enter various climate details and then click the Predict button to get the Air Quality Index.
     
## Demo
   Demo: (https://airuqalityindexprediction.herokuapp.com/ )
![Screenshot ](https://user-images.githubusercontent.com/53623131/134787897-042c0e5e-148e-4ef0-98b3-af02b7caa7e1.png)

     
     
     

  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Wikipedia](https://en.wikipedia.org/wiki/Air_quality_index)
 - [Data from Krish Naik's project](https://github.com/krishnaik06/AQI-Project/tree/master/Data/AQI)
-  [Importance of AirQuality](https://www.oxygenconcentratorstore.com/blog/the-air-quality-index-why-is-it-important/)
-  [images](https://www.freepik.com/free-photos-vectors/air-quality-index)
  
## Appendix

Any additional information goes here

  1. https://en.tutiempo.net/
  2. https://www.oxygenconcentratorstore.com/blog/the-air-quality-index-why-is-it-important/
  3. https://www.freepik.com/free-photos-vectors/air-quality-index
## Author

- [Anjana Suresh](https://github.com/Anjana85)

  
## Deployment

To deploy this project run

Flask==1.1.1
gunicorn==19.9.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Werkzeug==0.15.5
numpy>=1.9.2
scipy>=0.15.1
scikit-learn==0.23.2
matplotlib>=1.4.3
pandas>=0.19

  
## 🚀 About Me 
I Love to work wuth data ...
The best part about working with data is seeing the impact it can have in an organization. 
Data can be powerfully objective when properly and thoroughly analyzed- seeing the predictions 
of intensive analysis lead to meaningful change is extremely rewarding.

Contact: anjana.ps85@gmail.com


  
