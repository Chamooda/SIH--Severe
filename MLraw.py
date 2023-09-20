# Importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from urllib.parse import urlparse

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Logistic Regression
class PhishingWebsiteDetector():
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, Y):
        self.m, self.n = X.shape
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        for i in range(self.iterations):
            self.update_weights()
        return self

    def update_weights(self):
        A = 1 / (1 + np.exp(-(self.X.dot(self.W) + self.b)))
        tmp = (A - self.Y.T)
        tmp = np.reshape(tmp, self.m)
        dW = np.dot(self.X.T, tmp) / self.m
        db = np.sum(tmp) / self.m

        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

        return self

    def predict(self, X):
        Z = 1 / (1 + np.exp(-(X.dot(self.W) + self.b)))
        Y = np.where(Z > 0.5, 1, 0)
        return Y

# Driver code
def main():
    # Importing dataset
    df = pd.read_csv("verified_online.csv")  # Replace with your dataset file path

    df['DomainLength'] = df['url'].apply(lambda x: len(urlparse(x).netloc))

    # Extracting features and labels
    features = df.drop(columns=["target"])
    labels = df["target"]

    # Encode the target website labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)

    # Data preprocessing
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    # Splitting dataset into train and test set
    X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

    # Model training
    model = PhishingWebsiteDetector(learning_rate=0.01, iterations=1000)
    model.fit(X_train, Y_train)

    # Prediction on test set
    Y_pred = model.predict(X_test)

    # Model evaluation
    accuracy = accuracy_score(Y_test, Y_pred)
    confusion = confusion_matrix(Y_test, Y_pred)
    report = classification_report(Y_test, Y_pred)

    print("Accuracy on test set:", accuracy * 100)
    print("Confusion Matrix:\n", confusion)
    print("Classification Report:\n", report)

if __name__ == "__main__":
    main()
