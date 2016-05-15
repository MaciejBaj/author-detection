from __future__ import division

from parser.MongoCollection import MongoCollection
from parser.utils import update_and_return_json


class Benchmarker:

  def __init__(self):
    self.mongoCollection = MongoCollection()

  def benchmark(self, classes, classification_method, fields):
    all_records = self.mongoCollection.get_all_records()
    if all_records < 2:
      return
    print reduce(lambda res, class_name:
               update_and_return_json(res,
                                      class_name,
                                      self.create_accuracy_ranking(all_records,
                                                              fields,
                                                              class_name,
                                                              classification_method)), classes, {})

  def create_accuracy_ranking(self, records, features_to_benchmark, class_name, delivered_classification_method):
    def increment_if_successful_classified(score, record, feature):
      if record['classes'][class_name] == delivered_classification_method(record, class_name, feature, [x for x in records if x != record]):
        score += 1
      return score

    return reduce(lambda result, feature:
           update_and_return_json(result, feature,
                                  reduce(lambda score, record: increment_if_successful_classified(score, record, feature),
                                         records, 0) / (len(records) - 1)), features_to_benchmark, {})