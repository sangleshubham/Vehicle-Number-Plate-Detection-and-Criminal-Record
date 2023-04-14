# Vehicle-Number-Plate-Detection-and-Criminal-Record
`mkdir backup`
### copy weight to backup directory

`plate_detect.py`: This file contains code to detect number plates in an image. It uses OpenCV to perform image processing tasks such as thresholding, blurring, edge detection, and contour detection to locate regions of interest that may contain number plates. It then applies a series of filters to eliminate non-plate regions and extracts the plate region using perspective transformation.

`character_recognition.py`: This file contains code to recognize characters on number plates. It uses the Tesseract OCR engine to perform character recognition on the extracted plate regions. The recognized characters are then filtered and processed to obtain the final license plate number.

`database.py`: This file contains code to connect to a MySQL database and perform CRUD operations on it. It includes functions to create a new record, read existing records, update records, and delete records.

`criminal_record.py`: This file contains code to check if a given license plate number is present in the criminal record database. It connects to the MySQL database using database.py and fetches the relevant records.

`main.py`: This file is the entry point of the application. It takes an input image and performs license plate detection and character recognition using plate_detect.py and character_recognition.py. It then checks if the license plate number is present in the criminal record database using criminal_record.py.
