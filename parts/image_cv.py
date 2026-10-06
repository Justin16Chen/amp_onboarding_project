import cv2

class Object_Detection():
    def run(self, image):
        if image == None:
            return None

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        success, mask = cv2.threshold(gray, 127, 255, cv2.THRES_BINARY)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        largest_contour = None
        largest_moments = None

        for c in contours:
            moments = cv2.moments(c)
            if largest_moments is None or moments['m00'] > largest_moments['m00']:
                largest_moments = moments
                largest_contour = c
        if largest_moments is None:
            return None
    
        cv2.drawContours(image, [largest_contour], 0, (0, 255, 0), 2)
        centroid_x = -1
        centroid_y = -1
        if (largest_moments['m00'] > 1e-9):
            centroid_x = largest_moments['m10'] / largest_moments['m00']
            centroid_y = largest_moments['m01'] / largest_moments['m00']
            cv2.circle(image, (centroid_x, centroid_y), 10, (0, 0, 255), -1)

        return image, centroid_x, centroid_y, largest_moments['m00']

            
