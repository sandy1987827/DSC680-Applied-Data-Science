
#### Project 3: Model to Predict Quality of Wine

Wine is the fermented juice of grapes, made in many varieties, such as red, white, sweet, dry, still, and sparkling, for use as a beverage, in cooking, in religious rites, etc., and usually having an alcoholic content of 14 percent or less. The wine industry shows a recent exponential growth as social drinking is on the rise. Nowadays, industry players are using product quality certifications to promote their products. This is a time-consuming process and requires the assessment given by human experts, which makes this process very expensive. Also, the price of wine depends on a rather abstract concept of wine appreciation by wine tasters, opinion among whom may have a high degree of variability. Another vital factor in wine certification and quality assessment is physicochemical tests, which are laboratory-based and consider factors like acidity, pH level, sugar, and other chemical properties. The wine market would be of interest if the human quality of tasting can be related to wine’s chemical properties so that certification and quality assessment and assurance processes are more controlled. This project aims to determine which features are the best quality wine indicators and generate insights into each of these factors to our model’s wine quality.

* We have used the selectKbest method to identify the best features in the dataset
* Dropped some of the features that are not useful for predicting the quality
* Random Forest Regressor, Linear Regression, Random Forest Classifier and Decision Tree Classifier were used
* Random Forest Classifier has best accuracy when compared with all other models.
* The model was implemented to predict the quality of the wine based on the dependent variables alcohol, volatile acidity etc.
