# Movie Recommendation System


Pre-requisites:

Before proceeding with the installation process, ensure you have the following:

1. **Google Cloud Platform Account**: Obtain the necessary credentials (JSON key file) to authenticate with Firebase Cloud Firestore. Follow the instructions provided by Google to set up a project and generate a service account key.

2. **Python**: Ensure Python is installed on your system. You can download Python from the official website: Python Downloads.


Installation Steps:

1. **Clone the Repository**: `git clone https://github.com/itisgj/Movie-Recommendation-System.git`
2. **Navigate to the Project Directory**: `cd movie-recommendation-system`
3. **Set Up Virtual Environment**: `python -m venv venv`
4. **Activate Virtual Environment**:

   On Windows: `venv\Scripts\activate`
   On macOS and Linux: `source venv/bin/activate`
5. **Install Required Libraries**: `pip install numpy pandas scikit-learn streamlit firebase-admin`
6. **Add Firebase Credentials**: Place the JSON key file obtained from Google Cloud Platform in the project directory
7. **Run the Application**: `streamlit run app.py`
8. **Access the Application**: Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)


Note:

* Ensure that your Google Cloud Platform project has the Firebase Firestore service enabled.
* Replace `your-username` in the repository URL with your GitHub username.


Troubleshooting:

* If you encounter any issues during the installation process, refer to the documentation of the respective libraries or seek assistance from the community forums.
