import nmap #nmap
import socket # для dns
from openpyxl import Workbook # для экспорта в excel
from datetime import datetime # для даты и времени
from tqdm import tqdm # для индикатора прогресса

def scan_network(ip_with_mask):
    nm = nmap.PortScanner() # инициализация nmap
    results = []
    
    try:
        print(f"Сканирование WinRM в сети: {ip_with_mask}")
        # Сканирование портов 5985 и 5986
        nm.scan(ip_with_mask, '5985,5986', arguments='-sV -Pn')
        
        for host in tqdm(nm.all_hosts(), desc="Обработка хостов"):
            try:
                # Получаем имя ПК
                try:
                    hostname = socket.gethostbyaddr(host)[0]
                except:
                    hostname = "Не определено"
                
                winrm_status = "OFF"
                
                # Если в nmap product отдал Microsoft HTTPAPI значит WinRM работает
                for port in [5985, 5986]:
                    if (nm[host].has_tcp(port) and 
                        'Microsoft HTTPAPI' in nm[host]['tcp'][port].get('product', '')):
                        winrm_status = "ON"
                        break
                
                results.append({
                    'ip': host,
                    'hostname': hostname,
                    'winrm_status': winrm_status
                })
                
            except Exception as e:
                print(f"Ошибка при обработке хоста {host}: {str(e)}")
                
        return results
    
    except Exception as e:
        print(f"Ошибка сканирования: {str(e)}")
        return results

def export_to_excel(results):
    wb = Workbook()
    ws = wb.active
    ws.title = "Результаты сканирования WinRM"
    
    ws['A1'] = 'IP-адрес'
    ws['B1'] = 'Доменное имя'
    ws['C1'] = 'WinRM статус'
    
    for index, result in enumerate(results, start=2):
        ws[f'A{index}'] = result['ip']
        ws[f'B{index}'] = result['hostname']
        ws[f'C{index}'] = result['winrm_status']
    
    filename = f"winrm_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)
    return filename

def main():
    print("Сканер на WinRM")
    ip_with_mask = input("Введите IP адрес с маской (например, 10.221.32.1/22): ")
    
    print("\nCканирование запущено...")
    results = scan_network(ip_with_mask)
    
    if results:
        filename = export_to_excel(results)
        print(f"\nСканирование завершено. Результаты сохранены в файл: {filename}")
        print(f"Всего просканировано хостов: {len(results)}")
    else:
        print("\nСканирование завершено. Результаты не найдены.")


main()
