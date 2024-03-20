import json
from calculate import calculate

def main(request):
    if request.method != 'POST':
        return json.dumps({'error': 'Método não permitido'}), 405

    try:
        request_json = request.get_json()
        # num1 = request_json.get('num1')
        # num2 = request_json.get('num2')
        # operator = request_json.get('operator')
    except Exception as e:
        return json.dumps({'error': f'Erro ao processar o JSON da requisição. {e}'}), 400

    # if not num1 or not num2 or operator is None:
    #     return json.dumps({'error': 'num1, num2 e operador são obrigatórios'}), 400

    num1 = 2
    num2 = 3
    operator = '^'
    result = calculate(num1, num2, operator)

    return json.dumps({'operacao_realizada': f'{num1}{operator}{num2}', 'resultado': result}), 200