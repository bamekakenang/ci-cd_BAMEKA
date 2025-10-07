# CI/CD – TP4 GitHub Actions

![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/<user>/<repo>/actions/workflows/docker.yml/badge.svg)

## Instructions
1. Crée un dépôt GitHub nommé `ci-cd_<ton_nom>`
2. Clone le dépôt : `git clone https://github.com/<user>/ci-cd_<ton_nom>.git`
3. Copie tous les fichiers de ce dossier dans le dépôt
4. Commit et push :  
   ```bash
   git add .
   git commit -m "Init TP4 CI/CD"
   git push origin main
   ```
5. Vérifie l'onglet **Actions** → le workflow CI doit passer ✅
6. Crée un tag pour déclencher le build Docker :  
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
7. Va dans GHCR (GitHub Packages) pour voir ton image.
8. Crée un environnement `production` + secret `APP_SECRET`, puis exécute manuellement le workflow **Deploy**.
