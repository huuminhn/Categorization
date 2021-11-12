import pandas as pd
import streamlit as st
import components as comp

st.set_page_config(layout = 'wide')

# Create the side bar and uploader tool:
sidebar_title = st.sidebar.title('Keywords Categorization Tool')

st.markdown('## **NOTE:** ##')
st.write('In order for the tool to run smoothly, please put the columns name as: ')
st.write('Keyword, Campaign ID, Adgroup ID, Campaign Name, Adgroup Name')

upload = st.sidebar.file_uploader(label = '1. Upload your file here 📥', type = ['csv'])
s = int(st.sidebar.number_input('2. Enter a number of keywords per Adgroup: '))

st.sidebar.write('3. Wait a while for the program to run')

st.sidebar.write('4. Please scroll down to the bottom of the page to download the file 📥')


# Get the data:
data = comp.file_uploading(upload)

#Group it up:
data_groupby = data.groupby(['Campaign Name', 'Adgroup Name']).count().sort_values(['Keyword'], ascending = False).reset_index()
st.header('The Number of Keywords in each Campaigns and Adgroup Before: ')
st.write(data_groupby)

df = data.groupby(['Campaign Name', 'Adgroup Name'])

#Create the categorization function:
def cat(x):
    n = int(len(x)/ s + 1)

    for i in range(0,n):
        x['Adgroup Name'][i*s:(i+1)*s] = x['Adgroup Name'][i*s:(i+1)*s] + ' ' + str(i + 1)
        

# Apply the categorization function:

lyst = []
for a,b in df:
    cat(b)
    lyst.append(b)

categorized_data = pd.concat(lyst) # This is the data we want

cat_num = categorized_data.groupby(['Campaign Name', 'Adgroup Name']).count().sort_values(['Keyword','Campaign Name','Adgroup Name'], ascending = False).reset_index()

st.header('The New Categorized Adgroup and Coressponding Number of Keywords: ')
st.write(cat_num)

# Export the data:
#export_file = comp.to_excel(categorized_data)

comp.csv_downloader(categorized_data)