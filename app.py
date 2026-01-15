import json

# ชื่อไฟล์ต้นฉบับและไฟล์ปลายทาง
input_filename = 'jsonformatter.txt'
output_filename = 'output.geojson'

def convert_to_geojson(input_file, output_file):
    try:
        # อ่านไฟล์ JSON ต้นฉบับ
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        features = []
        
        for item in data:
            # ดึงค่าพิกัด
            lat_str = item.get("oct_side15_lat", "")
            lon_str = item.get("oct_side15_lon", "")
            
            # ตรวจสอบว่ามีค่าพิกัดหรือไม่
            if lat_str and lon_str:
                try:
                    lat = float(lat_str)
                    lon = float(lon_str)
                    
                    # สร้าง GeoJSON Feature
                    feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat] # GeoJSON ใช้ [ลองจิจูด, ละติจูด]
                        },
                        "properties": item # เก็บข้อมูลอื่นๆ ไว้ใน properties
                    }
                    features.append(feature)
                except ValueError:
                    print(f"Skipping item with invalid coordinates: {lat_str}, {lon_str}")
                    continue

        # สร้าง FeatureCollection
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        
        # บันทึกเป็นไฟล์ .geojson
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2)
            
        print(f"แปลงไฟล์สำเร็จ! บันทึกไฟล์ที่: {output_file}")
        print(f"จำนวนข้อมูลทั้งหมด: {len(features)} รายการ")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# เรียกใช้งานฟังก์ชัน
convert_to_geojson(input_filename, output_filename)