from parser.benchmark.BenchmarkClassifier import adjust_optimal_features_using_recursive_feature_elimination, \
  classify_with_one_property_only, select_k_best_features_using_univariate_selection
from parser.benchmark.Benchmarker import Benchmarker
from parser.classification.NumericalFeaturesClassifier import numerical_characteristics
from parser.utils import update_and_return_json


class NumericalFeaturesBenchmarker(Benchmarker):

  def benchmark(self, classes):
    print "\nSIMPLE CHARACTERISTICS BENCHMARKING:"
    Benchmarker.benchmark(self, classes, classify_with_one_property_only, numerical_characteristics)
    print "CREATING SELF-MADE ACCURACY RANKING FOR SIMPLE CHARACTERISTICS FOR CLASSES FOR EACH RECORD IN DB"
    self.select_k_best_numerical_features_using_univariate_feature_selection(classes)
    self.select_optimal_features_set_using_univariate_feature_selection(['age'])

  def select_optimal_features_set_using_univariate_feature_selection(self, classes):

    print "SELECTING OPTIMAL FEATURES SET USING RECURSIVE FEATURE ELIMINATION"
    print reduce(lambda result, class_name:
                 update_and_return_json(result,
                                        class_name,
                                        adjust_optimal_features_using_recursive_feature_elimination(class_name,
                                                                                                    self.mongoCollection.get_all_records())),
                 classes,
                 {})

  def select_k_best_numerical_features_using_univariate_feature_selection(self, classes, k=4):
    print "SELECTING ", k, " BEST FEATURES FOR: ", classes, " USING UNIVARIATE FEATURE SELECTION"

    def assign_value(result, class_name):
      result[class_name] = select_k_best_features_using_univariate_selection(class_name, k, self.mongoCollection.get_all_records())
      return result

    print reduce(assign_value, classes, {})
