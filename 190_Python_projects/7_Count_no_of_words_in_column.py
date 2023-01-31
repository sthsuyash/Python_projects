import pandas as pd
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding='latin-1')
# print(data.head(10))

# create new columns in the dataset and store the count of words in each column
data["No. of words in Article"] = data["Article"].apply(
    lambda x: len(x.split(" ")))
data["No. of words in Title"] = data["Title"].apply(
    lambda y: len(y.split(" ")))

# print the first row of dataset
print(data[:1].head())
