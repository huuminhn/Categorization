import pandas as pd
from io import BytesIO
#from pyxlsb import open_workbook as open_xlsb
import streamlit as st
import base64 
import time
timestr = time.strftime("%Y-%m-%d")

def file_uploading(upload):
    if upload is not None:
        data_import = pd.read_csv(upload)
        #columns = list(data_import.columns)
        #ad_num = int(upload['Ad Num'])

        return data_import

    else:
        return None

#Define the download function:
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def csv_downloader(data):
	csvfile = data.to_csv()
	b64 = base64.b64encode(csvfile.encode()).decode()
	new_filename = "Categorized_Adgroups_{}_.csv".format(timestr)
	st.markdown("## 📥 Download File Here 📥 ##")
	href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
	st.markdown(href,unsafe_allow_html=True)

