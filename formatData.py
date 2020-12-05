class Formatting:
    def formatData(df1):
        #get amount of rowsin data
        i = df1.shape[0]
        while(i > 0):
            i -=1
            #normalize ages
            if df1["Age"][i] == 'nan':
                df1["Age"][i] = "Unknown"
            elif df1["Age"][i] < 18:
                df1["Age"][i] = "Child"
            elif df1["Age"][i] > 18 and df1["Age"][i] < 30:
                df1["Age"][i] = "Young Adult"
            elif df1["Age"][i] < 50 and df1["Age"][i] > 30:
                df1["Age"][i] = "Adult"
            elif df1["Age"][i] > 50:
                df1["Age"][i] = "Elder Adult"
            #normalize fares
            if df1["Fare"][i] < 20.00:
                df1["Fare"][i] = "<20.00"
            elif df1["Fare"][i] > 20.00:
                df1["Fare"][i] = "<39.99"
            elif df1["Fare"][i] >= 40.00:
                df1["Fare"][i] = ">40.00"
            #normalize cabins as boolean
            if type(df1["Cabin"][i]) == float:
                df1["Cabin"][i] = "N"
            else:
                df1["Cabin"][i] = "Y"
            #create family size from SibSp and parch
            df1["SibSp"][i] += df1["Parch"][i]
        #drop columns with no relevant value: Parch becuase we used it with SibSp to create a new value,
        # Ticket becuase it has no relevance as it is unique to every customer
        dropColumns= ['Parch', 'Ticket']
        df1.drop(dropColumns, inplace=True, axis=1)
        df1.rename(columns = {'SibSp':'FamSize'}, inplace=True)
        return df1
