<<<<<<< HEAD
# CI/CD – TP4 GitHub Actions
=======
# Chaîne CI/CD – Python + GitHub Actions

Ce dépôt illustre une chaîne **CI/CD** complète pour une application Python (FastAPI) :
- **CI** : lint (ruff), tests `pytest` + **couverture ≥ 80%** (échec si < 80%).
- **CD** : build et **push Docker** vers **GitHub Container Registry (GHCR)** lors d'un **tag**.
- **Déploiement** : job manuel avec approbation via l'**environnement `production`**, lecture d'un **secret** `APP_SECRET` et message de déploiement.

## Badges (à adapter)
Remplacez `<user>` et `<repo>` par votre utilisateur et nom de dépôt GitHub.
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)

![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/<user>/<repo>/actions/workflows/docker.yml/badge.svg)

<<<<<<< HEAD
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
=======
## Lancer en local
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
```

## Tests + couverture
```bash
pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=term-missing --cov-fail-under=80
```

## Docker local
```bash
docker build -t demo-fastapi:dev .
docker run -p 8000:8000 demo-fastapi:dev
```

## Workflows
- **CI** : `.github/workflows/ci.yml` – s'exécute sur `push`/`pull_request` vers `main`.
- **Docker** : `.github/workflows/docker.yml` – s'exécute **sur tag** `v*` (ex: `v1.0.0`), **push** vers GHCR.
- **Deploy** : `.github/workflows/deploy.yml` – **manuel** via `workflow_dispatch`, nécessite une **approbation** sur l'environnement `production`, lit `APP_SECRET`, et affiche un message de déploiement.

## Publication Docker vers GHCR
Le workflow `docker.yml` utilise le `GITHUB_TOKEN` avec la permission `packages: write` pour pousser l'image.

L'image est publiée sous :
```
ghcr.io/<votre_utilisateur>/<nom_du_repo>:<tag>
```

## Déclencher le build Docker
```bash
git tag v1.0.0
git push origin v1.0.0
```

## Déploiement manuel
Dans l'onglet **Actions** > **deploy**, cliquez **Run workflow**, choisissez la version (ex: `v1.0.0`), puis un **relecteur** approuve l'environnement `production`.
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)

Trigger CI Mer  8 oct 2025 09:54:24 CEST
