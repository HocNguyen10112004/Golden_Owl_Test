from sqlalchemy import create_engine, text
import os

# Kết nối đến MySQL trên Railway

DATABASE_URL = "mysql+pymysql://root:EIqfDiYrUKGvecStazdDNdcYdKKJeUmG@autorack.proxy.rlwy.net:17657/railway"

engine = create_engine(DATABASE_URL)

# Chạy lệnh insert dữ liệu thủ công để kiểm tra
with engine.connect() as conn:
    trans = conn.begin()
    try:
        conn.execute(text("INSERT INTO diem_thi (sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu) VALUES (2001, 9.0, 8.0, 7.5, 8.5, 8.8, 7.2, 6.9, 7.3, 8.7, 'A2');"))
        trans.commit()
        print("✅ Dữ liệu đã insert thành công!")
    except Exception as e:
        trans.rollback()
        print("❌ Lỗi khi insert:", e)
