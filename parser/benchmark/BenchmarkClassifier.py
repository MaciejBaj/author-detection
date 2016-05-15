import json, numpy, yaml

from sklearn.feature_selection import SelectKBest, f_classif, chi2

from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV

from parser.classification.NumericalFeaturesClassifier import select_numerical_characteristics, \
  numerical_characteristics


def classify_with_one_property_only(to_detect_position, class_name, property_name, training_set):
  target_value = to_detect_position[property_name]
  class_names = map(lambda x: x["classes"][class_name], training_set)
  distances_to_target = map(lambda x: abs(target_value - x[property_name]), training_set)
  return class_names[distances_to_target.index(min(distances_to_target))]


def select_k_best_features_using_univariate_selection(class_name, k_best_features, training_set):
  class_names = map(lambda x: x["classes"][class_name], training_set)
  numerical_characteristics_training_set = map(lambda x: x, map(lambda x: select_numerical_characteristics(x), training_set))
  X_new = SelectKBest(f_classif, k=k_best_features).fit_transform(numerical_characteristics_training_set, class_names)
  best_features_indexes = map(lambda x: numerical_characteristics_training_set[0].index(x), X_new[0])
  return map(lambda i: numerical_characteristics[i], best_features_indexes)


#http://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#example-feature-selection-plot-rfe-with-cross-validation-py
def adjust_optimal_features_using_recursive_feature_elimination(class_name, training_set):
  class_names = map(lambda x: x["classes"][class_name], training_set)
  numerical_characteristics_training_set = map(lambda x: x, map(lambda x: select_numerical_characteristics(x), training_set))
  # Create the RFE object and compute a cross-validated score.
  svc = SVC(kernel="linear")
  # The "accuracy" scoring is proportional to the number of correct classifications
  rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(class_names, 2), scoring='accuracy')
  # ToDo: check if class has more than one representant always
  rfecv.fit(numerical_characteristics_training_set, class_names)
  optimal_features_indexes = [i for i, x in enumerate(rfecv.ranking_) if x == 1]
  print("Optimal number of features : %d" % rfecv.n_features_)
  return map(lambda i: numerical_characteristics[i], optimal_features_indexes)
    # X_new.shape