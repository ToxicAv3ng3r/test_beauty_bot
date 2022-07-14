from flask import Flask, jsonify, request

app = Flask(__name__)


def func_1():
    dct = {
        'func_name': 'func_1',
        'message': 'Успех!'
    }
    return dct


def func_2():
    dct = {
        'func_name': 'func_2',
        'message': 'Успех!'
    }
    return dct


func_dict = {'func_1': func_1, 'func_2': func_2}


@app.route('/Datalore', methods=['POST'])
def get_func_by_name():
    func_name = request.json['function']
    res = func_dict[func_name]()
    return jsonify(res)


if __name__ == '__main__':
    app.run()
