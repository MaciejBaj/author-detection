from __future__ import division
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer
different_a = {"x": 2, "y": 1, "unseen_feature": 1}
a = {"x": 2, "z": 2, "w": 1}
b = {"a": 1, "b": 2}
c = {"a": 1, "y": 4}

vectorizer = DictVectorizer(sparse=False)
X_training = vectorizer.fit_transform([a, b, c])
#converse DictVectorizer to behave similar as TfidVectorizer (tf feature)
X_training = map(lambda arr: map(lambda x: x / len(arr), arr), X_training)
print vectorizer.inverse_transform(X_training)

X_test = vectorizer.transform(different_a)

y = np.array(["a", "b", "c"])
clf = MultinomialNB()
clf.fit(X_training, y)

print(clf.predict(X_test))
