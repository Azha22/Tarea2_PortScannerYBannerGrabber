<h1 align="center"> Tarea2: PortScanner y BannerGrabber </h1>

<h2>Combina escaneo de puertos con captura de banners para identificar servicios en red</h2>

<ul>
<li>Se utiliza la libreria <i>'socket'</i> para escanear puertos en una IP objetivo y detectar aquellos que estan abiertos </li>
<li>Con Banner Grabber se captura la información del servicio que corre en los puertos abiertos</li>
<li>De está manera se identifican servicios vulnerables</li>

<li>La IP objetivo se declara en la variable <i>'ip_objetivo'</i></li>
<li>El rango de puertos a escanear se define en las variables <i>'puerto_inicio'</i> y <i>'puerto_fin'</i></li>
<li>Se definen las variables <i>'contador_abiertos'</i> y <i>'contador_cerrados'</i> para contabilizar el total de puertos abiertos y cerrados, respectivamente.</li>

<li>Mediante ciclo <i>'for'</i> se itera en los puertos del rango definido para detectar aquellos que están abiertos y obtener el banner del servicio.</li>
  <ul>
  <li>Se intenta crear el socket TCP con <i>AF_INET</i> y <i>SOCK_STREAM</i> para cada puerto</li>
  <li>Se define un timeout de 1 segundo para evitar bloqueos.</li>
  <li><i>connect_ex()</i> retorna 0 si el puerto está abierto</li>
  <li>Mediante la condiciòn <i>'if'</i> se incrementa la variable <i>'contador_abiertos'</i>, se imprime el nùmero de puerto </li>
  <li>Con <i>recv(1024)</i> se captura el banner y se obtiene hasta 1KB de datos del servicio</li>
  <li>Se imprime el banner del puerto</li>
  <li>En caso de puertos cerrados, se define en la sentencia <i>'else'</i> que incremente la variable <i>'contador_cerrados'</i></li>
  <li>Cierra el socket</li>
  </ul>
<li>Repite el ciclo <i>'for'</i> hasta que deje de cumplirse la condiciòn</li>

<li>Finalmente imprime un mensaje con el total de puertos abiertos y cerrados</li>
</ul>

<h2>Ejemplo de salida #1 </h2>  
<h1 align="center"> <img width="519" height="181" alt="EjemploSalida" src="https://github.com/user-attachments/assets/02117725-c824-4802-8a46-f72a40b2754b" /> </align>

<h2>Ejemplo de salida #2 </h2>
<h1 align="center"> <img width="510" height="140" alt="EjemploSalida2" src="https://github.com/user-attachments/assets/d2005af0-715d-43d1-8212-ff7fc410121a" />
 </align>




