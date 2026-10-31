"""Forecast hourly bike rentals from the official UCI Bike Sharing data."""
from __future__ import annotations
import argparse
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to official hour.csv")
    args = parser.parse_args()
    df = pd.read_csv(args.data).sort_values(["dteday", "hr"]).reset_index(drop=True)
    features = ["season", "yr", "mnth", "hr", "holiday", "weekday", "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"]
    split = int(len(df) * 0.8)
    model = HistGradientBoostingRegressor(max_iter=200, random_state=42)
    model.fit(df[features].iloc[:split], df["cnt"].iloc[:split])
    prediction = model.predict(df[features].iloc[split:])
    actual = df["cnt"].iloc[split:]
    print(f"rows={len(df)} test_rows={len(actual)}")
    print(f"MAE rentals={mean_absolute_error(actual, prediction):.2f}")
    print(f"RMSE rentals={root_mean_squared_error(actual, prediction):.2f}")


if __name__ == "__main__":
    main()
