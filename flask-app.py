from flask import Flask, request, jsonify
from AreaCalculater import calculate_area_in_acres

app = Flask('__main__')

'''
A function to get the request using flask and return 
the calculated are in acres.
'''
@app.route('/', methods=['GET', 'POST'])
def get_input():

    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']
    area = calculate_area_in_acres(length, width)
    return jsonify(area) 

if __name__ == '__main__':
    app.run()