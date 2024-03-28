import streamlit as st
import pandas as pd

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df, None
    except Exception as e:
        return None, e

def main():
    st.title("Alice & Bob's Pet Family!")

    # Reading first CSV file
    df1, error1 = read_csv('Data/cat.csv')
    if df1 is not None:
        st.write("### Cat Eating Schedule:")
        st.dataframe(df1)
    else:
        st.error(f"Error reading cat.csv: {error1}")

    # Reading second CSV file
    df2, error2 = read_csv('Data/dog.csv')
    if df2 is not None:
        st.write("### Dog Walking Schedule:")
        st.dataframe(df2)
    else:
        st.error(f"Error reading dog2.csv: {error2}")

if __name__ == "__main__":
    main()
