import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print("First 5 records are : ")
    df.head()

    print("Last 5 records are : ")
    df.tail()

    print("Total number of rows and columns are : ", df.shape)

    print("Columns are : ",end="")
    print(df.columns.to_list())

    print("Datatype of each column is : ")
    for name in df.columns:
        print(name," : ",end="")
        print(type(name))

if __name__ == "__main__":
    main()
    