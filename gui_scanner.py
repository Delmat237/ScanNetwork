import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import socket
import logging
from datetime import datetime

logging.basicConfig(filename="scan_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def load_suspicious_ports(file_path="suspicious_ports.txt"):
    try:
        with open(file_path, "r") as f:
            return [int(line.strip()) for line in f if line.strip().isdigit()]
    except FileNotFoundError:
        return [4444, 6667, 31337, 23]

suspicious_ports = load_suspicious_ports()

def scan_port(host, port, output_area):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        msg = f"[+] Port ouvert : {port}\n"
        output_area.insert(tk.END, msg)
        logging.info(f"Port ouvert : {port}")
        if port in suspicious_ports:
            alert = f"[!] Port suspect détecté : {port}\n"
            output_area.insert(tk.END, alert)
            logging.warning(f"Port suspect détecté : {port}")
        s.close()
    except:
        pass

def scan_host_gui(host, start_port, end_port, output_area):
    try:
        target_ip = socket.gethostbyname(host)
        output_area.insert(tk.END, f"Scan lancé sur {host} ({target_ip}) à {datetime.now()}\n")
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(target_ip, port, output_area))
            thread.start()
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de scanner : {e}")

def start_scan():
    host = entry_host.get()
    try:
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())
    except ValueError:
        messagebox.showerror("Erreur", "Les ports doivent être des entiers.")
        return
    output_area.delete(1.0, tk.END)
    threading.Thread(target=scan_host_gui, args=(host, start_port, end_port, output_area)).start()

# Interface
app = tk.Tk()
app.title("Scanner Réseau Sécurisé")

tk.Label(app, text="Hôte:").grid(row=0, column=0, sticky="e")
entry_host = tk.Entry(app, width=30)
entry_host.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app, text="Port début:").grid(row=1, column=0, sticky="e")
entry_start = tk.Entry(app, width=10)
entry_start.insert(0, "20")
entry_start.grid(row=1, column=1, sticky="w", padx=5)

tk.Label(app, text="Port fin:").grid(row=2, column=0, sticky="e")
entry_end = tk.Entry(app, width=10)
entry_end.insert(0, "1024")
entry_end.grid(row=2, column=1, sticky="w", padx=5)

btn_scan = tk.Button(app, text="Démarrer le scan", command=start_scan)
btn_scan.grid(row=3, column=0, columnspan=2, pady=10)

output_area = scrolledtext.ScrolledText(app, width=60, height=20)
output_area.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
