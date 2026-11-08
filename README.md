# Bike Sharing Demand Forecast

[![CI](https://github.com/Lennykipchumba33/bike-demand-forecast/actions/workflows/ci.yml/badge.svg)](https://github.com/Lennykipchumba33/bike-demand-forecast/actions/workflows/ci.yml)

A reproducible forecasting example using hourly Capital Bikeshare rental counts from 2011–2012 with weather and calendar covariates.

## What this demonstrates

- Time-aware data ordering and chronological evaluation.
- Feature selection that avoids target leakage: `casual` and `registered` are excluded because they are components of `cnt`.
- Gradient-boosted regression with MAE and RMSE reporting.
- A minimal command-line training workflow that is easy to reproduce.

## Pipeline

```text
UCI hour.csv -> chronological sort -> feature selection -> chronological split
             -> HistGradientBoostingRegressor -> MAE/RMSE
```

The model uses season, year, month, hour, holiday, weekday, working-day status, weather situation, temperature, feels-like temperature, humidity, and wind speed.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
mkdir -p data
curl -L -o data/bike-sharing-dataset.zip \
  https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip
unzip -j data/bike-sharing-dataset.zip "*/hour.csv" -d data
python -m src.train --data data/hour.csv
```

The command prints the number of rows, test rows, MAE in rentals, and RMSE in rentals. CI validates the Python source without downloading the dataset.

## Project layout

- `src/train.py` — loading, chronological split, training, and evaluation.
- `.github/workflows/ci.yml` — compile and dependency checks.
- `requirements.txt` — runtime dependencies.

## Data, license, and limitations

Download the official [UCI Bike Sharing dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing). UCI lists it under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode). Citation: Fanaee-T, H. (2013). *Bike Sharing*. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

These are operational mobility records. They support forecasting, not causal claims about weather or working-day status. Production use would require backtesting across multiple time windows, holiday/event features, prediction intervals, drift monitoring, and a comparison against seasonal baselines.

The code is MIT-licensed; the dataset remains under its source terms.
