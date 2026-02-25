import joblib
from sklearn.linear_model import LogisticRegression

def train():
    model = LogisticRegression()
    X = [[0,0],[1,1]]
    y = [0,1]
    model.fit(X,y)
    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()
