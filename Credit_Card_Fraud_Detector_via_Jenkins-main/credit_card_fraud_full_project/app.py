from __future__ import annotations

import os
from typing import List

import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = "model.pkl"
SCALER_PATH = "scaler.pkl"

model = None
scaler = None
load_error = None

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as exc:
    load_error = str(exc)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    error = None
    values = {}

    if request.method == "POST":
        try:
            raw_values: List[float] = []
            for i in range(1, 31):
                field_name = f"feature{i}"
                value = request.form.get(field_name, "").strip()
                values[field_name] = value
                raw_values.append(float(value))

            if model is None or scaler is None:
                raise RuntimeError(
                    f"Model or scaler not loaded correctly. Details: {load_error}"
                )

            input_array = np.array(raw_values, dtype=float).reshape(1, -1)
            scaled_input = scaler.transform(input_array)
            pred = int(model.predict(scaled_input)[0])

            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(scaled_input)[0]
                confidence = round(float(np.max(probs)) * 100, 2)

            prediction = "Fraudulent Transaction" if pred == 1 else "Legitimate Transaction"

        except ValueError:
            error = "Please enter valid numeric values in all 30 fields."
        except Exception as exc:
            error = f"Error: {exc}"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        error=error,
        values=values,
    )


@app.route("/health")
def health():
    ok = model is not None and scaler is not None
    return {
        "status": "ok" if ok else "error",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None,
        "details": load_error,
    }, (200 if ok else 500)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
