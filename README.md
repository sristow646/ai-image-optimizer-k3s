
# ai-image-optimizer-k3s 🚀

Self-hosted AI-powered Image Optimizer with Real-ESRGAN + GFPGAN running on Kubernetes (K3s) with Helm Charts.

## Features:
- Gradio WebUI for easy drag & drop image uploads
- AI-Powered Image Enhancement (Super Resolution + Face Restoration)
- Optimized for CPU-only deployments (Intel/AMD) but GPU-ready
- Helm Chart for quick Kubernetes deployment
- Ready for GitHub Actions CI/CD pipeline

## 🚀 Quickstart:

1. Build & push Docker image automatically via CI/CD
2. Deploy Helm Chart via GitHub Actions to your K3s cluster

## 🛠️ Usage:
Once deployed, access the WebUI at:

```
https://ai.infranerd.de
```

Upload your images and download the enhanced result!

## 📦 Helm Install (manual)
```bash
helm install ai-image-optimizer ./charts/ai-image-optimizer
```

## CI/CD Pipeline:
- Docker Build & Push to DockerHub
- Helm Upgrade on K3s Cluster via GitHub Actions

## 🔐 Secrets needed:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `KUBECONFIG`

---

Made with ❤️ for Homelabs
