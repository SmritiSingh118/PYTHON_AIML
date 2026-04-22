 from sklearn.tree import DecisionTreeClassifier
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

from sklearn.datasets import make_classification

X, y = make_classification(n_samples=5000, n_features=5, n_informative=5, 
                           n_redundant=0, n_repeated=0, n_classes=3, 
                           n_clusters_per_class=1, random_state=42)

print(f"Shape of features (X): {X.shape}")
print(f"Shape of target (y): {y.shape}")
print(f"Number of classes: {len(set(y))}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dtc=DecisionTreeClassifier(criterion='entropy')
y_pred=dtc.predict(X_test)
y_test
accuracy_score(y_test,y_pred)
precision_score(y_test,y_pred,average='weighted')
recall_score(y_test, y_pred,average='weighted')
f1_score(y_test, y_pred,average='weighted')
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
