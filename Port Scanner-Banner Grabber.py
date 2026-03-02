#- Tarea 2: PortScanner y BannerGrabber
#- Combina escaneo de puertos con captura de banners para identificar servicios en red
#- Alumna: Dulce Brenda Primero Cruz 

#- Libreria
import socket 

#- IP objetivo
ip_objetivo = '192.168.56.1' #- IP maquina fisica 	
#ip_objetivo =  '192.168.100.45' #- IP Maquina virtual
#ip_objetivo = 'localhost'

#- Rango de puertos a escanear
puerto_inicio = 1
puerto_fin = 100
contador_abiertos = 0
contador_cerrados = 0

print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)

for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conexion.settimeout(1) #- Tiempo de espera
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            print(f'Puerto {puerto}: ABIERTO')
            contador_abiertos = contador_abiertos + 1
            # Intentamos obtener el banner
            try:
                socket_conexion.settimeout(1) # Esperamos máximo 1 segundo
                banner = socket_conexion.recv(1024)
                banner_texto = banner.decode('utf-8', errors='ignore')
            
                print(f' Banner: {banner_texto.strip()}')
            
            except:
                print(f' Banner: No disponible')
        
        else:
            #print(f'Puerto {puerto}: CERRADO')
            contador_cerrados = contador_cerrados + 1
        socket_conexion.close()
    
    except:
        pass

print('-' * 50)
print(f' Puertos abiertos: {contador_abiertos} - Puertos cerrados: {contador_cerrados}')
print('Escaneo completado')
