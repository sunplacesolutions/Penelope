import subprocess
import os
from termcolor import colored

def print_banner():
    banner = '''
    
XX    XX  SSSSS                
 XX  XX  SS        eee    cccc 
  XXXX    SSSSS  ee   e cc     
 XX  XX       SS eeeee  cc     
XX    XX  SSSSS   eeeee  ccccc 
            Security team
    '''
    print(banner)

def run_command(command):
    """Ejecuta un comando de shell y captura la salida."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Error al ejecutar el comando {command}: {e}")
        sys.exit(1)

def save_unique_sorted(filename, data):
    """Guarda los datos en un archivo, ordenados y sin duplicados."""
    unique_sorted_data = sorted(set(data))  # Sort and remove duplicates
    with open(filename, "w") as f:
        f.write("\n".join(unique_sorted_data))

def main(domain):
    print_banner()
    
    # Paso 1: Obtener subdominios con assetfinder
    print(f"[+] Buscando subdominios para: {domain}")
    assetfinder_cmd = f"assetfinder --subs-only {domain}"
    subdomains = run_command(assetfinder_cmd)
    
    # Guardar subdominios únicos y ordenados
    subdomain_file = f"{domain}_subdomains.txt"
    save_unique_sorted(subdomain_file, subdomains)
    print(f"[+] Subdominios guardados en {subdomain_file}")

    # Paso 2: Filtrar subdominios válidos con httprobe
    print(f"[+] Filtrando subdominios válidos con httprobe...")
    httprobe_cmd = f"cat {subdomain_file} | httprobe -t 40000"
    valid_subdomains = run_command(httprobe_cmd)
    
    # Guardar subdominios válidos, únicos y ordenados
    httprobe_file = f"{domain}_httprobe.txt"
    save_unique_sorted(httprobe_file, valid_subdomains)
    print(f"[+] Subdominios válidos guardados en {httprobe_file}")

    # Paso 3: Ejecutar subzy en los subdominios válidos y guardar la salida
    print(f"[+] Ejecutando subzy en los subdominios válidos...")
    subzy_cmd = f"subzy -targets {httprobe_file}"
    vulnerable_sites = run_command(subzy_cmd)
    
    # Guardar sitios vulnerables, únicos y ordenados
    vulnerable_file = f"{domain}_vulnerables.txt"
    save_unique_sorted(vulnerable_file, vulnerable_sites)
    
    if vulnerable_sites:
        print(f"[+] Resultados guardados en {vulnerable_file}")
        print(colored(f"[*] ¡Sitios vulnerables encontrados y guardados en {vulnerable_file}!", "red", attrs=["bold"]))
    else:
        print("[*] No se encontraron sitios vulnerables.")

if __name__ == "__main__":
    domain = input("Ingrese el dominio a analizar: ")
    main(domain)
