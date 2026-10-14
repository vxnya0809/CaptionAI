🗣️ CaptionAI — Real-Time Sign Language Captioning

Bridging communication gaps through AI-powered gesture recognition.

CaptionAI is an AI-powered application designed to make communication more accessible for deaf and hard-of-hearing individuals. It uses computer vision and hand gesture recognition to identify selected gestures through a live camera feed, convert them into readable text, and translate the generated captions into multiple Indian languages.

The project explores how Artificial Intelligence can support inclusive communication through an interactive, multilingual interface.

✨ Key Features

- Real-Time Gesture Recognition: Detects and recognizes supported hand gestures using a live camera feed.
- Text Caption Generation: Converts recognized gestures into readable text captions.
- Multilingual Translation: Translates generated captions into English, Tamil, Hindi, Telugu, Kannada, and Malayalam.
- Interactive Web Interface: Provides a simple interface built with Streamlit for real-time interaction.
- Computer Vision Integration: Uses MediaPipe for hand tracking and OpenCV for camera-frame processing.
- Accessibility-Focused Design: Explores technology-driven approaches to reducing communication barriers.

🛠️ Tech Stack

Technology| Purpose
Python| Core application development
OpenCV| Camera access and image processing
MediaPipe| Hand tracking and landmark detection
Streamlit| Interactive web application interface
Google Translator ("deep-translator")| Multilingual text translation
Machine Learning / Gesture Classification| Recognition of supported gestures

⚙️ How It Works

1. Camera Input: Captures live video through the device camera.
2. Hand Detection: MediaPipe detects and tracks hands in the video frames.
3. Gesture Recognition: The application processes hand information and classifies supported gestures.
4. Caption Generation: The recognized gesture is converted into its corresponding text.
5. Language Translation: The generated caption can be translated into a selected supported language.
6. Display Output: The caption and translated text are displayed through the Streamlit interface.

🌍 Supported Languages

- English
- Tamil
- Hindi
- Telugu
- Kannada
- Malayalam

🚀 Getting Started

Prerequisites

Make sure you have the following installed:

- Python 3.10 or another Python version compatible with your dependencies
- Git
- A working webcam
- Visual Studio Code or another Python IDE (optional)

Installation

1. Clone the repository

git clone https://github.com/vxnya0809/captionAI.git

2. Navigate to the project directory

cd captionAI

3. Create and activate a virtual environment (recommended)

python -m venv venv

Windows:

venv\Scripts\activate

4. Install the dependencies

If your repository contains a "requirements.txt" file:

pip install -r requirements.txt

Otherwise, install the packages used by your application:

pip install streamlit opencv-python mediapipe deep-translator

5. Run the application

streamlit run app.py

If your main Python file has a different name, replace "app.py" with the appropriate filename.

Open the local URL displayed in your terminal to access the application.

🎯 Project Objectives

- Explore real-time computer vision and hand gesture recognition.
- Convert supported gestures into understandable text.
- Demonstrate multilingual translation in an accessibility-focused application.
- Gain practical experience integrating Python libraries into an interactive AI application.
- Explore the potential of AI-assisted tools for more inclusive communication.

🔮 Future Enhancements

- Expand the gesture vocabulary and improve recognition accuracy.
- Develop a more robust gesture classification model using a larger and more diverse dataset.
- Support continuous gesture sequences and sentence-level caption generation.
- Improve performance under different lighting conditions and camera angles.
- Add speech output for generated captions.
- Explore broader sign language recognition with appropriate datasets and linguistic validation.

⚠️ Current Limitations

CaptionAI currently recognizes a limited set of supported gestures. Its output depends on the gestures included in the recognition system and the quality of camera input. It is a prototype intended for experimentation and learning, not a complete sign language interpreter.

The project does not yet support unrestricted sign language conversation or guarantee accurate interpretation of all signs.

👩‍💻 About the Project

CaptionAI is a student-led project exploring the practical application of Artificial Intelligence, computer vision, and multilingual technologies to accessibility challenges.

This project reflects an interest in building technology that combines technical learning with meaningful real-world applications.

📄 License

This project is open for learning and experimentation. A formal license has not yet been specified. Add a suitable "LICENSE" file before defining permissions for reuse or redistribution.

---

Built with Python, Computer Vision, and a focus on accessible communication.
