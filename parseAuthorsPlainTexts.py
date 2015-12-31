import shutil
from os import listdir
from os.path import isfile, join

from trainingSetParser import save_characteristics_in_db, clear_characteristics_collection

texts_path = './texts'
author_text_files = [f for f in listdir(texts_path) if isfile(join(texts_path, f))]

clear_characteristics_collection()
# todo: uncomment when VB with morphological parsing will be enabled
# shutil.rmtree('./xmlResults/')
for author_text in author_text_files:
  author_name = author_text.split('_')[0]
  xml_file_path = './xmlResults/' + author_name + '.xml'
  # todo: uncomment when VB with morphological parsing will be enabled
  # XmlParser.produce_xml_with_morphological_data(texts_path + '/' + author_text, './xmlResults/' + author_name + '.xml')
  save_characteristics_in_db(texts_path + '/' + author_text, author_name, xml_file_path)
