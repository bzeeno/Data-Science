# argument: data file
import sys
import numpy as np
import pandas as pd

raw_csv_avg_income = pd.read_csv(str(sys.argv[1]))

df = raw_csv_avg_income.copy()

# Drop all rows that aren't "all_households" and drop all rows that are "all_quintiles" or a percentile
indices_to_drop = [] # list to hold indices that we will drop
incomes_to_drop = ["all_quintiles","percentiles_81_90","percentiles_91_95","percentiles_96_99","top_1_percent"]

for i in range(df["household_type"].shape[0]):

    if((df["household_type"][i] != "all_households")):
        indices_to_drop.append(i)

    for j in range(len(incomes_to_drop)):                      # Checking for income groups to drop
        if(df["income_group"][i] == incomes_to_drop[j]):       # if income group is listed as one to drop
            indices_to_drop.append(i)                          # Then drop it

df = df.drop(indices_to_drop, axis=0)
df = df.reset_index(drop=True)

# For this project, all I care about is income_group, year, market_income, inc_before_transfer_taxes inc_after_transfer_taxes. So, we'll drop the other columns
columns_to_drop = ["household_type", "social_insurance_benefits", "means_tested_transfers", "federal_taxes"]
df = df.drop(columns_to_drop, axis=1)

# Separate data based on quintile and save to file
lowest_indices = []
second_indices = []
middle_indices = []
fourth_indices = []
highest_indices = []

for i in range(df["income_group"].shape[0]):
    if(df["income_group"][i] == "lowest_quintile"):
        lowest_indices.append(i)
    elif(df["income_group"][i] == "second_quintile"):
        second_indices.append(i)
    elif(df["income_group"][i] == "middle_quintile"):
        middle_indices.append(i)
    elif(df["income_group"][i] == "fourth_quintile"):
        fourth_indices.append(i)
    elif(df["income_group"][i] == "highest_quintile"):
        highest_indices.append(i)
    else:
        print("Error: Row at index ", i, " was not assigned!")

# Separate into different dataframes
lowest_df = df.take(lowest_indices)
lowest_df = lowest_df.reset_index(drop=True)

second_df = df.take(second_indices)
second_df = second_df.reset_index(drop=True)

middle_df = df.take(middle_indices)
middle_df = middle_df.reset_index(drop=True)

fourth_df = df.take(fourth_indices)
fourth_df = fourth_df.reset_index(drop=True)

highest_df = df.take(highest_indices)
highest_df = highest_df.reset_index(drop=True)

# Save to csv's
lowest_df.to_csv("data/lowest_quintile.csv", index=False)
second_df.to_csv("data/second_quintile.csv", index=False)
middle_df.to_csv("data/middle_quintile.csv", index=False)
fourth_df.to_csv("data/fourth_quintile.csv", index=False)
highest_df.to_csv("data/highest_quintile.csv", index=False)

