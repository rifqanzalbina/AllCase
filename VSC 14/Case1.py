from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score  

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.3, random_state=50)

clf = DecisionTreeClassifier(random_state=50)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Akurasi model adalah : ", accuracy)