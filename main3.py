import mysql.connector
import csv


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "18780",
    database = "mon"
)

mycursor = db.cursor()

mycursor.execute("""
CREATE DATABASE IF NOT EXISTS mydb
""")
mycursor.execute("""
USE mydb
""")


data1 = [
    [' Exploring the beauty of the beaches at sunset.', 'sunset, beach', 'Sunset Wonders', 'travel', 'P001', 'Ali Rezaei', 'ali.rezaei@example.com'],
    ['A comprehensive guide to hiking the tallest mountains.', 'hiking, mountain', 'Mountain Adventures', 'nature', 'P002', 'Sara Mohammadi', 'sara.mohammadi@example.com'],
    ['Discovering the nightlife in bustling cities.', 'night, city', 'City Life', 'urban', 'P003', 'Hossein Karimi', 'hossein.karimi@example.com'],
    ['The wonders of the rainforest and its hidden waterfalls.', 'waterfall, rainforest', 'Rainforest Secrets', 'nature', 'P002', 'Sara Mohammadi', 'sara.mohammadi@example.com'],
    ['Surviving the harsh conditions of the desert.', 'desert, sand', 'Desert Survival', 'travel', 'P001', 'Ali Rezaei', 'ali.rezaei@example.com'],
    ['The calming effect of ocean waves.', 'ocean, waves', 'Ocean Calm', 'nature', 'P004', 'Maryam Ahmadi', 'maryam.ahmadi@example.com'],
    ['A walk through the forest trails.', 'forest, trail', 'Forest Walk', 'nature', 'P005', 'Reza Jafari', 'reza.jafari@example.com'],
    ['The magnificence of city skylines.', 'city, skyline', 'Skyline Views', 'urban', 'P003', 'Hossein Karimi', 'hossein.karimi@example.com'],
    ['Experiencing the magic of winter wonderland.', 'winter, snow', 'Winter Magic', 'seasonal', 'P006', 'Fatemeh Ebrahimi', 'fatemeh.ebrahimi@example.com'],
    [' The beauty of autumn leaves.', 'autumn, leaves', 'Autumn Beauty', 'seasonal', 'P007', 'Mahdi Ghasemi', 'mahdi.ghasemi@example.com']
]

data2 = [
    ['/path/to/image1.jpg', 'Sunset at the Beach', 'sunset', 'A beautiful sunset at the beach with golden hues lighting up the sky and reflecting on the water.', 'travel', 'P001', 'Ali Rezaei', 'ali.rezaei@example.com'],
    ['/path/to/image2.jpg', 'Mountain Range', 'hiking', 'A stunning mountain range, perfect for hiking enthusiasts looking for breathtaking views.', 'nature', 'P002', 'Sara Mohammadi', 'sara.mohammadi@example.com'],
    ['/path/to/image3.jpg', 'City Lights', 'night', 'The city comes alive at night with vibrant lights and a bustling atmosphere.', 'urban', 'P003', 'Hossein Karimi', 'hossein.karimi@example.com'],
    ['/path/to/image4.jpg', 'Rainforest Waterfall', 'waterfall', 'A serene rainforest waterfall surrounded by lush greenery and exotic wildlife.', 'nature', 'P002', 'Sara Mohammadi', 'sara.mohammadi@example.com'],
    ['/path/to/image5.jpg', 'Desert Dunes', 'desert', 'Majestic desert dunes with rippling sands stretching as far as the eye can see.', 'travel', 'P001', 'Ali Rezaei', 'ali.rezaei@example.com'],
    ['/path/to/image6.jpg', 'Ocean Waves', 'ocean', 'The calming effect of ocean waves crashing against the shore, creating a soothing symphony.', 'nature', 'P004', 'Maryam Ahmadi', 'maryam.ahmadi@example.com'],
    ['/path/to/image7.jpg', 'Forest Trail', 'forest', 'A tranquil forest trail perfect for a peaceful walk amidst nature\'s beauty.', 'nature', 'P005', 'Reza Jafari', 'reza.jafari@example.com'],
    ['/path/to/image8.jpg', 'City Skyline', 'city', 'The magnificence of the city skyline, capturing the essence of urban life.', 'urban', 'P003', 'Hossein Karimi', 'hossein.karimi@example.com'],
    ['/path/to/image9.jpg', 'Winter Wonderland', 'winter', 'Experiencing the magic of winter wonderland with snow-covered landscapes and a cozy atmosphere.', 'seasonal', 'P006', 'Fatemeh Ebrahimi', 'fatemeh.ebrahimi@example.com'],
    ['/path/to/image10.jpg', 'Autumn Leaves', 'autumn', 'The beauty of autumn leaves, showcasing a palette of vibrant colors as they fall.', 'seasonal', 'P007', 'Mahdi Ghasemi', 'mahdi.ghasemi@example.com']
]


with open('authors.csv', 'w', newline='') as csvfile:
    csvm = csv.writer(csvfile)
    csvm.writerows(data1)

with open('photos.csv', 'w', newline='') as csvfile:
    csvm = csv.writer(csvfile)
    csvm.writerows(data2)

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INT,
        content VARCHAR(255),
        keywords VARCHAR(255),
        title VARCHAR(255),
        category VARCHAR(255),
        writer_code VARCHAR(255),
        writer_name VARCHAR(255),
        writer_email VARCHAR(255),
        PRIMARY KEY(id)
    )
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS photos (
        id INT,
        image_path VARCHAR(255),
        title VARCHAR(255),
        tags VARCHAR(255),
        description VARCHAR(255),
        category VARCHAR(255),
        photographer_code VARCHAR(255),
        photographer_name VARCHAR(255),
        photographer_email VARCHAR(255),
        PRIMARY KEY(id)
    )
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS combined_data (
        id INT,
        image_path VARCHAR(255),
        photo_title VARCHAR(255),
        tags VARCHAR(255),
        description VARCHAR(255),
        photo_category VARCHAR(255),
        photographer_code VARCHAR(255),
        photographer_name VARCHAR(255),
        photographer_email VARCHAR(255),
        content VARCHAR(255),
        keywords VARCHAR(255),
        author_title VARCHAR(255),
        author_category VARCHAR(255),
        writer_code VARCHAR(255),
        writer_name VARCHAR(255),
        writer_email VARCHAR(255),
        PRIMARY KEY(id)
    )
""")

mycursor.execute("""
    INSERT INTO combined_data (
        image_path, photo_title, tags, description, photo_category,
        photographer_code, photographer_name, photographer_email,
        content, keywords, author_title, author_category,
        writer_code, writer_name, writer_email
    )
    SELECT
        p.image_path, p.title AS photo_title, p.tags, p.description, p.category AS photo_category,
        p.photographer_code, p.photographer_name, p.photographer_email,
        a.content, a.keywords, a.title AS author_title, a.category AS author_category,
        a.writer_code, a.writer_name, a.writer_email
    FROM photos p, authors a
    WHERE p.photographer_name = a.writer_name
""")

with open('authors.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        sql = "INSERT INTO authors (content, keywords, title, category, writer_code, writer_name, writer_email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, row)

with open('photos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sql = "INSERT INTO photos (image_path, title, tags, description, category, photographer_code, photographer_name, photographer_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, row)

with open('combined_data_without_join.csv', 'w', newline='') as csvfile:
    mycursor.execute("SELECT * FROM combined_data")
    data = mycursor.fetchall()
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([i[0] for i in mycursor.description])  
    csv_writer.writerows(data)

db.commit()
mycursor.close()
db.close()

print("Data imported successfully.")
