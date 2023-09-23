# Virtual Try-On with OpenCV and Pose Detection

This project demonstrates a Virtual Try-On system using OpenCV, Pose Detection, and image overlays. It allows users to try on different shirts virtually and select the one they like.

## Features

- Real-time pose detection to identify key body points.
- Overlay different shirts on the user's upper body.
- Change shirts with gesture controls.
- Display a selection rectangle around the currently worn shirt.
- Display all available shirt options in the top left corner.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- OpenCV and cvzone libraries installed. You can install them using pip:

  ```bash
  pip install opencv-python
  pip install cvzone

A video source (e.g., webcam or video file) for trying on shirts.
Shirt images in a folder (e.g., "Resources/Shirts") that you want to use for virtual try-on.

## Usage:

1. Clone this repository to your local machine:

 ```bash
git clone https://github.com/yourusername/virtual-tryon.git

2. Navigate to the project directory:
 ```bash
cd virtual-tryon

3. Run the 'main.py' script:
```bash
python main.py

4. Use your webcam or provide a video file as the video source. The application will detect your upper body and overlay different shirts as you move.

5. Control the shirt selection with the following gestures:
-If your left hand goes above your head, it will cycle through shirt options to the left.
-If your right hand goes above your head, it will cycle through shirt options to the right.

6. The selected shirt will have a rectangular highlight around it.

## License

This project is licensed under the MIT License. See the LICENSE file for details.




