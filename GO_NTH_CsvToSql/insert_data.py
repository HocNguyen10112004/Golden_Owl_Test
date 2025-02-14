import pandas as pd
import mysql.connector
import numpy as np
#connect
conn = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="123456",   
    database="diem_thi_thpt"
)
cursor = conn.cursor()

#read data (pandas)
df = pd.read_csv("diem_thi_thpt_2024.csv")  
df = df.replace({np.nan: None})

#insert
for index, row in df.iterrows():
    sql = """
    INSERT INTO diem_thi (sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        row["sbd"], row["toan"], row["ngu_van"], row["ngoai_ngu"],
        row["vat_li"], row["hoa_hoc"], row["sinh_hoc"],
        row["lich_su"], row["dia_li"], row["gdcd"], row["ma_ngoai_ngu"]
    )
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()

print("Dữ liệu đã được nhập thành công")
