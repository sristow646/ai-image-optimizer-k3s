

🖼️ AI Image Optimizer K3s

Self-hosted AI System for Image Enhancement & Text-to-Image Generation – powered by Gradio, Stable Diffusion, and K3s

🚀 Projektziel

Ein vollständig automatisiertes, containerisiertes KI-System zur Bildverarbeitung:

🔧 Bildoptimierung (z. B. Upscaling, Reparatur)

🎨 Text-to-Image Generierung (via Stable Diffusion)

🧩 Deploybar per Helm auf einem K3s Cluster

🛡️ Ingress HTTPS-Support + PVC via Longhorn

Ideal als Referenzprojekt für DevOps, MLOps und Homelab-Enthusiasten.
---
⚙️ Architektur
```
Proxmox VM (Ubuntu)
└── K3s (via Helm)
    ├── ai-image-optimizer (Gradio App)
    │   ├── Mode 1: Bild hochladen & verbessern
    │   └── Mode 2: Text eingeben → Bild generieren (Stable Diffusion)
    ├── Ingress (nginx + TLS via Wildcard-Zertifikat)
    ├── Persistent Storage (Longhorn PVC)
    └── GitHub Actions Runner (CI/CD)
```
---
📦 Features

✅ Gradio WebUI mit Tabs für 2 KI-Funktionen

✅ Text-to-Image via HuggingFace diffusers

✅ Helm-Chart mit pullPolicy: Always

✅ K3s-optimierte Ressourcen (CPU/GPU, float16)

✅ CI/CD mit GitHub Actions + Self-Hosted Runner

✅ Image Tagging mit Short-SHA

✅ Automatische Docker-Cleanup Hooks

🧪 Funktionen

1. 🧼 Bildoptimierung

Bild-Upload

Speicherung auf PVC

Ausgabe: optimiertes PNG

2. 🪄 Text zu Bild

Texteingabe (z. B. "Katze im Cyberpunk-Stil")

Stable Diffusion v1.5 Generierung

Ausgabe: KI-generiertes PNG

🚀 Deployment (K3s + Helm)

helm upgrade --install ai-image-optimizer ./charts/ai-image-optimizer \
  --set image.repository=<dein-repo>/ai-image-optimizer-k3s \
  --set image.tag=<kurzer-git-sha> \
  --namespace default \
  --atomic --wait

Zugriff via Ingress:

https://ai.infranerd.de

🤖 CI/CD: GitHub Actions

Bei jedem Push auf main:

Image Build & Push (:short-sha)

Helm Upgrade (mit PullPolicy Always)

Cleanup: docker image prune -f

Secrets:

DOCKER_USERNAME

DOCKER_PASSWORD

📂 Verzeichnisstruktur

ai-image-optimizer-k3s/
├── app/                    # Gradio App
│   ├── app.py             # Dual Mode: Optimizer + Generator
│   └── requirements.txt
├── charts/ai-image-optimizer/
│   ├── templates/
│   └── values.yaml
├── .github/workflows/
│   └── deploy.yml
└── README.md

✨ Technologie-Stack

Python 3.10

Gradio 3.41

Diffusers / Stable Diffusion

Helm + K3s + Ingress

GitHub Actions + Self-Hosted Runner

👨‍💻 Autor

Stephan RistowDevOps Engineer · Selfhoster · AI-Enthusiast

💡 Projekt entstand als persönliche Lern- & Showcase-Plattform für CI/CD, AI-Infrastruktur & Kubernetes Automation.

