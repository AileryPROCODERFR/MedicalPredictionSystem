'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - missing_values.py
24 Oct 2024
**
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #convert categorical variables to numeric
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)

    #define features and target variable
    if 'charges' not in df_numeric:
        return "error: target variable 'charges' not found."
    X = df_numeric.drop('charges', axis=1)  #all columns except the target
    y = df_numeric['charges']  #target variable

    #split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    #dictionary to store the performance of each model
    model_performance = {}

    #build and evaluate linear regression
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)
    model_performance['Linear Regression'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_linear),
        'R2 Score': r2_score(y_test, y_pred_linear)
    }

    #build and evaluate decision tree regressor
    tree_model = DecisionTreeRegressor(random_state=42)
    tree_model.fit(X_train, y_train)
    y_pred_tree = tree_model.predict(X_test)
    model_performance['Decision Tree'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_tree),
        'R2 Score': r2_score(y_test, y_pred_tree)
    }

    #build and evaluate random forest regressor
    forest_model = RandomForestRegressor(random_state=42, n_estimators=100)
    forest_model.fit(X_train, y_train)
    y_pred_forest = forest_model.predict(X_test)
    model_performance['Random Forest'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_forest),
        'R2 Score': r2_score(y_test, y_pred_forest)
    }

    #build and evaluate k-nearest neighbors regressor
    knn_model = KNeighborsRegressor(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    model_performance['K-Nearest Neighbors'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_knn),
        'R2 Score': r2_score(y_test, y_pred_knn)
    }

    #build and evaluate support vector machine regressor
    svm_model = SVR(kernel='rbf')
    svm_model.fit(X_train, y_train)
    y_pred_svm = svm_model.predict(X_test)
    model_performance['SVM Regressor'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_svm),
        'R2 Score': r2_score(y_test, y_pred_svm)
    }

    #optional step: build and evaluate adaboost regressor
    ada_model = AdaBoostRegressor(random_state=42, n_estimators=100)
    ada_model.fit(X_train, y_train)
    y_pred_ada = ada_model.predict(X_test)
    model_performance['AdaBoost Regressor'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_ada),
        'R2 Score': r2_score(y_test, y_pred_ada)
    }

    #optional step: build and evaluate xgboost regressor
    xgb_model = XGBRegressor(random_state=42, n_estimators=100, use_label_encoder=False, eval_metric='rmse')
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    model_performance['XGBoost Regressor'] = {
        'Mean Squared Error': mean_squared_error(y_test, y_pred_xgb),
        'R2 Score': r2_score(y_test, y_pred_xgb)
    }

    #display the performance of each model
    performance_df = pd.DataFrame(model_performance).T
    performance_df.reset_index(inplace=True)
    performance_df.rename(columns={'index': 'Model'}, inplace=True)
    output.append("\n=== model performance summary ===\n")
    output.append(performance_df.to_string(index=False))

    #plotting the performance of each model with enhanced visuals
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    #bar plot for mean squared error with trendline
    sns.barplot(x='Model', y='Mean Squared Error', data=performance_df, ax=axes[0], palette='Blues_d')
    axes[0].set_title('Mean Squared Error of Regression Models', fontsize=16)
    axes[0].set_xlabel('Model', fontsize=14)
    axes[0].set_ylabel('Mean Squared Error', fontsize=14)
    axes[0].tick_params(axis='x', rotation=45)

    #adding trendline to mse bar plot
    x = np.arange(len(performance_df))
    z = np.polyfit(x, performance_df['Mean Squared Error'], 1)
    p = np.poly1d(z)
    axes[0].plot(x, p(x), linestyle='--', color='red', linewidth=2)

    #bar plot for r2 score with trendline
    sns.barplot(x='Model', y='R2 Score', data=performance_df, ax=axes[1], palette='Greens_d')
    axes[1].set_title('R2 Score of Regression Models', fontsize=16)
    axes[1].set_xlabel('Model', fontsize=14)
    axes[1].set_ylabel('R2 Score', fontsize=14)
    axes[1].tick_params(axis='x', rotation=45)

    #adding trendline to r2 score bar plot
    z_r2 = np.polyfit(x, performance_df['R2 Score'], 1)
    p_r2 = np.poly1d(z_r2)
    axes[1].plot(x, p_r2(x), linestyle='--', color='red', linewidth=2)

    plt.tight_layout()
    plt.show()

    return "\n\n".join(output)

