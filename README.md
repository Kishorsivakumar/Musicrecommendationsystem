# 🎵 Music Recommendation System using Facial Emotion Detection

## 📌 Project Overview

This is a Music Recommendation System that uses facial emotion detection to recommend music tracks. The system detects the user's facial emotion (like happy, sad, angry, etc.) and recommends a song that matches the detected emotion.I had used the Pre-Trained Model emotion_model.h5

## 🚀 Features

* ✅ Real-time facial emotion detection using a pre-trained model (`emotion_model.h5`).
* ✅ Automatic music recommendation based on the detected emotion.
* ✅ Supports multiple emotions (happy, sad, neutral, angry, fear, surprise, and disgust).
* ✅ Plays music using VLC media player (supports various formats like MP3, M4A).

## ⚡ Tech Stack

* **Language:** Python
* **Libraries:** OpenCV, Keras (for emotion model), VLC (for music playback), NumPy, Matplotlib
* **Jupyter Notebook:** For an interactive interface and easy testing

## 📁 Project Structure

```bash
├── Musicrecommendationsystembyusingfacialemotion.ipynb  # Main Jupyter Notebook
├── emotion_model.h5                                    # Pre-trained emotion detection model
├── README.md                                           # Project documentation
└── Music/                                              # Folder containing songs categorized by emotion
```

## ✅ How to Use

1. Clone this repository:

   ```bash
   git clone <repo-url>
   ```
2. Install the required libraries:

   ```bash
   pip install opencv-python-headless numpy matplotlib python-vlc
   ```
3. Ensure your `emotion_model.h5` is in the same directory.
4. Place your categorized music files in the `Music` folder.
5. Run the Jupyter Notebook.

## 🚀 Demo

* ✅ Run the notebook cell by cell to see the system in action.
* ✅ When an emotion is detected, the system will automatically play a recommended song.

## 🤖 Future Improvements

* 🌟 Add a GUI for easier use.
* 🌟 Support for Spotify API integration for real-time song fetching.
* 🌟 Optimize the emotion detection model for better accuracy.

## 💡 Acknowledgments

* The emotion detection model was trained using a pre-trained `emotion_model.h5`.
* Special thanks to the developers of the libraries used in this project.

## 📄 License

This project is open-source and free to use under the MIT License.
