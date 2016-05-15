import shutil
from os import listdir
from os.path import isfile, join

from XmlParser import XmlParser
from trainingSetParser import add_new_record, clear_characteristics_collection, clear_author_characteristics

texts_path = './texts'

def parse_all_texts(texts_path):
  author_text_files = [f for f in listdir(texts_path) if isfile(join(texts_path, f))]

  clear_characteristics_collection()
  # todo: uncomment when VB with morphological parsing will be enabled
  shutil.rmtree('./xmlResults/')
  for author_text in author_text_files:
    author_name = author_text.split('_')[0]
    xml_file_path = './xmlResults/' + author_name + '.xml'
    # todo: uncomment when VB with morphological parsing will be enabled
    XmlParser.produce_xml_with_morphological_data(texts_path + '/' + author_text, xml_file_path)
    add_new_record(texts_path + '/' + author_text, author_name, xml_file_path)


def parse_file(path, name):
    xml_file_path = './xmlResults/' + name + '.xml'
    print "parsing by WCRFT ..."
    XmlParser.produce_xml_with_morphological_data(path, xml_file_path)
    print "parsed by WCRFT ..."
    clear_author_characteristics(name)
    print "saving in db..."
    add_new_record(path, name, xml_file_path)