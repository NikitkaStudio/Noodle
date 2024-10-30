import sys
import subprocess
import importlib

def run_file(file_path):
    try:
        if file_path.endswith('.py'):
            subprocess.run(['python', file_path])
        else:
            with open(file_path, 'r') as file:
                code = file.read()
                execute_code(code)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")

def execute_code(code):
    lines = code.splitlines()
    for line in lines:
        line = line.strip()
        
        if line.startswith("printLine"):
            text = line[len("printLine "):].strip().strip('"')
            print(text)
        elif line.startswith("pause"):
            print("Нажмите любую кнопку, чтобы продолжить выполнение")
            input()  # Ожидаем нажатия клавиши
        elif line.startswith("import "):
            module_name = line[len("import "):].strip()
            try:
                importlib.import_module(module_name)
                print(f"Модуль '{module_name}' импортирован.")
            except ModuleNotFoundError:
                print(f"Ошибка: Модуль '{module_name}' не найден.")
        else:
            try:
                # Выполняем Python код
                exec(line)
            except Exception as e:
                print(f"Ошибка выполнения кода: {e}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run':
        print("Использование: python noodle.py run <файл.noodles или файл.py>")
        return

    file_path = sys.argv[2]
    run_file(file_path)

if __name__ == '__main__':
    main()
