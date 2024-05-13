# Cat Prediction Application

This application predicts the likelihood of an image containing a cat using a single-layer neural network model. The backend is built with Python and Flask, while the frontend is built with Next.js. The model itself is saved in the .pickle format and created within a Jupyter Notebook.

## Features

 - User-friendly interface for uploading cat images
 - Real-time prediction of "cat" or "not cat"
 - Responsive design for various devices
 - Clear visualization of the prediction result

## Prerequisites

  - Node.js (version >= 14)
  - Python (version >= 3.7)
  - pip (Python package installer)

# Installation

## Clone the repository:
```
  git clone https://github.com/your-username/cat-prediction.git
```

## Install frontend dependencies:

```
cd cat-prediction/client
npm install
```

## Install backend dependencies:

```
cd ../server
pip install -r requirements.txt
```

# Running the Application

## Start the Next.js development server:

```
cd ../client
npm run dev
```

## In a separate terminal, start the Flask server:

```
cd ../server
python server.py
```
- Open your web browser and navigate to http://localhost:3000 to access the application.

# Contributing
We welcome contributions! Feel free to open an issue or submit a pull request if you find any issues or have suggestions for improvements.

# Additional Notes

- The .pickle model file should be placed in the appropriate directory within the server folder. Refer to the server-side code for specific instructions.
 - The Jupyter Notebook used to create the model is not included in this repository by default. However, you can provide a link to it or include it if desired.
