import subprocess
import optparse
import re
import sys
import json
import os

CONFIG_FILE = "config.json"

# Парсинг аргументов командной строки для ввода сетевого интерфейса и нового MAC-адреса
def parse_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="net_interface", help="Укажите сетевой интерфейс для изменения MAC-адреса")
    parser.add_option("-m", "--mac", dest="target_mac", help="Укажите новый MAC-адрес")
    parser.add_option("-r", "--revert", action="store_true", help="Вернуть оригинальный MAC-адрес")
    args, _ = parser.parse_args()
    # Проверка обязательных аргументов
    if not args.net_interface:
        parser.error("[-] Ошибка: Укажите интерфейс. Используйте --help для помощи.")
    return args

# Проверка правильности формата MAC-адреса 
def validate_mac_address(mac_address):
    mac_pattern = re.compile(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$")
    if not mac_pattern.match(mac_address):
        sys.exit("[-] Ошибка: Некорректный формат MAC-адреса. Пример: 00:11:22:33:44:55")
    return True

# Проверка наличия прав администратора
def is_user_root():
    if not subprocess.geteuid() == 0:
        sys.exit("[-] Ошибка: Скрипт должен быть запущен с правами администратора.")
    return True

# Сохранение оригинального MAC-адреса в конфиг
def save_original_mac(net_interface, mac_address):
    config_data = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config_data = json.load(f)
    config_data[net_interface] = mac_address
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f)
    print("[+] Оригинальный MAC-адрес сохранен в конфигурационном файле.")

# Получение оригинального MAC-адреса из конфиг файла
def get_original_mac(net_interface):
    if not os.path.exists(CONFIG_FILE):
        sys.exit("[-] Ошибка: Файл конфигурации не найден. Невозможно вернуть оригинальный MAC-адрес.")
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)
        if net_interface in config_data:
            return config_data[net_interface]
        else:
            sys.exit(f"[-] Ошибка: Оригинальный MAC-адрес для интерфейса {net_interface} не найден в конфигурации.")

# Изменение MAC-адреса интерфейса
def change_mac(net_interface, target_mac):
    try:
        print(f"[+] Изменение MAC-адреса интерфейса {net_interface} на {target_mac}")
        subprocess.call(["ifconfig", net_interface, "down"])
        subprocess.call(["ifconfig", net_interface, "hw", "ether", target_mac])
        subprocess.call(["ifconfig", net_interface, "up"])
        print("[+] MAC-адрес успешно изменен.")
    except Exception as e:
        print(f"[-] Ошибка при изменении MAC-адреса: {e}")
        sys.exit(1)

# Получение текущего MAC-адреса указанного интерфейса
def retrieve_mac(net_interface):
    try:
        ifconfig_output = subprocess.check_output(["ifconfig", net_interface]).decode('utf-8')
        mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)
        if mac_result:
            return mac_result.group(0)
        else:
            print("[-] Не удалось определить текущий MAC-адрес. Проверьте указанный интерфейс.")
            return None
    except subprocess.CalledProcessError:
        print("[-] Ошибка: Не удалось получить данные интерфейса. Проверьте правильность интерфейса.")
        sys.exit(1)

# Проверка успешности изменения MAC-адреса
def verify_mac_change(net_interface, target_mac):
    current_mac_address = retrieve_mac(net_interface)
    if current_mac_address == target_mac:
        print(f"[+] MAC-адрес подтвержден: {current_mac_address}")
    else:
        print("[-] MAC-адрес не был изменен.")

# Возврат к оригинальному MAC-адресу
def revert_mac(net_interface):
    original_mac = get_original_mac(net_interface)
    print(f"[+] Возврат к оригинальному MAC-адресу: {original_mac}")
    change_mac(net_interface, original_mac)

def main():
    # Проверка прав администратора
    is_user_root()
    
    # Получение аргументов из командной строки
    args = parse_arguments()
    
    # Проверка на флаг возврата оригинального MAC-адреса
    if args.revert:
        revert_mac(args.net_interface)
        return
    
    # Валидация формата MAC-адреса
    if args.target_mac:
        validate_mac_address(args.target_mac)
    
    # Определение текущего MAC-адреса
    current_mac_address = retrieve_mac(args.net_interface)
    print(f"Текущий MAC-адрес: {current_mac_address}")

    # Сохранение оригинального MAC-адреса в конфигурационном файле
    save_original_mac(args.net_interface, current_mac_address)

    # Изменение MAC-адреса на новый
    change_mac(args.net_interface, args.target_mac)

    # Проверка успешного изменения MAC-адреса
    verify_mac_change(args.net_interface, args.target_mac)


if __name__ == "__main__":
    main()
