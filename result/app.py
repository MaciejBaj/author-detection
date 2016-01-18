from flask import Flask
from flask_restful import Resource, Api, reqparse
from classifier import classify_with_db_training_set


app = Flask(__name__)
api = Api(app)

class Classify(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('characteristics', type=str, help='text input characteristics')
            args = parser.parse_args()

            characteristics = args['characteristics']
            classify_with_db_training_set(characteristics)
            print(characteristics)
            if characteristics == None:
                 return {'error': 'empty characteristics'}
            return {'characteristics': characteristics}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(Classify, '/classify')

if __name__ == '__main__':
    app.run(port=7002)
