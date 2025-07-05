import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load crater data
df = pd.read_csv(r"D:\CV\run\crater_outputs\profiles\crater_metrics.csv")

# Extract diameter and depth
D = df["diameter_m"].values.reshape(-1, 1)
d = df["depth_m"].values.reshape(-1, 1)

# (a) Regression for all craters
model_all = LinearRegression().fit(D, d)
d_pred_all = model_all.predict(D)
r2_all = model_all.score(D, d)
m_all = model_all.coef_[0][0]
c_all = model_all.intercept_[0]

# ─── Plotting ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))

# (a) Depth–Diameter regression
ax.scatter(D, d, color='black')
ax.plot(D, d_pred_all, color='red')
ax.set_title("Depth–Diameter Relationship")
ax.set_xlabel("Diameter (m)")
ax.set_ylabel("Depth (m)")
ax.grid(True)
ax.text(0.05, 0.95,
        f"d = {m_all:.4f}*D + {c_all:.1f}\nR² = {r2_all:.2f}",
        transform=ax.transAxes,
        verticalalignment='top',
        bbox=dict(facecolor="white", edgecolor="gray"))

plt.tight_layout()
plt.show()
