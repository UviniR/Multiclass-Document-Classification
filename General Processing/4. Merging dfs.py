import pandas as pd

path="Data Set"

# List of DataFrames to merge
df_list = [pd.read_csv(path+"ChildProtection.csv"), pd.read_csv(path+"Cybersecurity.csv"), pd.read_csv(path+"DataPrivacy.csv"),
           pd.read_csv(path+"DataSystemsDevelopment.csv"), pd.read_csv(path+"DigitalFinance.csv"), pd.read_csv(path+"DigitalInclusion.csv"),
           pd.read_csv(path+"DigitalInformatioServices.csv"), pd.read_csv(path+"DigitalInfrastructure.csv"), pd.read_csv(path+"DigitalLiteracy.csv"),
           pd.read_csv(path+"DigitalServices.csv"), pd.read_csv(path+"Egovernment.csv"), pd.read_csv(path+"Upskilling.csv")]

# Merge the DataFrames using the `concat()` function
merged_df = pd.concat(df_list)

merged_df.drop(columns="filename",inplace=True)

# save the new Dataframe
merged_df.to_csv('Processed DF/Merged_data.csv', index=False)

# Group the dataframe by the content column, and concatenate the fileclass column
# this is to treat multi-label instances
final = merged_df.groupby("content").agg({"fileclass": lambda x: ", ".join(x)}).reset_index()

#save the new Dataframe
final.to_csv('Processed DF/Labelled.csv', index=False)