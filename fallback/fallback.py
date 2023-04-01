from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/get-result')
def get_result():
    try:
        args = request.args
                
        petal_length= args.get('petal_length', default='0')
        
        if int(petal_length) < 2.5:
            return Response(response='iris-setosa', status=200, mimetype='application/json')
        else:
            return Response(response='iris-versicolor', status=200, mimetype='application/json')
    except:
        return Response(response="", status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run("0.0.0.0")