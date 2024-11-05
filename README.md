# Penelope - Buscar Subdominios con XSec Security Team
Este script permite buscar subdominios, filtrarlos, y detectar posibles sitios vulnerables de un dominio específico. Utiliza herramientas como assetfinder, httprobe y subzy para realizar un análisis completo y muestra un banner personalizado de "XSec" al inicio de su ejecución.

# Características
Búsqueda de Subdominios: Encuentra subdominios de un dominio ingresado utilizando assetfinder.
Filtrado de Subdominios Válidos: Usa httprobe para verificar la disponibilidad de los subdominios.
Detección de Sitios Vulnerables: Emplea subzy para identificar subdominios potencialmente vulnerables.
Resultados Únicos y Ordenados: Cada archivo de salida es procesado para eliminar duplicados y ordenar los resultados alfabéticamente.
Alerta de Sitios Vulnerables: Muestra en pantalla un mensaje si se encuentran sitios vulnerables.

# Requisitos Previos
Asegúrate de tener instaladas las siguientes herramientas:

assetfinder
httprobe
subzy
termcolor: Para el mensaje de sitios Vulnerables (instalación: pip install termcolor).

# Uso
# Clona este repositorio:

git clone https://github.com/sunplacesolutions/Penelope.git

cd Penelope

# Ejecuta el script e ingresa el dominio que deseas analizar:

python3 buscar_subdominios.py

# Ingresa el dominio cuando el script lo solicite. El script generará tres archivos de resultados:

<domain>_subdomains.txt: Lista de subdominios encontrados.

<domain>_httprobe.txt: Lista de subdominios válidos.

<domain>_vulnerables.txt: Lista de sitios potencialmente vulnerables.

Si se encuentran sitios vulnerables, se mostrará un mensaje en pantalla resaltado en rojo y en negrita.

# Ejemplo de Ejecución

Ingrese el dominio a analizar: ejemplo.com
[+] Buscando subdominios para: ejemplo.com
[+] Subdominios guardados en ejemplo_com_subdomains.txt
[+] Filtrando subdominios válidos con httprobe...
[+] Subdominios válidos guardados en ejemplo_com_httprobe.txt
[+] Ejecutando subzy en los subdominios válidos...
[*] ¡Sitios vulnerables encontrados y guardados en ejemplo_com_vulnerables.txt!

# Notas
Archivos de Salida: Cada archivo de salida se genera aplicando sort y uniq, eliminando duplicados y ordenando los subdominios alfabéticamente.
Compatibilidad: Este script está diseñado para sistemas compatibles con las herramientas assetfinder, httprobe y subzy.
# Contribuciones
¡Las contribuciones son bienvenidas! Si tienes mejoras o encuentras algún problema, abre un issue o envía un pull request.
