from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests, json, time
from parser.classification.ClassifierAggregator import ClassifierAggregator
from recordsSaver import create_new_record, save_in_db
from flask.ext.cors import CORS

wcrft2_api_download_url = 'http://ws.clarin-pl.eu/nlprest/base/downloadbin/'
CLARINS_URL = 'http://ws.clarin-pl.eu/nlprest/base'


def get_record_from_request(classes):
  headers = {'content-type': 'application/json'}
  parser = reqparse.RequestParser()
  parser.add_argument('text')
  args = parser.parse_args()
  text = args['text'].encode('utf-8')
  uploaded_file_token = requests.post(CLARINS_URL + '/upload', data=text, headers=headers)
  print "got uploaded token: " + uploaded_file_token.content
  task_status_token = requests.get(CLARINS_URL + '/startTask/wcrft2/' + uploaded_file_token.content, headers=headers)
  print "waiting for WCRFT ..."
  status_response = requests.get(CLARINS_URL + '/getStatus/' + task_status_token.content, headers=headers)
  while json.loads(status_response.content)['status'] != 'DONE':
    time.sleep(5)
    status_response = requests.get(CLARINS_URL + '/getStatus/' + task_status_token.content, headers=headers)
  print "WCRFT done. Downloading XML ..."
  wcrft_response = requests.get(wcrft2_api_download_url + json.loads(status_response.content)['value'], headers=headers)
  print "WCRFT XML downloaded. Processing ..."
  return create_new_record(wcrft_response.content, classes, text)


class Recognize(Resource):
  def post(self):
    try:
      print "received recognize request"
      classes_to_guess = {"author": "true", "type": "true", "age": "false", "male": "false"}
      to_detect = get_record_from_request(classes_to_guess)
      return ClassifierAggregator().full_classification(to_detect)

    except Exception as e:
      return {'error': str(e)}


class Parse(Resource):
  def post(self):
    try:
      parser = reqparse.RequestParser()
      parser.add_argument('author')
      parser.add_argument('type')
      parser.add_argument('male')
      parser.add_argument('age')
      args = parser.parse_args()
      save_in_db(get_record_from_request({
        'author': args['author'].encode('utf-8'),
        'type': args['type'].encode('utf-8'),
        'male': args['male'].encode('utf-8'),
        'age': args['age'].encode('utf-8')
      }))
      return "OK"

    except Exception as e:
      return {'error': str(e)}


if __name__ == '__main__':
  app = Flask(__name__)
  api = Api(app)
  api.add_resource(Recognize, '/recognize')
  api.add_resource(Parse, '/parse')
  app.run(port=7001)
  CORS(app)
