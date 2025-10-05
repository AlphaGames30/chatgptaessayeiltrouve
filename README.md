# 🌐 Discord Global Chat Bot

Un bot Discord simple qui permet de synchroniser plusieurs salons entre différents serveurs et de relayer les messages en temps réel.  
Le bot inclut aussi un mini service web (Flask) qui tourne sur le même service Render.

---

## 🚀 Fonctionnalités
- Commande **/addsync** → ajoute le salon courant dans le chat global.  
- Commande **/removesync** → retire le salon courant du chat global.  
- Tous les salons ajoutés avec `/addsync` recevront automatiquement les messages envoyés dans les autres salons synchronisés.  
- Un mini service web affiche une page de statut sur Render (`/`).

---

## 📦 Installation locale
### 1. Cloner le projet
```bash
git clone https://github.com/ton-compte/discord-global-chat.git
cd discord-global-chat
