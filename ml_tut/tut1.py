import pandas as pd
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score


def main():
    # Gather data
    df = pd.read_csv(r'C:\Users\nekiv\Documents\GitHub\Python\ml_tut\Churn.csv')

    x = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
    y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)
    x_train.head()
    y_train.head()

    # Build model
    model = Sequential()
    model.add(Dense(units=32, activation='relu', input_dim=len(x_train.columns)))  # adding hidden layer neurons=32
    model.add(Dense(units=64, activation='relu'))  # adding hidden layer neurons=64
    model.add(Dense(units=1, activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

    # Train the model on the existing data
    model.fit(x_train, y_train, epochs=200, batch_size=32)

    # predict
    y_hat = model.predict(x_test)
    y_hat = [0 if val < 0.5 else 1 for val in y_hat]

    # evaluate
    score = accuracy_score(y_test, y_hat)

    # Save the data
    model.save(r'C:\Users\nekiv\Documents\GitHub\Python\ml_tut\tfmodel')
    return x_test, x_train, y_test, y_train, y_hat, model


if __name__ == '__main__':
    main()
