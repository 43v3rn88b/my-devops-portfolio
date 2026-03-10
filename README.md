# my-devops-portfolio

[![Build Status](https://img.shields.io/badge/Build-GitHub_Actions-blue?logo=github-actions)](https://github.com/43v3rn88b/my-devops-portfolio/actions)
[![Security Scan](https://img.shields.io/badge/Security-Trivy-orange?logo=trivy)](https://aquasecurity.github.io/trivy/)
[![Performance](https://img.shields.io/badge/Load_Test-k6-7161ef?logo=k6)](https://k6.io/)

This project is a complete demonstration of a modern **DevSecOps lifecycle**, featuring automated quality gates, container orchestration, and application-level observability.

## 🛠 The Tech Stack
* **App:** Python (Flask), Prometheus-Flask-Exporter
* **CI/CD:** GitHub Actions
* **Containerization:** Docker (Alpine-hardened)
* **Orchestration:** Kubernetes (Minikube)
* **Security:** Trivy (Vulnerability Scanning)
* **Performance:** k6 (Load Testing)
* **Observability:** Prometheus & Grafana (Helm)

## 🏗 Pipeline Architecture: The "Fail-Fast" Logic
The GitHub Actions pipeline is designed to protect production. It will **immediately terminate** if any of the following gates are not met:
1. **Security Gate:** **Trivy** scans the Docker image. The pipeline fails if any `CRITICAL` or `HIGH` vulnerabilities are found.
2. **Performance Gate:** **k6** stress-tests the ephemeral container. If the application latency exceeds p(95)=500ms or error rates exceed 1%, deployment is blocked.

## 📈 Kubernetes & Observability
* **High Availability & Self-Healing:** Configured Kubernetes `Deployment` with 2 replicas, backed by custom Liveness and Readiness probes to ensure zero-downtime rollouts and automated restarts for zombie processes.
* **APM (Application Performance Monitoring):** Instrumented the Flask API to expose a `/metrics` endpoint. Deployed the `kube-prometheus-stack` via Helm to scrape metrics, visualizing HTTP request rates, latency histograms, and pod compute resources in Grafana.

