import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("./features/global_features.csv")

X = df.drop(columns=["pdbid", "binding_affinity"])
y = df["binding_affinity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

model = GradientBoostingRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)

rmse = mean_squared_error(y_test, pred, squared=False)
print("RMSE:", rmse)
