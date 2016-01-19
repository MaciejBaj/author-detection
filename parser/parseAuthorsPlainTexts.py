import shutil
from os import listdir
from os.path import isfile, join

from xmlParser import XmlParser
from trainingSetParser import save_characteristics_in_db, clear_characteristics_collection, clear_author_characteristics

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
    save_characteristics_in_db(texts_path + '/' + author_text, author_name, xml_file_path)


def parse_file(path, name):
    xml_file_path = './xmlResults/' + name + '.xml'
    XmlParser.produce_xml_with_morphological_data(path, xml_file_path)
    clear_author_characteristics(name)
    save_characteristics_in_db(path, name, xml_file_path)