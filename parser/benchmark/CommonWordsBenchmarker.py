from parser.benchmark.Benchmarker import Benchmarker
from parser.classification.CommonWordsClassifier import CommonWordsClassifier


class CommonWordsBenchmarker(Benchmarker):

  def benchmark(self, classes):
    print "\nTOP WORDS USED BENCHMARKING:"
    Benchmarker.benchmark(self, classes, CommonWordsClassifier.classify, ["base_words"])

