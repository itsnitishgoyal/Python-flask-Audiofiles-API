from flask import Flask,jsonify,request
from flask_restful import Api,Resource
import logging
from resources.audiofiles import audiofiles
from resources.audiorestoperations import audiorestoperations
from resources.getallaudiofiles import getallfiles

logging.basicConfig(filename="main_music" + '.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

app = Flask(__name__)
api=Api(app)



logging.info("app started")
api.add_resource(audiofiles,'/audiofiles')
api.add_resource(audiorestoperations,'/audiofiles/<string:audioFileType>/<int:audioFileID>')
api.add_resource(getallfiles,'/audiofiles/<string:audioFileType>')

if __name__ == "__main__":
    app.run(port=81325)