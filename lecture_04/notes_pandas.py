# %% [markdown]
# # Pandas

# %%
import pandas as pd

# %% [markdown]
# dataframe-ის შექმნა dictionary-ის გამოყენებით.
# - key - სვეტის სახელი
# - value - სვეტის მონაცემები list-ის სახით

# %%
pd.DataFrame({
    "first_name": ["Abraham", "George", "Thomas"],
    "last_name": ["Lincoln", "Washgington", "Jefferson"],
    "age": [230, 300, 200]
})

# %% [markdown]
# dataframe-ის შექმნა მატრიცით.

# %%
df = pd.DataFrame([
    ["Abraham", "Lincoln", 230.0],
    ["Thomas", "Jefferson", 200],
    ["George", "washington", None],
    ["Franklin", "Roosevelt", 120]
], columns=["first_name", "last_name", "age"])

df

# %% [markdown]
# მონაცემების შენახვა შესაძლებელია სხვადასხვა ფორმატებში (json, excel, csv...), რისთვისაც არსებობს სხვადასხვა მეთოდები:
# - df.to_csv("file.csv")
# - df.to_json("file.json")
# - df.to_excel("file.xlsx")
# - ...

# %%
df.to_csv("./data/data.csv", index=False)

# %% [markdown]
# **ინდექსები**
# 
# dataframe-ის შექმნისას თითოეულ სტრიქონს ენიჭება ინდექსი - რიცხვი 0-დან n-მდე (n = სვეტების რაოდენობა), რომელიც შეგვიძლია გამოვიყენოთ ფილტრაციისთვის.
# 
# ინდექსის შეცვლა შესაძლებელია .set_index() მეთოდის გამოყენებით.

# %%
df.shape

# %%
df["id"] = list(map(lambda x: "00" + str(x), list(range(0, df.shape[0]))))

# %%
# copy the existing df, set a new index and return
df.set_index("id", inplace=False)

# modify the existing df
df.set_index("id", inplace=True)

# %% [markdown]
# ***dataframe-ის სხვადასხვა მეთოებს შესაძლოა ქონდეთ inplace პარამეტრი, რომელიც განსაზღვრავს მეთოდი დააბრუნებს ახალ dataframe-ს თუ შეცვლის არსებულს.***

# %%
df

# %% [markdown]
# მონაცემებზე წვდომა:

# %%
df["first_name"]
df.first_name

# %% [markdown]
# **loc** vs **iloc**
# - loc  - მუშაობს ინდექსის და სვეტის დასახელებებზე
# - iloc - მუშაობს რიცხვით ინდექსებზე

# %%
df.loc["000", "first_name"]

df.iloc[0, -1]

# %% [markdown]
# dataframe-ში ცარიელი უჯრები წარმოდგენილია სპეციალური მონაცემთა ტიპით - NaN

# %%
# drop all rows with at least one NaN value in any column
df.dropna()

# %%
# replace all nan values with specific value
df["age"] = df["age"].fillna(df["age"].mean())

# %%
df

# %% [markdown]
# ლოგიკური ოპერატორები:
# 
# - or  - |
# - and - &
# - not - ~
# 
# dataframe-ში მონაცემების გაფილტრვა შესაძლებელია სხვადასხვა ლოგიკური პირობებით

# %%
df[[True, True, False, False]]

# %%
df[(df.age < 200) | (df.age > 300)]

# %% [markdown]
# მონაცემების წაკითხვა ფაილიდან:
# 
# pandas შესაძლებლობას გვაძლევს მონაცემები წავიკითხოთ სხვადასხვა ტიპის ფაილებიდან, რისთვისაც გვაქვს სხვადასხვა მეთოდები:
# - .read_csv("file.csv")
# - .read_excel("file.xlsx")
# - ...

# %%
df = pd.read_csv("./data/grades.csv")

# %%
df.columns

# %%
new_cols = []
for c in df.columns:
    new_cols.append(c.replace("\"", "").strip())
new_cols

# %%
new_cols = [c.replace("\"", "").strip() for c in df.columns]
df.columns = new_cols
df

# %%
df[~(df["Test2"] < 20) & (df["Test3"] < 40)]

# %%
df["Test2"].agg(["mean", "sum"])

# %%
df["Test2"].argmax()
