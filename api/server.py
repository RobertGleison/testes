import csv_processor as csv
from app import app

if __name__ == '__main__':
    csv.read_csv()
    app.run(host='0.0.0.0', port=9001)