from parseAuthorsPlainTexts import parse_all_texts, parse_file

def save_text_as_file(name, text):
  file = open(name, "w")
  file.write(text)
  file.write("\n")
  file.close()

if __name__ == '__main__':
    parse_file('./texts/toDetectFile')
