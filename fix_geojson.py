import json

# ชื่อไฟล์ต้นฉบับ (ที่คุณอัปโหลดมา)
input_filename = 'จังหวัดพิษณุโลก.geojson'
# ชื่อไฟล์ผลลัพธ์ที่จะได้
output_filename = 'phitsanulok_fixed.geojson'

def convert_to_valid_geojson(input_file, output_file):
    try:
        print(f"กำลังอ่านไฟล์: {input_file} ...")
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # ตรวจสอบว่าเป็น list หรือไม่
        if not isinstance(data, list):
            print("รูปแบบไฟล์ไม่ถูกต้อง (ต้องเป็น JSON Array)")
            return

        features = []
        
        for item in data:
            # ดึงค่าพิกัด
            lat_str = item.get("oct_side15_lat", "")
            lon_str = item.get("oct_side15_lon", "")
            
            # ตรวจสอบว่ามีค่าพิกัดครบถ้วน
            if lat_str and lon_str:
                try:
                    lat = float(lat_str)
                    lon = float(lon_str)
                    
                    # สร้าง Feature ตามมาตรฐาน GeoJSON
                    feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat]  # GeoJSON ใช้ [ลองจิจูด, ละติจูด]
                        },
                        "properties": item  # เก็บข้อมูลอื่นๆ ทั้งหมดไว้ใน properties
                    }
                    features.append(feature)
                except ValueError:
                    continue # ข้ามรายการที่แปลงพิกัดเป็นตัวเลขไม่ได้

        # สร้าง FeatureCollection
        geojson_output = {
            "type": "FeatureCollection",
            "features": features
        }
        
        # บันทึกไฟล์ใหม่
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(geojson_output, f, ensure_ascii=False, indent=2)
            
        print(f"เสร็จสิ้น! แปลงข้อมูลทั้งหมด {len(features)} รายการ")
        print(f"บันทึกไฟล์เรียบร้อยแล้วที่: {output_file}")
        print("สามารถนำไฟล์นี้ไปเปิดใน QGIS ได้เลยครับ")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# เรียกใช้งานฟังก์ชัน
convert_to_valid_geojson(input_filename, output_filename)