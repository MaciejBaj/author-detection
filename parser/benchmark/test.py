from parser.MongoCollection import MongoCollection
from parser.classification.ClassifierAggregator import ClassifierAggregator


mongoCollection = MongoCollection()


def test_classification():
  to_detect = mongoCollection.get_first_from_db()
  to_detect["classes"] = {"author": "true", "type": "true", "age": "false", "male": "false"}
  return ClassifierAggregator().full_classification(to_detect)
