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
    try:
        df1 = read_csv('Data/cat.csv')    
        print("### Cat Eating Schedule:")
        print(df1)
    except:
        raise Exception("Error reading cat.csv")

    # Reading second CSV file
    
    try:
        df2 = read_csv('Data/dog.csv')
        print("### Dog Walking Schedule:")
        print(df2)
    except:
        raise Exception("Error reading dog.csv")

if __name__ == "__main__":
  # Anything placed here will never be executed in a module context.
  main()
