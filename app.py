from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, '')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      f.save(filename)
      subprocess.call("rm -f ./a.out", shell=True) 
      retcode = subprocess.call('g++ '+ filename, shell=True)
      if retcode:
         return '<h2>Failed to compile ' + filename + "</h2>"
         exit
      retcode = subprocess.call("./test.sh", shell=True)
      feedback = "<h2>SCORE: " + str(retcode) + " out of 2 correct.</h2><br>" 
      feedback += "<h2>Original Submission</h2>"
      with open('walk.cc','r') as fs:
         for line in fs:
            feedback+= line + "<br>"
      return feedback
		
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
