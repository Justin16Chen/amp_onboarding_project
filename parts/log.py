import datetime
import csv

class Logger():
    def __init__(self):
        self.file = open("logger.csv", "w", newline="")
        self.writer = csv.writer(self.file)

        self.writer.writerow(["timestamp", "object/x", "object/y", "contour/area"])

    def run(self, object_x, object_y, contour_area):
        if object_x is None or object_y is None or contour_area is None:
            return None

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
        row = [timestamp, object_x, object_y, contour_area]
        self.writer.writerow(row)

        
    

