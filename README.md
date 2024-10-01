# EN
**GenMacChanger** is a Python tool that allows you to change your network interface's MAC address with ease. It provides functionalities to save the original MAC address in a config file and restore it whenever needed. This tool is useful for testing purposes, security audits, or to improve anonymity.

## Features
- **Change MAC Address**: Change the MAC address of your specified network interface.
- **Save Original MAC Address**: Automatically save the original MAC address before any changes are made.
- **Restore Original MAC Address**: Revert to the saved original MAC address whenever needed.
- **User-Friendly**: Easy command-line interface for changing and restoring MAC addresses.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/geniuszly/GenMacChanger
    cd GenMacChanger
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To change the MAC address of a network interface:

```bash
sudo python3 main.py -i [INTERFACE] -m [NEW_MAC]
```
- **-i, --interface**: The network interface to change the MAC address (e.g., `eth0`).
- **-m, --mac**: The new MAC address to be assigned (e.g., `00:11:22:33:44:55`).

### Example:
```bash
sudo python3 main.py -i eth0 -m 00:11:22:33:44:55
```

### Example output
```
[+] Текущий MAC-адрес: 11:22:33:44:55:66
[+] Сохранение оригинального MAC-адреса в config.json
[+] Изменение MAC-адреса интерфейса eth0 на 00:11:22:33:44:55
[+] MAC-адрес успешно изменен.
[+] MAC-адрес подтвержден: 00:11:22:33:44:55
```

The tool will change the MAC address and save the original in a `config.json` file for easy restoration later.

## Revert MAC Address
To revert back to the original MAC address:
```bash
sudo python3 main.py -i [INTERFACE] -r
```
- **-r, --revert**: Use this option to restore the original MAC address.

### Example:
```bash
sudo python3 main.py -i eth0 -r
```

### Example output
```
[+] Оригинальный MAC-адрес из config.json: 11:22:33:44:55:66
[+] Возврат к оригинальному MAC-адресу: 11:22:33:44:55:66
[+] MAC-адрес успешно изменен.
[+] MAC-адрес подтвержден: 11:22:33:44:55:66
```

# RU
**GenMacChanger** — это инструмент на Python, позволяющий изменять MAC-адрес вашего сетевого интерфейса. Программа автоматически сохраняет оригинальный MAC-адрес в конфигурационный файл и позволяет при необходимости вернуть его обратно. Это полезно для тестирования, аудита безопасности или повышения анонимности.

## Особенности
- **Изменение MAC-адреса**: Смените MAC-адрес указанного сетевого интерфейса.
- **Сохранение оригинального MAC-адреса**: Автоматическое сохранение текущего MAC-адреса перед его изменением.
- **Восстановление оригинального MAC-адреса**: Возможность вернуть MAC-адрес к сохраненному.
- **Простота использования**: Удобный интерфейс командной строки.

## Установка
1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/geniuszly/GenMacChanger
    cd GenMacChanger
    ```

2. **Установите необходимые зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

## Использование
Для изменения MAC-адреса сетевого интерфейса:

```bash
sudo python3 main.py -i [ИНТЕРФЕЙС] -m [НОВЫЙ_MAC]
```
- **-i, --interface**: Сетевой интерфейс, на котором будет изменен MAC-адрес (например, `eth0`).
- **-m, --mac**: Новый MAC-адрес (например, `00:11:22:33:44:55`).

### Пример:
```bash
sudo python3 main.py -i eth0 -m 00:11:22:33:44:55
```

### Пример вывода
```
[+] Текущий MAC-адрес: 11:22:33:44:55:66
[+] Сохранение оригинального MAC-адреса в config.json
[+] Изменение MAC-адреса интерфейса eth0 на 00:11:22:33:44:55
[+] MAC-адрес успешно изменен.
[+] MAC-адрес подтвержден: 00:11:22:33:44:55
```

Инструмент изменит MAC-адрес и сохранит оригинальный в `config.json`, чтобы его можно было легко восстановить.

## Восстановление MAC-адреса
Чтобы вернуть оригинальный MAC-адрес:
```bash
sudo python3 main.py -i [ИНТЕРФЕЙС] -r
```
- **-r, --revert**: Используйте этот флаг для возврата оригинального MAC-адреса.

### Пример:
```bash
sudo python3 main.py -i eth0 -r
```

### Пример вывода
```
[+] Оригинальный MAC-адрес из config.json: 11:22:33:44:55:66
[+] Возврат к оригинальному MAC-адресу: 11:22:33:44:55:66
[+] MAC-адрес успешно изменен.
[+] MAC-адрес подтвержден: 11:22:33:44:55:66
```
