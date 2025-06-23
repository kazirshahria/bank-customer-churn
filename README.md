# :bank: Bank Churn Prediction

This project uses a kaggle [dataset](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers) with customer information for a bank. The dataset includes customer's demographic, spending, and card information. There is a public streamlit [app](https://bank-churn-predict.streamlit.app/) that uses the trained model to classify if a customer will stay or leave with the bank.

## Classifying Customers

The dataset is trained using scikit-learn's [random forest classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html). The model is a binary output, `0` predicts the customer will stay, and `1` predicts the customer will leave. 

### Why Use the Random Forest Model?

The random forest model is easy to understand for non-technical users. For example, the model can be explained by saying that it splits the data using a set of yes/no questions and finds the optimal splits with the least errors. In this case, multiple decision trees vote if a customer will stay or leave the bank.


Please refer to `notebook/project.ipynb` and find the code used to analyze, preprocess, and train the model.

## Information From Data Analysis

- Customers who are young and have few transactions, are more likely to leave the bank.
- Customers who have more transaction count and amount, are more likely to stay with the bank.
- The utilization ratio, calculated by **`revolving balance`** divided by **`credit limit`**, is one of the top features the model uses to predict customer churn.


## Project Drawbacks

- **Class imbalance** - There is an imbalance of classes, with less than 16% of customers leaving the bank.
- **Model fine-tuning** - The model parameters remained default values, and weren't fine tuned.
- **Dataset information** - There is minimal information on the bank and how reliable the data is.

## Future Outlook

More data on the bank and customer would allow for better prediction results. Solving the imbalance of classes can also create a less bias model.

## Credits
Huge shout out to the Baruch [MLDS](https://www.linkedin.com/company/baruchmlds) club. I was given the opportunity to teach machine learning concepts and collaborate with 5 other members to build a functional app.