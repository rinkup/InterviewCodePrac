# Problem statement was to return item(col 1) list with highiest popularity(col 2) lower price(col 3)
import pandas as pd
def sortItemList(inputItemList):
    data = pd.DataFrame(inputItemList)
    data = data[0].str.split(',', expand=True)
    data = data.sort_values(by=[1], ascending=False)
    data = data.sort_values(by=[2], ascending=True)
    return data[0].tolist()

inputList = ["Item 1,23,98", "Item 2,80,26.75", "Item 3,28,65", "Item 4,32,57", "Item 5,27,99", "Item 6,80,2"]
print(sortItemList(inputList))