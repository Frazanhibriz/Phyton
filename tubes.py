import streamlit as st
import pandas as pd
import time
import plotly.express as px
import numpy as np

def insertion_sort(arr, key):
    comparisons = 0
    start_time = time.time()
    
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > key_item[key]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key_item
    
    end_time = time.time()
    return arr, end_time - start_time, comparisons

def selection_sort(arr, key):
    comparisons = 0
    start_time = time.time()
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    end_time = time.time()
    return arr, end_time - start_time, comparisons

def format_dataframe(df, start_no=1):

    df['No'] = range(start_no, len(df) + start_no)
    

    cols = ['No'] + [col for col in df.columns if col != 'No']
    df = df[cols]
    

    df['NIM'] = df['NIM'].astype(str)
    

    df['GPA'] = df['GPA'].round(2)
    

    df = df.set_index('No')
    
    return df


st.title("Student Data Sorting Algorithm Comparison")


st.sidebar.header("Input Data")
num_students = st.sidebar.slider("Number of students", 5, 100, 20)


names = [f"Student_{i+1}" for i in range(num_students)]
nims = np.random.randint(10000000, 99999999, size=num_students)
gpas = np.random.uniform(2.0, 4.0, size=num_students)

data = [{"Name": name, "NIM": nim, "GPA": gpa} 
        for name, nim, gpa in zip(names, nims, gpas)]


df = pd.DataFrame(data)
df = format_dataframe(df)
st.subheader("Original Student Data")
st.dataframe(df)


sort_key = st.selectbox("Sort by", ["Name", "NIM", "GPA"])
sort_algorithm = st.selectbox("Choose Algorithm", ["Insertion Sort", "Selection Sort", "Compare Both"])

if st.button("Sort Data"):
    if sort_algorithm == "Insertion Sort" or sort_algorithm == "Compare Both":
        insertion_data = data.copy()
        sorted_insertion, insertion_time, insertion_comparisons = insertion_sort(insertion_data, sort_key)
        
        st.subheader("Insertion Sort Results")
        st.write(f"Time taken: {insertion_time:.6f} seconds")
        st.write(f"Number of comparisons: {insertion_comparisons}")

        insertion_df = pd.DataFrame(sorted_insertion)
        insertion_df = format_dataframe(insertion_df)
        st.dataframe(insertion_df)
        
    if sort_algorithm == "Selection Sort" or sort_algorithm == "Compare Both":
        selection_data = data.copy()
        sorted_selection, selection_time, selection_comparisons = selection_sort(selection_data, sort_key)
        
        st.subheader("Selection Sort Results")
        st.write(f"Time taken: {selection_time:.6f} seconds")
        st.write(f"Number of comparisons: {selection_comparisons}")
        # Format and display sorted data
        selection_df = pd.DataFrame(sorted_selection)
        selection_df = format_dataframe(selection_df)
        st.dataframe(selection_df)
    
    if sort_algorithm == "Compare Both":

        comparison_data = {
            'Algorithm': ['Insertion Sort', 'Selection Sort'],
            'Time (seconds)': [insertion_time, selection_time],
            'Comparisons': [insertion_comparisons, selection_comparisons]
        }
        

        fig_time = px.bar(comparison_data, 
                         x='Algorithm', 
                         y='Time (seconds)',
                         title='Time Comparison')
        st.plotly_chart(fig_time)

        fig_comparisons = px.bar(comparison_data, 
                                x='Algorithm', 
                                y='Comparisons',
                                title='Number of Comparisons')
        st.plotly_chart(fig_comparisons)

st.subheader("Time Complexity Analysis")
st.write("""
- Insertion Sort:
  - Best Case: O(n) when the array is already sorted
  - Average Case: O(n²)
  - Worst Case: O(n²) when the array is reverse sorted
  
- Selection Sort:
  - Best Case: O(n²)
  - Average Case: O(n²)
  - Worst Case: O(n²)
""")