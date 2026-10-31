# Bike Sharing Demand Forecast

A real-world regression project using hourly Capital Bikeshare rental counts from 2011–2012, with weather and calendar covariates.

## Data source and attribution

Download the official [UCI Bike Sharing dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing) from [this data URL](https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip).

UCI lists the dataset under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode). Citation: Fanaee-T, H. (2013). Bike Sharing. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

## Run

```bash
pip install -r requirements.txt
python -m src.train --data data/hour.csv
```

The script uses a chronological split, predicts `cnt` (total rentals), excludes `casual` and `registered` because they are components of the target, and reports MAE and RMSE.

The observations are operational mobility records. They support forecasting, not causal claims about weather or working-day status. The original code is MIT-licensed; the dataset remains under its source terms.
