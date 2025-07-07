

# 🌐 CloudCompose

> **Dynamic Multi-Cloud Infrastructure Composer**  
> *Design once → deploy anywhere*

---

## 🚀 What is CloudCompose?

CloudCompose is an **open-source, self-service platform** that lets you design infrastructure at a high level  
(e.g., "Container Orchestrator + Managed DB + Monitoring")  
and automatically:

- Maps to equivalent services across **AWS, Azure, GCP**
- Generates **Terraform + Ansible** code
- Pushes to Git
- Deploys via **GitOps & ArgoCD**
- Tracks cost & drift

---

## 🧩 Why this matters

✅ Multi-cloud abstraction without complexity  
✅ Faster, secure, standardized deployments  
✅ Cost-aware & policy-driven  
✅ Clear audit trail & self-service for dev teams

---

## 🏗️ High-Level Architecture (v0)

UI → Codegen API → Service Catalog & Mapping
→ Generates Terraform + Ansible → Git Repo
→ CI/CD Pipeline → ArgoCD → Live Infra


*(Detailed diagrams coming soon in `/docs`)*

---

## ⚙️ Tech Stack

| Purpose              | Tech                          |
|---------------------|-------------------------------|
| UI                  | React / Next.js / Tailwind    |
| API / Codegen       | Python (FastAPI)              |
| IaC                 | Terraform, Ansible            |
| GitOps Deploy       | ArgoCD                         |
| CI/CD               | GitHub Actions / GitLab CI    |
| Cost & Monitoring   | Infracost, Prometheus, Grafana|

---

## 🛣 Roadmap

| Phase | Goal |
|--|--|
| 1 | Initialize mono-repo & docs |
| 2 | Build service catalog & mapping.json |
| 3 | Codegen API microservice |
| 4 | Frontend self-service UI |
| 5 | CI/CD pipelines & ArgoCD deploy |
| 6 | Cost tracking & dashboards |
| 7 | Dynamic multi-cloud service composer |
| 8 | Docs & showcase demo |

*(Detailed roadmap in `/docs` coming soon)*

---

## 📦 Repository Structure (v0)

cloudcompose/
├── frontend/ # React / Next.js UI
├── codegen-api/ # FastAPI microservice
├── service-catalog/ # Terraform modules & mapping.json
├── pipelines/ # CI/CD YAML templates
├── deploy/ # ArgoCD manifests
├── docs/ # Architecture diagrams & design docs
└── README.md


---

## 🧪 Status

🟢 Planning & architecture phase  
Next: draft `mapping.json` & start service catalog modules

---

## 📝 License

[MIT](LICENSE)

---

## ✨ Author

Built by Kiran — DevOps engineer passionate about automation, multi-cloud & innovation 🚀
