from flask import Flask
from flask_restful import Resource, Api, reqparse

from parseAuthorsPlainTexts import parse_all_texts, parse_file

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


class ParseAndSave(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()

            parser.add_argument('name')
            parser.add_argument('title')
            parser.add_argument('text')
            args = parser.parse_args()

            name = args['name']
            text = args['text']
            title = args['title']
            print args
            save_text_as_file('./texts/' + name + '_' + title, text)
            return "OK"

            # parse_all_texts('./texts')

        except Exception as e:
            return {'error': str(e)}


api.add_resource(ParseAndSave, '/parseAndSave')


class Parse(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('text')
            args = parser.parse_args()
            text = args['text']
            print(args)
            save_text_as_file('./texts/toDetectFile', str(text))
            parse_file('./texts/toDetectFile', 'toDetect')
            return "OK"

        except Exception as e:
            return {'error': str(e)}


api.add_resource(Parse, '/parse')


def save_text_as_file(name, text):
  file = open(name, "w")
  file.write(text)
  file.write("\n")
  file.close()

if __name__ == '__main__':
    app.run(port=7001)
