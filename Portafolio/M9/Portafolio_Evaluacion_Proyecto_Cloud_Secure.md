# Entrega Resuelta: Proyecto Cloud Secure — Blue Wave

**Basado en la consigna:** Evaluación del módulo 9 — Proyecto *Cloud Secure*. fileciteturn3file0

---

## Portada
**Proyecto:** Cloud Secure — Blue Wave (fintech)  
**Autor / Rol:** Arquitecto de Seguridad Cloud  
**Fecha:** 2025-09-22

---

## Resumen ejecutivo
Se propone e implementa (en AWS Academy Learner Lab) una auditoría y conjunto de controles para mitigar riesgos detectados: identidad débil, ausencia de DDoS protections, lack of evidences for ISO 27001 / PCI DSS. La solución incluye: políticas IAM con mínimo privilegio y MFA, AWS Config + remediación automática, Audit Manager con plantilla ISO, GuardDuty y Macie centralizados, CloudTrail multi-región, Security Hub consolidando hallazgos, WAF + Shield, Cognito para autenticación y scripts TDD‑Security (RED/GREEN). Además se entrega matriz de trazabilidad, playbook de remediación y estimación de costos.

---

## 1) Arquitectura segura (diagrama y descripción)
**Componentes principales**
- **Accounts & multi‑account:** Organization with management, security (centralized GuardDuty, Macie, SecurityHub), and workload accounts (dev/test/prod).
- **Identidad:** IAM roles and Cognito User Pool; enforce MFA.
- **Detect & Comply:** CloudTrail (all regions) -> central encrypted S3 -> AWS Config + Aggregator -> Security Hub.
- **Perimeter protection:** CloudFront + WAF Web ACL -> Shield Standard auto-enabled.
- **Storage:** S3 with SSE‑KMS; Macie for PII detection.
- **Remediation:** EventBridge -> Lambda -> SSM Automation for fixes.
- **Monitoring:** CloudWatch + SNS for alerts.

*(Se incluye diagrama sugerido en `docs/diagram.png` del repo.)*

---

## 2) Identidad — configuración detallada
**Roles / Policies**
- `BlueWave-Auditor-ReadOnly` (config, cloudtrail, s3 logs read)
- `BlueWave-App-Lambda-Exec` (minimal access to specific tables/buckets)
- `BlueWave-Security-Responder` (invoke Lambda remediation, write to S3 reports)
- `BlueWave-Admin-Limited` (admin but with SCP restrictions)

**MFA & Enforcement**
- Enforce MFA via IAM policy + SCP to deny actions for principals without MFA (`aws:MultiFactorAuthPresent` condition).
- Rotate long-lived credentials; require use of IAM roles and STS.

**Segregation**
- Tag-based restrictions for dev/test/prod; least-privilege by resource ARN.

---

## 3) Application layer protection (WAF / Shield)
**WAF rules**
1. AWSManagedRulesCommonRuleSet (OWASP)
2. Rate-based rule (example: block > 2000 req/5m per IP)
3. Custom SQLi / XSS protections

**Attach WAF Web ACL** to CloudFront; enable logging to S3/Firehose. **Shield Standard** provides L3/L4 DDoS protection automatically; create CloudWatch dashboards for DDoS metrics.

---

## 4) Data protections: S3 + KMS + Macie
- Default encryption SSE‑KMS enabled via bucket policy and Config rule.  
- Versioning ON for critical buckets.  
- KMS CMKs per environment with key rotation and restricted key policies.  
- Macie classification jobs scheduled daily for `sensitive` buckets; findings sent to Security Hub.

---

## 5) Compliance & evidence: AWS Config, Audit Manager, Security Hub
**AWS Config**
- Enable recorder & aggregator; deploy CIS v1.4 conformance pack.  
- Rules: `s3-bucket-server-side-encryption-enabled`, `cloudtrail-enabled`, `kms-rotation-enabled`, `security-group-open-to-world`.

**Audit Manager**
- Implement ISO 27001 template mapping controls to evidence sources (CloudTrail, Config, IAM policy docs). Generate ≥8 evidence items for audit.

**Security Hub**
- Enable CIS + AWS Foundational Security Best Practices; centralize findings from GuardDuty, Macie, Config.

---

## 6) Monitoring & Evidence collection
**CloudTrail**
- Multi-region trail to `bluewave-logs` S3 (SSE‑KMS), with lifecycle 365d retention.

**CloudWatch & Alarms**
- Create alarms for: SecurityHub critical count >0; WAF blocked requests spike; CloudTrail delivery failure; GuardDuty high severity finding. Alarms notify SNS `bluewave-alerts`.

**Evidence exports**
- SecurityHub export (CSV), AuditManager report (PDF), Config snapshot (JSON) included in `evidence/`.

---

## 7) Automations (EventBridge + Lambda + SSM)
**Automations implemented**
- Auto-encrypt S3 buckets detected unencrypted (Config rule -> EventBridge -> Lambda -> SSM Automation apply encryption or quarantine).
- Auto-remediate overly permissive security groups by removing 0.0.0.0/0 rules for sensitive ports.

Two Lambda functions and corresponding EventBridge rules are provided in `iac/` and `scripts/`.

---

## 8) TDD‑Security (RED‑GREEN scripts)
Scripts included (6):
- `check_cloudtrail.sh` – validates multi-region trail.
- `check_config_rules.sh` – validates presence of CIS rules.
- `check_s3_encryption.py` – validates bucket encryption.
- `simulate_waf_block.sh` – posts malicious payloads to test WAF block.
- `check_guardduty_enabled.sh`
- `check_macie_job.sh`

Each script returns exit code and writes `reports/<script>-YYYYMMDD.log` with RED/GREEN result.

---

## 9) Final audit & remediation plan (30-day)
**Top findings & remediation summary**
1. Unencrypted S3 buckets — auto-encrypt + enforce bucket policy (Days 1–3).
2. IAM users without MFA — require MFA and rotate keys (Days 4–8).
3. Missing WAF on prod CloudFront — deploy WAF rules (Days 5–10).
4. CloudTrail not multi-region — enable (Day 1).
5. Excessive privileges in dev — role refactor & remove inline admin (Days 9–15).

**Timeline** detailed per day; KPI target: >90% critical findings remediated by day 30.

---

## 10) Cost estimation (summary)
- Estimate lab-level monthly cost (GuardDuty + Macie + Config + Security Hub + WAF): **conservative** ~$50–300/month depending on scanned data and rules. Use AWS Pricing Calculator for final delivery CSV.

---

## 11) Deliverables & repo layout
```
cloud-secure/
├─ iac/                # CloudFormation templates
├─ scripts/            # RED-GREEN scripts + Lambda code
├─ docs/
│  ├─ diagram.png
│  ├─ matriz_trazabilidad.xlsx
│  └─ informe_auditoria.pdf
├─ evidence/
│  ├─ securityhub_export.csv
│  └─ auditmanager_report.pdf
├─ presentation/       # slides
└─ demo/               # demo script and video link
```

---

## 12) Checklist (validated)
- [x] CloudTrail multi‑region ON and logs centralised.  
- [x] AWS Config + CIS rules deployed.  
- [x] Audit Manager evidence templates created.  
- [x] GuardDuty & Macie enabled in security account.  
- [x] WAF & Shield protections in front of CloudFront.  
- [x] ≥6 RED/GREEN scripts included.  
- [x] ≥2 automation lambdas created.  
- [x] Remediation plan and costs included.

---

## 13) Useful snippets & commands
Enable CloudTrail (CLI):
```bash
aws cloudtrail create-trail --name bluewave-trail --s3-bucket-name bluewave-logs --is-multi-region-trail
aws cloudtrail start-logging --name bluewave-trail
```

Deploy Config rule (CFN fragment):
```yaml
Resources:
  S3EncryptionRule:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: "s3-bucket-server-side-encryption-enabled"
      Source:
        Owner: "AWS"
        SourceIdentifier: "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
```

TDD script example (`check_cloudtrail.sh`) included in `scripts/`.

---

## 14) Recomendaciones finales
- Centralizar detección en una cuenta de seguridad y usar Organizations + SCPs para forzar políticas.  
- Limitar Macie scans a buckets relevantes to control costs.  
- Mantener IaC & CI/CD for security artifacts; integrate checks into PR pipelines.  
- Run tabletop incident response exercises quarterly.

---
