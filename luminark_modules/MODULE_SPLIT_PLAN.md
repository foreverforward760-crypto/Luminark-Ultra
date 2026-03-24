# LUMINARK Module Split Plan
## Meridian Axiom Alignment Technologies

This document is the step-by-step engineering guide for splitting
`LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA.py` (2,263 lines) into
maintainable, independently importable modules.

---

## Target Structure

```
luminark_modules/
├── __init__.py              ← package init + re-exports
├── core.py                  ← SPATVector, SAPStage, ConsciousnessEngine, StageLibrary
├── corporate.py             ← CorporateConsciousnessAnalyzer, MERIDIANAdapter
├── defense.py               ← IblisProtocol, SophianicWisdomProtocol,
│                               LightIntegrationProtocol, OctoCamouflage,
│                               MycelialContainment, YunusProtocol,
│                               HarrowingProtocol, SevenLayerDefenseSystem
├── guardian.py              ← OracleEngine, LuminarkGuardian
├── assessment.py            ← PersonalAssessmentEngine
├── nsat.py                  ← NoctilucanStageAssessment, assign_transitional_code,
│                               get_archetype, NAM_ARCHETYPES
├── trap.py                  ← Stage8TrapDetector, DigitalRootCalculator
├── economics.py             ← NoctilucanEconomicIndex, CrossIndicatorTumblingIndex
├── predictor.py             ← ThresholdOutcomePredictor
├── sentinel.py              ← EnhancedSentinelClarity
├── velocity.py              ← PhysicsVelocityEngine
├── container_rule.py        ← ContainerRuleEngine, CONTAINER_RULE_TABLE
└── engine.py                ← LuminarkConsciousnessEngineOmega (imports all above)
```

---

## Line Ranges in the Monolithic File

| Module         | Lines         | Key Classes / Functions                    |
|----------------|---------------|---------------------------------------------|
| core.py        | 1 – 350       | SPATVector, SAPStage, ConsciousnessEngine, StageLibrary |
| corporate.py   | 351 – 750     | CorporateConsciousnessAnalyzer, MERIDIANAdapter |
| defense.py     | 751 – 880     | All protocol classes, SevenLayerDefenseSystem |
| guardian.py    | 396 – 560     | OracleEngine, LuminarkGuardian              |
| assessment.py  | 924 – 1045    | PersonalAssessmentEngine                   |
| engine.py      | 1046 – 1095   | LuminarkConsciousnessEngineOmega            |
| nsat.py        | 1096 – 1313   | NAM_ARCHETYPES, get_archetype, NoctilucanStageAssessment, assign_transitional_code |
| trap.py        | 1314 – 1465   | Stage8TrapDetector, DigitalRootCalculator  |
| economics.py   | 1466 – 1600   | NoctilucanEconomicIndex, CrossIndicatorTumblingIndex |
| predictor.py   | 1601 – 1705   | ThresholdOutcomePredictor                  |
| sentinel.py    | 1706 – 1833   | EnhancedSentinelClarity                    |
| velocity.py    | 1834 – 1949   | PhysicsVelocityEngine                      |
| container_rule.py | 1950 – 2094| ContainerRuleEngine, CONTAINER_RULE_TABLE  |

---

## Dependency Order (import without circular dependencies)

1. `core.py`           — no internal deps
2. `corporate.py`      — imports from core
3. `defense.py`        — imports from core
4. `guardian.py`       — imports from core, defense
5. `assessment.py`     — imports from core, defense, guardian
6. `nsat.py`           — no internal deps (standalone)
7. `trap.py`           — no internal deps (standalone)
8. `economics.py`      — imports DigitalRootCalculator from trap
9. `predictor.py`      — no internal deps
10. `sentinel.py`      — no internal deps
11. `velocity.py`      — no internal deps
12. `container_rule.py`— imports DigitalRootCalculator from trap
13. `engine.py`        — imports everything above

---

## Split Procedure (per module)

1. Copy the relevant line range from the monolithic file
2. Add the necessary imports at the top:
   ```python
   from .core import SPATVector, ConsciousnessEngine, STAGE_METADATA
   ```
3. Remove the class from the monolithic file
4. Add a compatibility import to the monolithic file:
   ```python
   from luminark_modules.corporate import CorporateConsciousnessAnalyzer
   ```
5. Run `test_omega.py` after each split to confirm nothing broke

---

## Status

| Module         | Status      |
|----------------|-------------|
| core.py        | ⬜ Pending  |
| corporate.py   | ⬜ Pending  |
| defense.py     | ⬜ Pending  |
| guardian.py    | ⬜ Pending  |
| assessment.py  | ⬜ Pending  |
| nsat.py        | ⬜ Pending  |
| trap.py        | ⬜ Pending  |
| economics.py   | ⬜ Pending  |
| predictor.py   | ⬜ Pending  |
| sentinel.py    | ⬜ Pending  |
| velocity.py    | ⬜ Pending  |
| container_rule.py | ⬜ Pending |
| engine.py      | ⬜ Pending  |
