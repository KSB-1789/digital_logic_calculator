from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry = AND(a, b)
    return sum_bit, carry

def full_adder(a, b, cin):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, cin)
    return sum2, OR(carry1, carry2)

def half_subtractor(a, b):
    diff = XOR(a, b)
    borrow = AND(NOT(a), b)
    return diff, borrow

def full_subtractor(a, b, bin):
    diff1, borrow1 = half_subtractor(a, b)
    diff2, borrow2 = half_subtractor(diff1, bin)
    return diff2, OR(borrow1, borrow2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = bool(int(data.get('a', 0)))
    b = bool(int(data.get('b', 0)))
    cin = bool(int(data.get('cin', 0)))  # For full adder/subtractor

    result = {
        'error': None,
        'outputs': {}
    }

    try:
        if operation == 'AND':
            result['outputs']['output'] = int(AND(a, b))
        elif operation == 'OR':
            result['outputs']['output'] = int(OR(a, b))
        elif operation == 'NOT':
            result['outputs']['output'] = int(NOT(a))
        elif operation == 'NAND':
            result['outputs']['output'] = int(NAND(a, b))
        elif operation == 'NOR':
            result['outputs']['output'] = int(NOR(a, b))
        elif operation == 'XOR':
            result['outputs']['output'] = int(XOR(a, b))
        elif operation == 'half_adder':
            sum_bit, carry = half_adder(a, b)
            result['outputs']['sum'] = int(sum_bit)
            result['outputs']['carry'] = int(carry)
        elif operation == 'full_adder':
            sum_bit, carry = full_adder(a, b, cin)
            result['outputs']['sum'] = int(sum_bit)
            result['outputs']['carry'] = int(carry)
        elif operation == 'half_subtractor':
            diff, borrow = half_subtractor(a, b)
            result['outputs']['difference'] = int(diff)
            result['outputs']['borrow'] = int(borrow)
        elif operation == 'full_subtractor':
            diff, borrow = full_subtractor(a, b, cin)
            result['outputs']['difference'] = int(diff)
            result['outputs']['borrow'] = int(borrow)
    except Exception as e:
        result['error'] = str(e)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 