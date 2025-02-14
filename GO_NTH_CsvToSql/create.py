import mysql.connector

#connect
conn = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="123456",   
    database="diem_thi_thpt"
)
cursor = conn.cursor()

#table_construction
sql = """
CREATE TABLE diem_thi (
    sbd BIGINT PRIMARY KEY,
    toan FLOAT,
    ngu_van FLOAT,
    ngoai_ngu FLOAT,
    vat_li FLOAT,
    hoa_hoc FLOAT,
    sinh_hoc FLOAT,
    lich_su FLOAT,
    dia_li FLOAT,
    gdcd FLOAT,
    ma_ngoai_ngu VARCHAR(2)
);
"""

cursor.execute(sql)

#close connection
cursor.close()
conn.close()

print("Bảng 'diem_thi' đã được tạo thành công")
