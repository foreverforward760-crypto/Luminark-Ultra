"""
LUMINARK CONSCIOUSNESS ENGINE OMEGA — Module Package
=====================================================
Meridian Axiom Alignment Technologies — Richard L. Stanfield

Package structure:
    luminark_modules/
        __init__.py          ← this file (convenience imports)
        core.py              ← SPATVector, ConsciousnessEngine, SAPStage, StageLibrary
        corporate.py         ← CorporateConsciousnessAnalyzer, MERIDIANAdapter
        defense.py           ← SevenLayerDefenseSystem, all protocol classes
        guardian.py          ← LuminarkGuardian, OracleEngine
        assessment.py        ← PersonalAssessmentEngine
        nsat.py              ← NoctilucanStageAssessment, assign_transitional_code
        trap.py              ← Stage8TrapDetector
        economics.py         ← NoctilucanEconomicIndex, CrossIndicatorTumblingIndex
        predictor.py         ← ThresholdOutcomePredictor
        sentinel.py          ← EnhancedSentinelClarity
        velocity.py          ← PhysicsVelocityEngine
        container_rule.py    ← ContainerRuleEngine
        engine.py            ← LuminarkConsciousnessEngineOmega (unified entry point)

Usage (after split):
    from luminark_modules import LuminarkConsciousnessEngineOmega
    omega = LuminarkConsciousnessEngineOmega()
    result = omega.assess_individual({...})

NOTE: Until the split is complete, the monolithic file remains the
authoritative source. This package structure is the target architecture.
"""

# Convenience re-exports once modules are split
# from luminark_modules.engine import LuminarkConsciousnessEngineOmega
# from luminark_modules.core import ConsciousnessEngine, SPATVector, SAPStage
# from luminark_modules.nsat import NoctilucanStageAssessment
# from luminark_modules.trap import Stage8TrapDetector
# from luminark_modules.economics import CrossIndicatorTumblingIndex
# from luminark_modules.predictor import ThresholdOutcomePredictor
# from luminark_modules.sentinel import EnhancedSentinelClarity
# from luminark_modules.velocity import PhysicsVelocityEngine
# from luminark_modules.container_rule import ContainerRuleEngine

__version__ = "1.0.0"
__author__  = "Richard L. Stanfield / Meridian Axiom Alignment Technologies"
