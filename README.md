# Winrm-and-SMBv1-Scanner-
Этот репозиторий содержит два сканера для корпоративной сети:

- **WinRM Scanner** – сканирует порты 5985/5986 для проверки службы WinRM.
- **SMBv1 Scanner** – сканирует порт 445 с использованием nmap-скрипта `smb-protocols` для определения статуса SMBv1.

При запуске программа запрашивает IP с маской (например, 10.221.32.1/22), сканирует сеть и сохраняет результаты в Excel-файл с отметкой времени.
Перед развёртыванием код превращался в исполняемый файл с использованием библиотеки PyInstaller:
pyinstaller --onefile scanner.py
**WinRM Scanner**
![image_2025-02-02_20-20-53 (2)](https://github.com/user-attachments/assets/43deb88d-9408-4747-aad3-1ec31e20023a)
![image_2025-02-02_20-20-53](https://github.com/user-attachments/assets/e48d58d4-fcaa-4128-bfa9-7d8f3c8e45a7)

**SMBv1 Scanner**
![image](https://github.com/user-attachments/assets/8689b61a-046a-4b25-960d-07e81fbe0080)
![image](https://github.com/user-attachments/assets/2763d46d-a97c-46c2-a8b2-cf6dd4103077)
