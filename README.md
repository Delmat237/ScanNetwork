# 🔍 Secure Network Scanner

Mini-projet de cybersécurité : outil Python pour scanner les ports ouverts sur une machine et identifier des ports suspects.

## 🎯 Fonctionnalités

- Scan TCP de ports
- Multi-threading rapide
- Log des résultats dans `scan_log.txt`
- Détection de ports "suspects" via une liste personnalisable

## 🚀 Utilisation

```bash
python scanner.py 192.168.1.10 -s 20 -e 100

ou 

python gui_scanner.py 
```

## ⚠️ Exemples de ports suspects

- `6667` : IRC (souvent détourné)
- `4444` : backdoors/metasploit
- `31337` : Elite port
- `23` : Telnet

Modifiable dans le fichier `suspicious_ports.txt`.

## 📁 Structure

- `scanner.py` : script principal
- `suspicious_ports.txt` : liste des ports suspects
- `scan_log.txt` : log généré automatiquement

## 📦 Dépendances

Tkinter


## 👤 Auteur

🤵 Nom : Leonel Azangue

📨 Email : azangueleonel9@gmail.com

GitHub : @Delmat237

LinkedIn : leonel-azangue

WhatsApp : +237 657 450 314

## 📄 Licence

Ce projet est sous licence MIT — voir le fichier LICENSE pour plus de détails.

## 🤝 Contribuer

Les contributions sont les bienvenues !
N'hésitez pas à forker le dépôt, créer une branche, proposer une fonctionnalité ou corriger un bug via une Pull Request.