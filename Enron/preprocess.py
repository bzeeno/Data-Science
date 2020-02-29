import sys
import pickle
import numpy as np
import pandas as pd

pickle_file = "data.pkl"

with open(pickle_file, "rb") as all_pickle:
	raw_dict = pickle.load(all_pickle,encoding="latin1")

feature_names = []
features = []

first_iter = True
for person_name, values in raw_dict.items():
    # Array to hold current feature values
    temp_array = np.array([])

    # Only run on first iteration
    if (first_iter == True):
        # Put feature names in list
        feature_names = values.keys()
    
    first_iter = False

    # Get feature values for current person
    for feature_name, feature_value in values.items():
        # Append feature_value to temporary array
        temp_array = np.append(temp_array, feature_value)
    # Add temporary array to features
    features.append(temp_array)

# Order of columns (Want poi at end)
cols = ["email_address",
        "long_term_incentive",
        "expenses",
        "exercised_stock_options",
        "from_messages",
        "salary", 
        "director_fees",  
        "total_payments",
        "restricted_stock", 
        "from_poi_to_this_person",
        "from_this_person_to_poi", 
        "total_stock_value", 
        "bonus",
        "restricted_stock_deferred", 
        "loan_advances",
        "shared_receipt_with_poi", 
        "other", 
        "deferred_income",
        "deferral_payments", 
        "to_messages",
        "poi"]

# Save to pandas dataframe
df = pd.DataFrame(data=features,columns=feature_names)
df = df[cols] # rearrange columns so POI is last

print(df.head())


