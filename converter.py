import json
import argparse
import sys

def parse_json(input_data):
    try:
        return json.loads(input_data)
    except json.JSONDecodeError as e:
        print(f"Ошибка синтаксиса JSON: {e}", file=sys.stderr)
        sys.exit(1)

def convert_to_custom_language(data):
    output = []
    if isinstance(data, dict):
        for key, value in data.items():
            output.append(f"var {key} {convert_value(value)}")
    return "\n".join(output)

def convert_value(value):
    if isinstance(value, str):
        return f'@"{value}"'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        return f'list({", ".join(map(convert_value, value))})'
    elif isinstance(value, dict):
        return convert_to_custom_language(value)
    else:
        raise ValueError(f"Неизвестный тип значения: {value}")

def main():
    parser = argparse.ArgumentParser(description='Конвертер JSON в учебный конфигурационный язык.')
    parser.add_argument('output_file', type=str, help='Путь к выходному файлу')
    args = parser.parse_args()

    input_data = sys.stdin.read()
    json_data = parse_json(input_data)
    custom_language_output = convert_to_custom_language(json_data)

    with open(args.output_file, 'w') as f:
        f.write(custom_language_output)

if __name__ == '__main__':
    main()
