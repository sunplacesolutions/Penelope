import subprocess
import sys
import os

def run_command(command):
    """Ejecuta un comando de shell y captura la salida."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Error al ejecutar el comando {command}: {e}")
        sys.exit(1)

def main(domain):
    # Paso 1: Obtener subdominios con assetfinder
    print(f"[+] Buscando subdominios para: {domain}")
    assetfinder_cmd = f"assetfinder --subs-only {domain}"
    subdomains = run_command(assetfinder_cmd)
    
    # Guardar subdominios en archivo
    subdomain_file = f"{domain}_subdomains.txt"
    with open(subdomain_file, "w") as f:
        f.write("\n".join(subdomains))
    
    # Paso 2: Filtrar subdominios válidos con httprobe
    print(f"[+] Filtrando subdominios válidos con httprobe...")
    httprobe_cmd = f"cat {subdomain_file} | httprobe -t 40000"
    valid_subdomains = run_command(httprobe_cmd)
    
    # Guardar subdominios válidos en archivo
    httprobe_file = f"{domain}_httprobe.txt"
    with open(httprobe_file, "w") as f:
        f.write("\n".join(valid_subdomains))
    
    # Paso 3: Ejecutar subzy en los subdominios válidos y guardar la salida en vulnerables.txt
    print(f"[+] Ejecutando subzy en los subdominios válidos...")
    subzy_cmd = f"subzy r --targets {httprobe_file}"
    
    try:
        result = subprocess.run(subzy_cmd, shell=True, capture_output=True, text=True)
        subzy_output = result.stdout
        with open(f"{domain}_vulnerables.txt", "w") as f:
            f.write(subzy_output)
        print(f"[+] Resultados guardados en {domain}_vulnerables.txt")
    except Exception as e:
        print(f"Error al ejecutar subzy: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python buscar_subdominios.py <dominio>")
        sys.exit(1)

    # Capturar el dominio de los argumentos
    domain = sys.argv[1]

    # Ejecutar el script principal
    main(domain)
