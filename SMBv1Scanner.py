import nmap #nmap
import socket # для dns
from openpyxl import Workbook # для экспорта в excel
from datetime import datetime # для даты и времени
from tqdm import tqdm # для индикатора прогресса

def scan_network(ip_with_mask):
    nm = nmap.PortScanner() 
    results = []
    
    try:
        print(f"Сканирование SMB протоколов в сети: {ip_with_mask}")
        nm.scan(ip_with_mask, arguments='--script smb-protocols -p 445')
        
        for host in tqdm(nm.all_hosts(), desc="Обработка хостов"):
            try:
                try:
                    hostname = socket.gethostbyaddr(host)[0]
                except:
                    hostname = "Не определено"
                
                smb_v1_status = "ВЫКЛ"
                
                if 'hostscript' in nm[host]:
                    for script in nm[host]['hostscript']:
                        if script['id'] == 'smb-protocols':
                            if "NT LM 0.12 (SMBv1)" in script['output']:
                                smb_v1_status = "ВКЛ"
                
                results.append({
                    'ip': host,
                    'hostname': hostname,
                    'smb_v1_status': smb_v1_status
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
    ws.title = "Результаты сканирования SMB v1"
    
    ws['A1'] = 'IP-адрес'
    ws['B1'] = 'Доменное имя'
    ws['C1'] = 'Статус SMB v1'
    
    for index, result in enumerate(results, start=2):
        ws[f'A{index}'] = result['ip']
        ws[f'B{index}'] = result['hostname']
        ws[f'C{index}'] = result['smb_v1_status']
    
    filename = f"smb_v1_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)
    return filename

def main():
    print("Сканер SMB v1")
    ip_with_mask = input("Введите IP адрес с маской (например, 10.221.32.1/22): ")
    
    print("\nСканирование запущено...")
    results = scan_network(ip_with_mask)
    
    if results:
        filename = export_to_excel(results)
        print(f"\nСканирование завершено. Результаты сохранены в файл: {filename}")
        print(f"Всего просканировано хостов: {len(results)}")
    else:
        print("\nСканирование завершено. Результаты не найдены.")


main()
