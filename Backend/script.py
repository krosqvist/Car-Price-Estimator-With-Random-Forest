import sys
import pandas as pd
import joblib
from grapher import grapher
import os
import tempfile
import requests

args = sys.argv

MODEL_PATH = os.path.join(tempfile.gettempdir(), "car_price_model.pkl")
#if os.path.exists(MODEL_PATH):
#    os.remove(MODEL_PATH)
MODEL_URL = 'https://github.com/krosqvist/Car-Price-Estimator-With-Random-Forest/releases/download/RandomForestModel/car_price_model.pkl'
data = pd.read_csv('grouped_cars.csv')

def load_model():
    # Check if cached file exists
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            head = f.read(10)
        # If first bytes look like HTML, delete cache
        if head.startswith(b'<'):
            os.remove(MODEL_PATH)

    # Load from cache if valid
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    # Download from GitHub Release
    response = requests.get(MODEL_URL)
    response.raise_for_status()
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)

    # Verify file
    with open(MODEL_PATH, 'rb') as f:
        head = f.read(10)
        if head.startswith(b'<'):
            raise ValueError('Downloaded file looks like HTML, check MODEL_URL')
    return joblib.load(MODEL_PATH)

new_data = pd.DataFrame([{
    'Maker': args[1].lower(),
    'Genmodel': args[2].lower(),
    'Gearbox': args[3].lower(),
    'Fuel_type': args[4].lower(),
    'Bodytype': args[5].lower(),
    'Engin_size': float(args[6]),
    'Reg_year': int(args[7]),
    'Runned_Miles': int(args[8]),
    'Adv_year': 2025
}])

model = load_model()
grapher(
    model=model,
    maker=new_data.loc[0, 'Maker'],
    genmodel=new_data.loc[0, 'Genmodel'],
    reg_year=new_data.loc[0, 'Reg_year'],
    engin_size=new_data.loc[0, 'Engin_size'],
    gearbox=new_data.loc[0, 'Gearbox'],
    fuel_type=new_data.loc[0, 'Fuel_type'],
    bodytype=new_data.loc[0, 'Bodytype'],
    miles=new_data.loc[0, 'Runned_Miles'],
)