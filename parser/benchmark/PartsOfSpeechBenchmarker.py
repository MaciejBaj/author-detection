from parser.benchmark.Benchmarker import Benchmarker
from parser.classification.PartsOfSpeechClassifier import PartsOfSpeechClassifier


class PartsOfSpeechBenchmarker(Benchmarker):

  def benchmark(self, classes):
    print "\nPARTS OF SPEECH BENCHMARKING:"
    Benchmarker.benchmark(self, classes, PartsOfSpeechClassifier.classify, ["parts_of_speech_frequencies"])

