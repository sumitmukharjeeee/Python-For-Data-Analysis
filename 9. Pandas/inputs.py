import pandas as pd

def createDataFrameFromInput():
    n = int(input("How many students? "))
    rows = []
    for i in range(n):
        stuid = int(input(f"Student {i+1} ID: "))
        age = int(input(f"Student {i+1} age: "))
        rows.append(stuid,age)

    df = pd.DataFrame(rows, columns=["stundent_id","age"])
    return df

createDataFrameFromInput()