import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    border = "-"*40


    # Step1 : load the dataset from csv file
    print(border)
    print("Step1 : load the dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some Entries from dataset: ")
    print(df.head())
    print(border)


    # Step2 : Clean the dataset
    print(border)
    print("Step2 : Clean the dataset")
    print(border)

    df.dropna(inplace= True) #remove Na None values from the dataframe


    print("shape of dataset ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total Columns : ", df.shape[1])

    print(border)


    # Step3: Seperate independent and dependent variables

    print(border)
    print("Step3: Seperate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("shape of X : ",X.shape)
    print("shape of Y : ",Y.shape)

    print(border)
    print("input columns : ", X.columns.tolist())
    print("output columns : class")
    print(border)

    # Step4: split the data for tarining and testing

    print(border)
    print("Step4: split the data for tarining and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print(border)
    print("details of training and testing data")

    print("shape of X_train: ",X_train.shape)
    print("shape of X_test: ",X_test.shape)
    print("shape of Y_train: ",Y_train.shape)
    print("shape of Y_test: ",Y_test.shape)
    print(border)


    # Step5: Feture scaling
    
    print(border)
    print("Step5: Feture scaling")
    print(border)

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("feture scaling done")

    print(border)


    # Step6: Build the model
        
    print(border)
    print("Step6: Build the model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)

    print("classification model is created")


    #step7 : Train the model 
    print(border)
    print("step7 : Train the model")
    print(border)

    model = model.fit(X_train_scaled,Y_train)

    print("Model training completed")

    print(border)

    #step8 : Test the model 
    print(border)
    print("step8 : Test the model")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    acurracy = accuracy_score(Y_test,Y_pred)

    print("Model accuracy is : ",acurracy*100)





def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()