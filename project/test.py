from pymongo import MongoClient
import gridfs

def save_audio_to_mongo(file_path,
                        mongo_uri="mongodb+srv://ebzlevinson:AdyRDIGdvKWy3AtM@cluster0.7zr8p1s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
                        db_name="audio_db"):
    """
    שמירה של קובץ שמע לתוך MongoDB בעזרת GridFS
    """
    # 1. חיבור ל-Atlas
    client = MongoClient(mongo_uri)
    db = client[db_name]

    # 2. יצירת GridFS
    fs = gridfs.GridFS(db)

    # 3. פתיחת הקובץ והעלאתו ל-DB
    with open(file_path, "rb") as f:
        file_id = fs.put(f, filename=file_path.split("\\")[-1])
        print(f"✅ הקובץ {file_path} נשמר במונגו עם _id: {file_id}")
        return file_id
def load_audio_from_mongo(file_id,
                          output_path,
                          mongo_uri="mongodb+srv://ebzlevinson:AdyRDIGdvKWy3AtM@cluster0.7zr8p1s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
                          db_name="audio_db"):
    """
    שליפה של קובץ מ-MongoDB GridFS ושמירה חזרה לדיסק
    """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    fs = gridfs.GridFS(db)

    # שליפה לפי file_id
    audio_data = fs.get(file_id).read()

    with open(output_path, "wb") as f:
        f.write(audio_data)

    print(f"✅ הקובץ שוחזר ממונגו ונשמר בשם: {output_path}")


if __name__ == "__main__":
    # 🔹 תעדכן את הנתיב לקובץ האמיתי אצלך
    file_path = r"C:\Users\צרצוש\Desktop\testC\MuezzinProject\project\data_files\podcasts\download (1).wav"

    file_id = save_audio_to_mongo(file_path)

    # שלב 2: שליפה חזרה ושמירה בדיסק
    output_file = r"C:\Users\צרצוש\Desktop\restored.wav"
    load_audio_from_mongo(file_id, output_file)