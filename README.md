# Phishing & Malicious Domain Detection

An intelligent phishing and malicious domain detection system developed for the Smart India Hackathon. This project uses machine learning models and domain analysis to identify suspicious URLs and protect users from phishing attacks.

## 🎯 Project Overview

This system combines multiple approaches to detect phishing and malicious domains:
- **Machine Learning Models**: TensorFlow Lite and Random Forest classifiers for URL classification
- **Domain Analysis**: WHOIS API integration and domain feature extraction
- **Browser Extension**: Chrome extension for real-time URL scanning
- **REST API**: Flask-based backend for URL analysis
- **URL Analysis**: Advanced URL parsing and feature extraction techniques

## 📁 Project Structure

```
├── app.py                              # Flask API server
├── trials.py                           # Main detection logic
├── urlAnalysis.py / urlAnalysis_updated.py  # URL feature extraction
├── domainAnalysis.py                   # Domain-level analysis
├── whoisapi.py                         # WHOIS API integration
├── randomForestModel.py                # Random Forest model training
├── MLraw.py                            # ML preprocessing
│
├── Models/
│   ├── phishing_detection_model.tflite        # TensorFlow Lite model v1
│   ├── phishing_detection_model_v4.tflite     # TensorFlow Lite model v4
│   ├── rfcModel.sav                           # Random Forest classifier v1
│   ├── rfcModel2.sav                          # Random Forest classifier v2
│   ├── rfcModel3.sav                          # Random Forest classifier v3
│   └── rfcModelv4.sav                         # Random Forest classifier v4
│
├── Data/
│   ├── Domain Data.csv                        # Domain features dataset
│   ├── Domain Data 2.csv                      # Extended domain dataset
│   ├── Domain Data 3.csv                      # Dataset variant 3
│   ├── Domain Data 4.csv                      # Dataset variant 4
│   ├── Updated Dataset.csv                    # Latest dataset version
│   ├── top-1m.csv                             # Top 1M legitimate domains
│   ├── top200.csv                             # Top 200 domains
│   ├── verified_online.csv                    # Verified legitimate sites
│   └── history.csv                            # Processing history
│
├── Chrome Extension/
│   ├── dontcare/                              # Main extension
│   │   ├── manifest.json
│   │   ├── popup.html
│   │   ├── popup.js
│   │   ├── content.js
│   │   └── background.js
│   │
│   └── extending/                             # Extended version
│       ├── manifest.json
│       ├── popup.html
│       ├── popup.js
│       ├── popup.css
│       └── fishy.js
│
├── requirements.txt                    # Python dependencies
├── vercel.json                         # Vercel deployment config
└── README.md                           # This file
```

## 🛠 Technologies Used

**Backend:**
- Python 3.x
- Flask - Web framework for REST API
- Scikit-learn - Machine learning library
- NumPy & Pandas - Data processing
- TensorFlow Lite - Lightweight ML model format
- BeautifulSoup - Web scraping

**Frontend:**
- Chrome Extension Manifest V3
- HTML/CSS/JavaScript
- Context menu integration

**Deployment:**
- Vercel - Serverless deployment platform
- Gunicorn - WSGI HTTP Server

## 📦 Installation

### Prerequisites
- Python 3.7+
- pip package manager
- Chrome browser (for extension)

### Backend Setup

1. **Clone or download the repository:**
```bash
cd d:\SIH--Severe
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Chrome Extension Setup

1. **Navigate to Chrome Extensions:**
   - Open Chrome
   - Go to `chrome://extensions/`
   - Enable "Developer mode" (top-right corner)

2. **Load the extension:**
   - Click "Load unpacked"
   - Navigate to the `extending/` or `dontcare/` folder
   - Select and load the extension

## 🚀 Usage

### Running the API Server

```bash
python app.py
```

The Flask server will start on `http://localhost:5000`

### API Endpoints

**Check URL Safety:**
```
GET /urls/<string:urls>
```
- **Parameter**: `urls` - URL to analyze (spaces replaced with `/`)
- **Response**: JSON with classification result

Example:
```bash
curl http://localhost:5000/urls/www.example.com
```

**Health Check:**
```
GET /justcheckin
```
Returns server status

**Root Endpoint:**
```
GET /
```
Returns "Server Up and Running"

### Using the Chrome Extension

1. Click the extension icon in your browser toolbar
2. Enter a URL or the extension will automatically check the current page
3. View real-time phishing detection results
4. Green indicator = Safe | Red indicator = Suspicious

## 🤖 Machine Learning Models

### Available Models

1. **TensorFlow Lite Models** (`.tflite`)
   - `phishing_detection_model.tflite` - Base model
   - `phishing_detection_model_v4.tflite` - Improved version 4
   - Optimized for mobile and browser deployment

2. **Random Forest Models** (`.sav`)
   - `rfcModel.sav` - Initial model
   - `rfcModel2.sav` - Improved iteration
   - `rfcModel3.sav` - Further refinement
   - `rfcModelv4.sav` - Latest version
   - Scikit-learn compatible

### Training Data

The project includes multiple datasets for model training:
- Domain features extracted from legitimate and phishing sites
- WHOIS information features
- URL structure analysis
- Historical domain data

## 📊 Key Features Analyzed

- Domain registration age
- Domain registrar information
- SSL certificate status
- URL structure patterns
- Domain popularity (top sites list)
- Special characters in domain
- Subdomain count
- URL length analysis
- Suspicious keyword detection
- Domain reputation

## 🔄 Workflow

1. **URL Input** → User submits URL via API or extension
2. **Feature Extraction** → Analyze domain and URL characteristics
3. **WHOIS Lookup** → Retrieve domain registration details
4. **Model Prediction** → Run through ML models
5. **Risk Assessment** → Calculate phishing probability
6. **Response** → Return classification to user

## 📝 Files Description

| File | Purpose |
|------|---------|
| `app.py` | Flask REST API server |
| `trials.py` | Main detection logic orchestration |
| `urlAnalysis.py` | URL feature extraction |
| `domainAnalysis.py` | Domain-level analysis |
| `whoisapi.py` | WHOIS API wrapper |
| `randomForestModel.py` | RF model training script |
| `MLraw.py` | ML data preprocessing |
| `Pls_work.js` | Utility JavaScript |

## 🔐 Security Considerations

- Models trained on known phishing and legitimate domain datasets
- Real-time WHOIS lookups for current domain information
- Multiple model ensemble for robust detection
- Chrome extension runs with minimal permissions

## 📈 Model Performance

The project uses multiple model versions, allowing comparison and selection of best performing variant:
- Version 4 models are the latest iterations
- Random Forest models provide interpretable decisions
- TensorFlow Lite models optimize for speed and size

## 🌐 Deployment

### Local Deployment
Run `python app.py` for development

### Production Deployment
Configured for Vercel deployment using `gunicorn`:
```bash
gunicorn app:app
```


**Last Updated**: October 2023

