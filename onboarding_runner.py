import donkeycar.donkeycar as dk


from parts.image_publisher import Image_Publisher
from parts.log import Logger
from parts.image_cv import Object_Detection

if __name__ == "__main__":
    V = dk.vehicle.Vehicle()
    print("starting")

    image_pub = Image_Publisher()
    logger = Logger()
    object_detection = Object_Detection()

    V.add(image_pub, inputs=[], outputs=["image"])
    V.add(object_detection, inputs=["image"], outputs=["image_cv", "object_x", "object_y", "contour_area"])
    V.add(logger, inputs=["object_x", "object_y", "contour_area"], outputs=[])

    V.start(rate_hz=30)
    