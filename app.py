from flask import Flask ,request,Response,jsonify
from sentiment import Sentimet_Analysis
app = Flask(__name__) 


@app.route('/',methods = [ 'GET']) 
def index(): 
    if request.method == 'GET': 
        sentence = request.args.get('sentence') 
        response= jsonify(
            Intention = Sentimet_Analysis(sentence),
            sentence=sentence
        )
        print(response)
        return Response(response.get_data(as_text=True),status=200,mimetype='application/json')
    else: 
        return Response("Method Not Allowed",status=405)

if __name__ == '__main__': 
    app.run(debug = True) 
