import pandas as pd

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df, None
    except Exception as e:
        return None, e

def main():
    print("================")
    print("Alice & Bob's Pet Family!")

    # Reading first CSV file
    df1 = read_csv('Data/cat.csv')
    if df1 is not None:
        print("### Cat Eating Schedule:")
        print(df1)
    else:
        error("Error reading cat.csv:")

    # Reading second CSV file
    df2, error2 = read_csv('Data/dog.csv')
    if df2 is not None:
        print("### Dog Walking Schedule:")
        print(df2)
    else:
        error("Error reading dog2.csv")

if __name__ == "__main__":
  # Anything placed here will never be executed in a module context.
  main()
