# 🏠 House Price Predictor

A little Flask web app that takes house details — `size`, `year`, and `view` — and uses a support vector regressor model to predict its price.

## 💡 Features

- Predicts housing prices using a pre-trained `.pkl` model
- Clean UI with Bootstrap 5
- Interactive form submission with vanilla JavaScript
- Minimal dependencies, fast and lightweight

## ⚽️ Tech Stack

- Python 3.9+
- Flask
- Scikit-learn (for model)
- HTML/CSS/Bootstrap
- JavaScript (basic fetch API)
- [Pickle](https://docs.python.org/3/library/pickle.html) for model serialization


## 🏎️ Run it own your own machine

1. Clone the repo:

   `git clone https://github.com/TDJR007/house-price-predictor.git`

   `cd House-Price-Predictor`

2. Set up the virtual environment

    `python3 -m venv venv`
    
    `source venv/bin/activate`
    
    (For windows) `venv\scripts\activate`
    
3. Install dependencies:

    `pip install -r requirements.txt`
    
4. Run SVR_Real_Estate.py to generate pickle files:

    `python3 model/SVR_Real_Estate.py`
    
    or you could use the notebook in models/

4. Run the app:

    `python app.py`

5. Open your browser at `http://localhost:5000`


## 📸 Credits

Special thanks to *Avi Waxman*! 😊️ for giving away his beautiful picture "white-and-red houses" royalty free on unsplash. It serves as the background image for this project and we appreciate the vibes.


