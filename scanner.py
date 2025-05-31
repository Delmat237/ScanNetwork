import socket
import threading
import argparse
import logging
from datetime import datetime

# Configuration du log
logging.basicConfig(filename="scan_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Liste de ports suspects à surveiller (peut être modifiée dans le fichier externe)
def load_suspicious_ports(file_path="suspicious_ports.txt"):
    try:
        with open(file_path, "r") as f:
            return [int(line.strip()) for line in f if line.strip().isdigit()]
    except FileNotFoundError:
        return [6667, 31337, 4444]  # ports typiques d'activités douteuses

suspicious_ports = load_suspicious_ports()

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"[+] Port ouvert : {port}")
        logging.info(f"Port ouvert : {port}")

        if port in suspicious_ports:
            print(f"[!] Port suspect détecté : {port}")
            logging.warning(f"Port suspect détecté : {port}")

        s.close()
    except:
        pass

def scan_host(host, start_port, end_port):
    print(f"\n[~] Début du scan de {host} de {start_port} à {end_port} ...\n")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scanner réseau sécurisé (mini-projet)")
    parser.add_argument("host", help="Adresse IP ou nom d'hôte à scanner")
    parser.add_argument("-s", "--start", type=int, default=1, help="Port de début (défaut: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Port de fin (défaut: 1024)")

    args = parser.parse_args()
    target_ip = socket.gethostbyname(args.host)

    print(f"Scan lancé sur {args.host} ({target_ip}) à {datetime.now()}")
    scan_host(target_ip, args.start, args.end)
