# Smart AI-Based Traffic Manipulation System

## Overview
The **Smart AI-Based Traffic Manipulation System** is an intelligent traffic management solution that leverages **YOLOv8** for object detection and **OpenCV** for video processing. This system processes video inputs to detect vehicles and count the number of incoming and outgoing vehicles in real-time. Based on this data, it dynamically adjusts traffic light conditions to optimize traffic flow and reduce congestion.

## Features
- **Real-time Object Detection**: Uses YOLOv8 to accurately detect vehicles.
- **Vehicle Counting**: Tracks and counts incoming and outgoing vehicles.
- **Dynamic Traffic Control**: Adjusts traffic signals based on vehicle density.
- **OpenCV Integration**: Efficiently processes video streams.
- **Scalable and Customizable**: Can be adapted to different traffic environments.

## Technologies Used
- **YOLOv8** (You Only Look Once) for vehicle detection
- **OpenCV** for video processing
- **Python** for implementation

## Installation
To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/Smart-AI-based-Traffic-Manipulation-System.git
cd Smart-AI-based-Traffic-Manipulation-System
pip install -r requirements.txt
```

## Usage
Run the system by executing:

```bash
python main.py --video input_video.mp4
```

### Arguments:
- `--video` : Path to the input video file.
- `--live` : (Optional) Enable real-time processing from a camera.

## How It Works
1. **Video Input**: The system takes a video feed as input.
2. **Object Detection**: YOLOv8 identifies and classifies vehicles in each frame.
3. **Vehicle Counting**: Tracks the number of incoming and outgoing vehicles.
4. **Traffic Signal Adjustment**: Adjusts the traffic lights dynamically based on the detected vehicle count.

## Future Enhancements
- Implementing **deep learning-based traffic prediction**
- Enhancing detection for **bicycles, pedestrians, and emergency vehicles**
- Integrating **IoT sensors** for real-world deployment

## Contributing
Contributions are welcome! Please create an issue or pull request for any improvements.

## License
This project is licensed under the MIT License.

## Contact
For any queries, reach out at sahasbhs2022@gmail.com or open an issue in the repository.

---
Made with ❤️ using AI & Computer Vision.

