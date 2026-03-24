"""
LUMINARK UNIFIED MASTER API — main.py
======================================
FastAPI server exposing both engines:
  • LUMINARK CONSCIOUSNESS ENGINE OMEGA  (human / organizational intelligence)
  • LUMINARK OVERWATCH PRIME ULTRA       (infrastructure / industrial intelligence)

Usage:
    pip install fastapi uvicorn
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Endpoints:
    GET  /                          → version + engine status
    POST /omega/assess_individual   → personal SAP assessment
    POST /omega/assess_company      → corporate consciousness analysis
    POST /omega/assess_portfolio    → financial portfolio behavior
    POST /omega/scan_ai_content     → AI content safety scan
    GET  /omega/family_dashboard    → family overwatch (demo data)
    POST /overwatch/analyze         → infrastructure system analysis
    POST /overwatch/container_rule  → Container Rule / Digit Vessel
    GET  /overwatch/validate        → historical hurricane validation
    GET  /health                    → liveness probe

Author : Richard L. Stanfield / Meridian Axiom Alignment Technologies
Version: 1.0 — March 2026
"""

import sys
import os

# ── ensure local engine files are importable ───────────────────────────────────
# When deployed, place both engine .py files in the same directory as main.py.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

try:
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel, Field
except ImportError:
    raise ImportError(
        "FastAPI not installed. Run: pip install fastapi uvicorn"
    )

# ── lazy-load engines so the API starts even if one has an issue ───────────────
_omega = None
_overwatch = None

def get_omega():
    global _omega
    if _omega is None:
        from LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA import LuminarkConsciousnessEngineOmega
        _omega = LuminarkConsciousnessEngineOmega()
    return _omega

def get_overwatch():
    global _overwatch
    if _overwatch is None:
        from LUMINARK_OVERWATCH_PRIME_ULTRA import LuminarkOverwatchPrimeUltra
        _overwatch = LuminarkOverwatchPrimeUltra()
    return _overwatch

# ── FastAPI app ────────────────────────────────────────────────────────────────
app = FastAPI(
    title="LUMINARK Unified API",
    description=(
        "Predictive stage intelligence for human consciousness, "
        "organizational health, and physical infrastructure."
    ),
    version="1.0.0",
    contact={"name": "Richard L. Stanfield", "email": "info.rstanfield@gmail.com"},
    license_info={"name": "Proprietary — Meridian Axiom Alignment Technologies"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten in production to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── request / response models ─────────────────────────────────────────────────

class SPATInput(BaseModel):
    """5-dimensional NSDT input vector. All values 0.0–10.0."""
    complexity:    float = Field(..., ge=0.0, le=10.0, description="System complexity / load")
    stability:     float = Field(..., ge=0.0, le=10.0, description="Operational stability")
    tension:       float = Field(..., ge=0.0, le=10.0, description="Internal stress / tension")
    adaptability:  float = Field(..., ge=0.0, le=10.0, description="Capacity to adapt / respond")
    coherence:     float = Field(..., ge=0.0, le=10.0, description="Cross-subsystem alignment")
    life_vector:   Optional[str] = Field("growth", description="Domain context (growth/finances/health/infra)")

class CompanyInput(BaseModel):
    name:                   str   = Field(..., description="Company name")
    ticker:                 str   = Field(..., description="Ticker symbol or identifier")
    revenue_growth_pct:     float = Field(10.0, description="Revenue growth %")
    operating_margin:       float = Field(15.0, description="Operating margin %")
    debt_to_equity:         float = Field(1.0,  description="Debt-to-equity ratio")
    rd_spend_pct:           float = Field(5.0,  description="R&D as % of revenue")
    employee_turnover_pct:  float = Field(15.0, description="Annual employee turnover %")
    cash_burn_rate:         float = Field(0.0,  description="Cash burn (0=positive CF, 10=extreme)")
    market_cap_change_yoy:  float = Field(0.0,  description="Market cap change YoY %")
    leadership_changes_12m: int   = Field(0,    description="Leadership changes in last 12 months")

class PortfolioInput(BaseModel):
    win_rate_pct:           float = Field(50.0, description="Win rate %")
    avg_hold_days:          float = Field(30.0, description="Average hold time in days")
    top3_concentration_pct: float = Field(40.0, description="% assets in top 3 positions")
    max_drawdown_pct:       float = Field(15.0, description="Maximum drawdown %")
    leverage_ratio:         float = Field(1.0,  description="Leverage multiplier (1.0 = no leverage)")
    plan_overrules_30d:     int   = Field(2,    description="Times investor broke own rules in 30 days")
    portfolio_correlation:  float = Field(0.5,  description="Portfolio correlation (0=diversified, 1=all same)")

class AIScanInput(BaseModel):
    text:       str = Field(..., description="Text to analyze for AI safety / manipulation")
    user_stage: int = Field(4,  ge=0, le=9, description="Operator's current SAP stage (0–9)")

class InfraInput(BaseModel):
    system_id:   str   = Field(..., description="Unique system identifier")
    system_type: str   = Field("generic", description="System type (power_grid, water, vehicle, etc.)")
    complexity:  float = Field(..., ge=0.0, le=10.0)
    stability:   float = Field(..., ge=0.0, le=10.0)
    tension:     float = Field(..., ge=0.0, le=10.0)
    adaptability:float = Field(..., ge=0.0, le=10.0)
    coherence:   float = Field(..., ge=0.0, le=10.0)

class ContainerRuleInput(BaseModel):
    content_digit:     int = Field(..., ge=1, le=9, description="Inner Drive / Load digit (1–9)")
    container_digit:   int = Field(..., ge=1, le=9, description="Outer Form / Capacity digit (1–9)")
    current_sap_stage: Optional[int] = Field(None, ge=0, le=9, description="Current SAP stage for cross-validation")

# ── utility ────────────────────────────────────────────────────────────────────

def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()

def _wrap(data: Any, endpoint: str) -> dict:
    return {"timestamp": _ts(), "endpoint": endpoint, "data": data}

# ── root ───────────────────────────────────────────────────────────────────────

@app.get("/", summary="API root — version and engine status")
async def root():
    omega_ok = True
    ow_ok    = True
    try:
        get_omega()
    except Exception as e:
        omega_ok = False
    try:
        get_overwatch()
    except Exception as e:
        ow_ok = False

    return _wrap({
        "api":      "LUMINARK Unified API v1.0",
        "company":  "Meridian Axiom Alignment Technologies",
        "contact":  "info.rstanfield@gmail.com",
        "engines": {
            "CONSCIOUSNESS_ENGINE_OMEGA":  "OK" if omega_ok else "ERROR — check engine file",
            "OVERWATCH_PRIME_ULTRA":       "OK" if ow_ok    else "ERROR — check engine file",
        },
        "docs":    "/docs",
    }, "/")

@app.get("/health", summary="Liveness probe for Docker/K8s")
async def health():
    return {"status": "ok", "timestamp": _ts()}

# ── OMEGA endpoints ────────────────────────────────────────────────────────────

@app.post("/omega/assess_individual",
          summary="Personal SAP stage assessment from SPAT vector")
async def assess_individual(spat: SPATInput):
    try:
        result = get_omega().assess_individual(spat.dict())
        return _wrap(result, "/omega/assess_individual")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/omega/assess_company",
          summary="Corporate consciousness analysis")
async def assess_company(company: CompanyInput):
    try:
        payload = company.dict()
        name    = payload.pop("name")
        ticker  = payload.pop("ticker")
        result  = get_omega().assess_company(name, ticker, payload)
        return _wrap(result, "/omega/assess_company")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/omega/assess_portfolio",
          summary="Financial portfolio behavioral analysis (MERIDIAN)")
async def assess_portfolio(portfolio: PortfolioInput):
    try:
        result = get_omega().assess_portfolio_behavior(portfolio.dict())
        return _wrap(result, "/omega/assess_portfolio")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/omega/scan_ai_content",
          summary="AI content safety scan (manipulation / Stage 8 permanence detection)")
async def scan_ai_content(payload: AIScanInput):
    try:
        result = get_omega().scan_ai_content(payload.text, payload.user_stage)
        return _wrap(result, "/omega/scan_ai_content")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/omega/family_dashboard",
         summary="Family Overwatch demo dashboard")
async def family_dashboard(members: str = "Rick,Daughter,Son"):
    try:
        member_list = [m.strip() for m in members.split(",") if m.strip()]
        result = get_omega().family_dashboard(member_list)
        return _wrap(result, "/omega/family_dashboard")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── OVERWATCH endpoints ───────────────────────────────────────────────────────

@app.post("/overwatch/analyze",
          summary="Infrastructure system SAP stage analysis")
async def overwatch_analyze(infra: InfraInput):
    try:
        payload = {
            "complexity":   infra.complexity,
            "stability":    infra.stability,
            "tension":      infra.tension,
            "adaptability": infra.adaptability,
            "coherence":    infra.coherence,
        }
        result = get_overwatch().analyze_system(
            infra.system_type, infra.system_id, payload
        )
        return _wrap(result, "/overwatch/analyze")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/overwatch/container_rule",
          summary="Container Rule / Digit Vessel analysis")
async def container_rule(cr: ContainerRuleInput):
    try:
        from LUMINARK_OVERWATCH_PRIME_ULTRA import InfraContainerRuleEngine
        engine = InfraContainerRuleEngine()
        result = engine.analyze(
            content_digit=cr.content_digit,
            container_digit=cr.container_digit,
            current_sap_stage=cr.current_sap_stage,
        )
        return _wrap(result, "/overwatch/container_rule")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/overwatch/validate",
         summary="Historical hurricane / grid validation (Milton + Helene + Uri)")
async def overwatch_validate():
    try:
        result = get_overwatch().run_historical_validation()
        return _wrap(result, "/overwatch/validate")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── error handler ──────────────────────────────────────────────────────────────

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc), "path": str(request.url)},
    )

# ── dev runner ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
