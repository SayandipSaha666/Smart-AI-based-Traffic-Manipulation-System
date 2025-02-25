# Smart AI-Based Traffic Manipulation System

## Overview
The **Smart AI-Based Traffic Manipulation System** is an intelligent traffic management solution leveraging **YOLOv8** for object detection and **OpenCV** for video processing. This system processes video feeds to detect vehicles and count incoming and outgoing vehicles in real-time. The data is then used to dynamically adjust traffic light conditions, optimizing traffic flow and reducing congestion.

## Features
- **Real-time Object Detection**: Utilizes YOLOv8 for accurate vehicle identification.
- **Vehicle Counting**: Tracks and maintains count of vehicles entering and exiting.
- **Dynamic Traffic Control**: Adjusts traffic signals based on vehicle density.
- **Emergency Vehicle Detection**: Automatically prioritizes emergency vehicles.
- **Accident Detection**: Identifies unusual activities and stops traffic for safety.

## Technologies Used
- **YOLOv8** (You Only Look Once) for vehicle detection.
- **OpenCV** for video processing.
- **Python** for implementation.
- **Arduino** for traffic signal control.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/SayandipSaha666/Smart-AI-based-Traffic-Manipulation-System.git
   cd Smart-AI-based-Traffic-Manipulation-System
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the system:
   ```sh
   python main.py --video input_video.mp4
   ```
   
   **Arguments:**
   - `--video` : Path to the input video file.
   - `--live` : (Optional) Enable real-time processing from a camera.

## How It Works
1. **Video Input**: The system processes video feeds from cameras.
2. **Object Detection**: YOLOv8 detects and classifies vehicles.
3. **Vehicle Counting**: Tracks vehicles entering and exiting a zone.
4. **Traffic Signal Adjustment**: Dynamically modifies signal timings based on real-time vehicle count.

## Future Enhancements
- **Integration with GPS & Google Maps** for real-time traffic updates.
- **Advanced Traffic Prediction Models** using AI.
- **Dynamic Lane Management** to optimize road usage.
- **Better Pedestrian Safety Measures** with intelligent signal control.

## Contributing
Contributions are welcome! Please create an issue or pull request for improvements.

## License
This project is licensed under the MIT License.

## Contact
For queries, open an issue on the [GitHub repository](https://github.com/SayandipSaha666/Smart-AI-based-Traffic-Manipulation-System) or contact **sahasbhs2022@gmail.com**.

---
Made with ❤️ using AI & Computer Vision.

