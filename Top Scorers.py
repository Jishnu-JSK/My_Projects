import pandas as pd
import matplotlib.pyplot as pt
d={"Name":["Haaland","Mbappe","Ronaldo","Harry Kane"],
      "Team":["Man City","Real Madrid","Al Nassr","Bayern Münich"],
      "Goals":[50,52,54,52]}
df=pd.DataFrame(data=d)
avg=df['Goals'].mean()
print("THIS SEASON'S TOP SCORER")
print(df)
print("The Average Goals of the Season:",avg)

pt.figure(figsize =(10, 15))
pt.bar(df['Name'],df["Goals"],color='green')
pt.xlabel("Name")
pt.ylabel("Goals")
pt.title("Top Scorers of 2024")
pt.show() 
