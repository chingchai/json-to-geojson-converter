# JSON to GeoJSON Converter
A Python utility to convert Phitsanulok province's raw JSON data into GeoJSON format for use in QGIS and other GIS software.

เครื่องมือสำหรับแปลงไฟล์ข้อมูลดิบ (JSON) ของจังหวัดพิษณุโลก ให้เป็นรูปแบบ GeoJSON มาตรฐานสำหรับการใช้งานในโปรแกรม GIS (เช่น QGIS, ArcGIS, Google Earth)

## Features
- แปลงข้อมูล JSON Array ปกติให้เป็น GeoJSON FeatureCollection
- จัดการพิกัด (Latitude/Longitude) ให้ถูกต้อง
- รองรับภาษาไทย (UTF-8)

## Getting Started

1. วางไฟล์ข้อมูลดิบ (เช่น `jsonformatter.txt`) ในโฟลเดอร์เดียวกับสคริปต์
2. รันคำสั่ง:
   ```bash
   python app.py
   ```
   หรือ
   ```bash
   python fix_geojson.py
   ```
## Requirements
- Python 3.x
- Standard Library (json module) - ไม่ต้องติดตั้งอะไรเพิ่ม
