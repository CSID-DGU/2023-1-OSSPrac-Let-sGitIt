from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  # default URL
def main():
   return render_template('main.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      
      result['Name'] = request.form.get('name')

      result['Number'] = request.form.get('number')
      
      result['Major'] = request.form.get('major')
      
      result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')

      result['Gender'] = request.form.get('gender')
      
      result['languages'] = ', '.join(request.form.getlist('chkbox'))
      
      return render_template("result.html", result = result)

if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug = True)