import xml.etree.ElementTree as ET
import os
# https://github.com/CenturyLinkLabs/panamax-ui/wiki/How-To%3A-Port-Forwarding-on-VirtualBox

class XmlParser:
  tree = 0

  def __init__(self, xml_file_path):
    self.root = ET.parse(xml_file_path).getroot()

  def get_number_of_words(self):
    return [base_word for base_word in self.root.iter('base')].__len__()

  def get_base_form_words(self):
    return [base_word.text for base_word in self.root.iter('base')]

  def get_parts_of_speech_frequency(self):
    part_of_speech_counter = {}
    for tag in self.root.iter('ctag'):
      part_of_speech = tag.text.split(':')[0]
      if part_of_speech in part_of_speech_counter:
        part_of_speech_counter[part_of_speech] += 1
      else:
        part_of_speech_counter[part_of_speech] = 1

    all_words_length = self.get_number_of_words()
    for name in part_of_speech_counter:
      part_of_speech_counter[name] /= float(all_words_length)

    return part_of_speech_counter

  @staticmethod
  def produce_xml_with_morphological_data(text_file_path, output_file_path):
    os.system("~/apps/wcrft/wcrft/wcrft.py -d ~/apps/model_nkjp10_wcrft/ ~/apps/wcrft/config/nkjp.ini -i txt " +
              text_file_path + " -O " + output_file_path)
