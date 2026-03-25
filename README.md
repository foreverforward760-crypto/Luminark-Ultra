# LUMINARK® — Intelligent Infrastructure & Consciousness Intelligence Platform

**Meridian Axiom Alignment Technologies**
*Richard L. Stanfield — Founder & Chief Architect*

---

## Overview

LUMINARK is a dual-engine AI intelligence platform that translates raw sensor telemetry and behavioral data into **actionable stage-based insights** using a proprietary framework called **Stanfield's Axiom of Perpetuity (SAP)** — a 10-stage model of system development, maturity, and decay applied across physical infrastructure, organizations, and human behavior.

The platform consists of two production-ready Python engines that share a common core and communicate through a unified REST API.

---

## Architecture

### Telemetry to Actionable Insight

![Telemetry to Actionable Insight](docs/images/telemetry-flow.svg)

Raw sensor data flows through a Domain Adapter into the NSDT/SPAT Stage Classifier, which produces a 5D Stage Vector and TrapScore. The Master API routes this to the Temporal Engine, feeding both the ULTRA and OMEGA insight layers before surfacing results in the OEM Dashboard and 7-Layer Defense system.

### Unified Dual-Engine Architecture

![Unified Dual-Engine Architecture](docs/images/dual-engine-architecture.svg)

OEM hardware connects through a Domain Adapter to a **Shared Core Engine** containing the NSDT/SPAT classifier and SAP framework. The core feeds two specialized engines:
- **ULTRA** — physical infrastructure (grid, water, nuclear, fleet, defense)
- **OMEGA** — human/organizational consciousness (corporate behavior, portfolio analysis, AI safety)

Both engines expose their capabilities through a unified Master API.

---

## Engines

### LUMINARK OVERWATCH PRIME ULTRA (`LUMINARK_OVERWATCH_PRIME_ULTRA.py`)
**2,515 lines | Infrastructure Intelligence Engine**

Analyzes physical systems — power grids, water infrastructure, nuclear facilities, transportation fleets, and cyber-physical environments — using the SAP framework to detect failure trajectories before they become crises.

Key modules:
- **NSDT** (Normalized Stage Distance Tool) — 5D vector classifier (complexity, stability, tension, adaptability, coherence)
- **TrapScore** — Failure risk metric: `Stage × Rigidity × (1 − Adaptability)`
- **InfraContainerRuleEngine** — Digital root-based stage mapping
- **RISSCalculator** — Cyber Kill Chain threat assessment (7-stage)
- **BioSensoryFusion** — Mycelium + Octopus + Thermal sensor fusion
- **InfraPhysicsVelocityEngine** — Stage momentum and velocity calculation
- **7-Layer Defense System** — Progressive threat response architecture
- **Temporal Engine** — Multi-period stage trajectory and drift detection
- **Hurricane/Uri Validation** — Retroactive accuracy scoring on real events

### LUMINARK CONSCIOUSNESS ENGINE OMEGA (`LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA.py`)
**2,263 lines | Consciousness & Organizational Intelligence Engine**

Assesses the developmental stage and health of human systems — individuals, corporations, financial portfolios, and AI agents — using the same SAP framework adapted for behavioral, financial, and cognitive signals.

Key modules:
- **SPAT Engine** — Individual psychological stage assessment (7 behavioral dimensions)
- **Corporate Analyzer** — Revenue, margin, growth, and organizational health staging
- **NSAT** (Noctilucan Stage Assessment Tool) — Advanced composite stage scoring
- **Stage 8 Trap Detector** — Early warning for terminal rigidity
- **NEI** (Noctilucan Economic Index) — Macroeconomic stage classifier
- **CITI** (Cross-Indicator Tumbling Index) — Cross-domain momentum decay detection
- **ThresholdOutcomePredictor** — Probabilistic stage transition forecasting
- **Enhanced Sentinel Clarity** — AI content safety and manipulation detection
- **Ma'at Ethical Scoring** — 7-principle ethical alignment measurement
- **Family Overwatch Dashboard** — Household behavioral health monitoring

---

## Core Framework

### Stanfield's Axiom of Perpetuity (SAP) — 10 Stages

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Seed | Dormant potential, pre-emergence |
| 2 | Sprout | Initial activation, fragile growth |
| 3 | Growth | Expanding capability and reach |
| 4 | Momentum | Accelerating development |
| 5 | Peak | Maximum performance and stability |
| 6 | Plateau | Stagnation begins, efficiency drops |
| 7 | Decline | Visible deterioration, tension rising |
| 8 | Crisis | Active failure, high TrapScore |
| 9 | Collapse | Systemic breakdown |
| 10 | Dissolution/Rebirth | Terminal decay or transformation |

### The Container Rule (Digit Vessel)
A mathematical principle where `content digit + container digit → digital root = SAP stage`. Used to map entity relationships to developmental stage with Magnetic Drag, Pivot/Flip, Harmonic Resonance, and Dissolve thresholds.

### TrapScore Formula
```
TrapScore = Stage × Rigidity × (1 − Adaptability)
```
Scores above 6.0 indicate high failure risk. Stage 8+ with TrapScore > 7.5 triggers the 7-Layer Defense response.

---

## REST API (`main.py`)

Built with **FastAPI** and **Pydantic v2**. Exposes both engines through a single service.

```
GET  /                          # Health check
GET  /health                    # Detailed system status
POST /omega/assess_individual   # SPAT individual assessment
POST /omega/assess_company      # Corporate SAP analysis
POST /omega/assess_portfolio    # Portfolio behavior staging
POST /omega/scan_ai_content     # AI safety / manipulation detection
GET  /omega/family_dashboard    # Household behavioral overview
POST /overwatch/analyze         # Infrastructure NSDT analysis
POST /overwatch/container_rule  # Digit vessel calculation
GET  /overwatch/validate        # Engine validation check
```

---

## Deployment

### Docker
```bash
docker build -t luminark .
docker run -p 8000:8000 luminark
```

### Local
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Requirements
```
fastapi==0.111.0
uvicorn[standard]==0.29.0
pydantic==2.7.1
```

---

## Testing

```bash
python -m pytest test_omega.py -v
```

40+ unit tests covering all major modules across both engines.

---

## Validated Case Studies

- **Texas Winter Storm Uri (2021)** — ULTRA retroactively stages the grid failure trajectory, detecting Stage 8 trap conditions 72+ hours before blackout
- **Hurricane Milton / Helene** — Storm-force validation of BioSensory fusion and InfraPhysics velocity prediction
- **Corporate Archetype Mapping** — OMEGA correctly classifies Fortune 500 behavioral archetypes against historical patterns

---

## Licensing

LUMINARK is available for OEM licensing under three tiers:

| Tier | Use Case | Model |
|------|----------|-------|
| Developer | Integration & prototyping | Per-seat annual |
| OEM Standard | Embedded product use | Royalty + flat fee |
| OEM Enterprise | Full white-label deployment | Custom negotiated |

For licensing inquiries: **info.rstanfield@gmail.com**

---

## Repository Structure

```
├── LUMINARK_OVERWATCH_PRIME_ULTRA.py     # Infrastructure engine (2,515 lines)
├── LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA.py # Consciousness engine (2,263 lines)
├── main.py                               # FastAPI unified REST API
├── test_omega.py                         # Full test suite (40+ tests)
├── Dockerfile                            # Container deployment
├── requirements.txt                      # Python dependencies
├── SBIR_Phase1_Narrative.md              # DOE SBIR Phase I grant narrative
├── luminark_modules/                     # Module split architecture plan
│   ├── __init__.py
│   └── MODULE_SPLIT_PLAN.md
└── docs/
    ├── images/
    │   ├── telemetry-flow.svg            # Telemetry to Actionable Insight diagram
    │   └── dual-engine-architecture.svg  # Unified Dual-Engine Architecture diagram
    └── version-comparison.csv            # Version evolution comparison table
```

---

*© 2026 Meridian Axiom Alignment Technologies. All rights reserved.*
*LUMINARK® is a registered trademark of Richard L. Stanfield.*
