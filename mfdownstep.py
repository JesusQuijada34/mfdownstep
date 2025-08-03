import argparse, os, sys, time, requests, shutil, subprocess

# 🎨 Colores ANSI
class Ansi:
    CYAN = '\033[96m'; GREEN = '\033[92m'; RED = '\033[91m'
    YELLOW = '\033[93m'; GRAY = '\033[90m'; RESET = '\033[0m'

# 📊 Barra de progreso basada en tamaño
def mostrar_progreso(descargado, total):
    if total == 0: return
    porcentaje = int((descargado / total) * 100)
    barra = '█' * (porcentaje // 5) + '-' * (20 - porcentaje // 5)
    sys.stdout.write(f"\r{Ansi.YELLOW}[{barra}] {porcentaje}%{Ansi.RESET}")
    sys.stdout.flush()

# 🌐 Handshake visual
def mostrar_handshake(headers, status):
    print(f"{Ansi.CYAN}🌐 Handshake HTTP:{Ansi.RESET}")
    print(f"  ➜ Status: {Ansi.GREEN}{status}{Ansi.RESET}")
    print(f"  ➜ Server: {Ansi.GRAY}{headers.get('Server', 'Desconocido')}{Ansi.RESET}")
    print(f"  ➜ Tipo: {headers.get('Content-Type', 'Desconocido')}")
    print(f"  ➜ Tamaño: {headers.get('Content-Length', '¿?')} bytes\n")

# 📥 Descarga con `requests` + barra
def descargar_con_requests(url, destino):
    try:
        r = requests.get(url, stream=True, timeout=15)
        mostrar_handshake(r.headers, r.status_code)

        nombre = url.split('/')[-1].split('?')[0] or "descarga.bin"
        path = os.path.join(destino, nombre)
        total = int(r.headers.get('Content-Length', 0))
        descargado = 0

        with open(path, 'wb') as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                    descargado += len(chunk)
                    mostrar_progreso(descargado, total)

        print(f"\n{Ansi.GREEN}✅ Descarga completa:{Ansi.RESET} {path}")
        return True
    except Exception as e:
        print(f"{Ansi.RED}⚠️ Error: {e}{Ansi.RESET}")
        return False

# 🔁 Fallback con wget/curl
def fallback_descarga(url, destino):
    nombre = url.split('/')[-1].split('?')[0] or "descarga.bin"
    path = os.path.join(destino, nombre)

    if shutil.which("wget"):
        print(f"{Ansi.YELLOW}➤ Reintentando con wget...{Ansi.RESET}")
        subprocess.run(["wget", url, "-O", path])
    elif shutil.which("curl"):
        print(f"{Ansi.YELLOW}➤ Reintentando con curl...{Ansi.RESET}")
        subprocess.run(["curl", "-L", url, "-o", path])
    else:
        print(f"{Ansi.RED}❌ No hay wget ni curl disponibles.{Ansi.RESET}")
        return

    if os.path.exists(path):
        print(f"{Ansi.GREEN}✅ Fallback exitoso:{Ansi.RESET} {path}")
    else:
        print(f"{Ansi.RED}⚠️ Fallback fallido.{Ansi.RESET}")

# 🎯 Entrada principal
def main():
    parser = argparse.ArgumentParser(description="Descargador Universa")
    parser.add_argument('--url', type=str, required=True, help='Enlace a descargar')
    args = parser.parse_args()

    destino = os.path.join(os.path.expanduser("~"), "Descargas", "UniversalDownloads")
    os.makedirs(destino, exist_ok=True)

    if not descargar_con_requests(args.url, destino):
        fallback_descarga(args.url, destino)

if __name__ == "__main__":
    main()

