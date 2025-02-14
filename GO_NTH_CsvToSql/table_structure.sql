
CREATE DATABASE diem_thi_thpt;

USE diem_thi_thpt;

CREATE TABLE diem_thi (
    sbd BIGINT PRIMARY KEY,
    toan DATE,
    ngu_van FLOAT,
    ngoai_ngu FLOAT,
    vat_li FLOAT,
    hoa_hoc FLOAT,
    sinh_hoc FLOAT,
    lich_su FLOAT,
    dia_li FLOAT,
    gdcd FLOAT,
    ma_ngoai_ngu varchar(2)
);