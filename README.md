# Tarea2_PortScannerYBannerGrabber
Tarea 2: Combina escaneo de puertos con captura de banners para identificar servicios en red

*Se utiliza la libreria socket para escaner puertos en una IP objetivo y detectar aquellos que estan abiertos
*Con Banner Grabber se captua la informaciòn del servicio que corre en los puertos abiertos
*De està manera se identifican servicios vulnerables

*La IP objetivo se declara en la variable 'ip_objetivo'
*El rango de puertos a escanear se define en las variables 'puerto_inicio' y 'puerto_fin'
*Se definen las variables 'contador_abiertos' y 'contador_cerrados' para contabilizar el total de puertos abiertos y cerrados, respectivamente.

*Mediante ciclo 'for' se itera en los puertos del rango definido para detectar aquellos que estàn abiertos y obtener el banner del servicio.
  *Se intenta crear el socket TCP con AF_INET y SOCK_STREAM para cada puerto
  *Se define un timeout de 1 segundo para evitar bloqueos.
  *connect_ex() retorna 0 si el puerto está abierto
  *Mediante la condiciòn 'if' se incrementa la variable 'contador_abiertos', se imprime el nùmero de puerto 
  *Con recv(1024) se captura el banner y se obtiene hasta 1KB de datos del servicio
  *Se imprime el banner del puerto.
  
  *En caso de puertos cerrados, se define en la sentencia 'else' que incremente la variable 'contador_cerrados'

  *Cierra el socket

*Repite el bucle for hasta que deje de cumplirse la condiciòn

*Finalmente imprime un mensaje con el total de puertos abiertos y cerrados
  





