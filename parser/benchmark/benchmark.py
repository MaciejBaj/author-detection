from parser.benchmark.CommonWordsBenchmarker import CommonWordsBenchmarker
from parser.benchmark.NumericalFeaturesBenchmarker import NumericalFeaturesBenchmarker
from parser.benchmark.PartsOfSpeechBenchmarker import PartsOfSpeechBenchmarker

# http://scikit-learn.org/stable/modules/feature_selection.html

NumericalFeaturesBenchmarker().benchmark(['age', 'type', 'author'])
PartsOfSpeechBenchmarker().benchmark(['age', 'type', 'author'])
CommonWordsBenchmarker().benchmark(['age', 'type', 'author'])

