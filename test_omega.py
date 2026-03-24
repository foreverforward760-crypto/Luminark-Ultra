"""
LUMINARK CONSCIOUSNESS ENGINE OMEGA — Test Suite
=================================================
Run with:  python test_omega.py
Or:        python -m pytest test_omega.py -v

Tests cover every major class and method in the engine.
Author: Richard L. Stanfield / Meridian Axiom Alignment Technologies
"""

import sys, os, unittest

# Ensure engine file is importable from same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA import (
    ConsciousnessEngine, SPATVector, SAPStage,
    CorporateConsciousnessAnalyzer, MERIDIANAdapter,
    LuminarkGuardian, LuminarkConsciousnessEngineOmega,
    NoctilucanStageAssessment, Stage8TrapDetector,
    DigitalRootCalculator, NoctilucanEconomicIndex,
    CrossIndicatorTumblingIndex, ThresholdOutcomePredictor,
    EnhancedSentinelClarity, PhysicsVelocityEngine,
    ContainerRuleEngine, get_archetype, assign_transitional_code,
)


# ── helpers ────────────────────────────────────────────────────────────────────

def make_spat(c=5, s=5, t=5, a=5, co=5, lv="growth"):
    return SPATVector(complexity=c, stability=s, tension=t,
                      adaptability=a, coherence=co, life_vector=lv)


# ── ConsciousnessEngine ────────────────────────────────────────────────────────

class TestConsciousnessEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ConsciousnessEngine()

    def test_calculate_stage_returns_valid_range(self):
        for vals in [(0,0,0,0,0), (10,10,10,10,10), (5,5,5,5,5), (3,7,2,8,1)]:
            spat = make_spat(*vals)
            stage = self.engine.calculate_stage(spat)
            self.assertIn(stage, range(10), f"Stage {stage} out of range for spat {vals}")

    def test_stage_0_low_all(self):
        """Very low SPAT should map to early stages."""
        spat = make_spat(0.1, 0.1, 0.1, 0.1, 0.1)
        stage = self.engine.calculate_stage(spat)
        self.assertLessEqual(stage, 3)

    def test_stage_high_complexity_tension(self):
        """High complexity and tension without stability → late-stage warning."""
        spat = make_spat(c=9.5, s=1.0, t=9.0, a=1.0, co=1.0)
        stage = self.engine.calculate_stage(spat)
        self.assertGreaterEqual(stage, 6)

    def test_micro_position_bounds(self):
        spat = make_spat(5, 5, 5, 5, 5)
        stage = self.engine.calculate_stage(spat)
        micro = self.engine.calculate_micro_position(spat, stage)
        self.assertGreaterEqual(micro, 0.0)
        self.assertLessEqual(micro, 1.0)

    def test_trap_score_keys(self):
        spat = make_spat(8, 2, 9, 1, 2)
        stage = self.engine.calculate_stage(spat)
        ts = self.engine.calculate_trap_score(spat, stage)
        for key in ("raw", "normalized", "risk_level"):
            self.assertIn(key, ts)

    def test_trap_score_stage8_is_high(self):
        """Stage 8 with high tension should produce HIGH or CRITICAL trap score."""
        spat = make_spat(c=9, s=2, t=9, a=1, co=2)
        stage = self.engine.calculate_stage(spat)
        ts = self.engine.calculate_trap_score(spat, stage)
        self.assertIn(ts["risk_level"], ("HIGH", "CRITICAL"))

    def test_velocity_calculation(self):
        history = [
            {"stage": 3, "timestamp": "2026-01-01"},
            {"stage": 4, "timestamp": "2026-02-01"},
            {"stage": 5, "timestamp": "2026-03-01"},
        ]
        vel = self.engine.calculate_velocity(history)
        self.assertIn("trend", vel)

    def test_inversion_principle_keys(self):
        spat = make_spat(5, 5, 5, 5, 5)
        stage = self.engine.calculate_stage(spat)
        inv = self.engine.check_inversion_principle(spat, stage)
        self.assertIn("inversion_active", inv)


# ── CorporateConsciousnessAnalyzer ────────────────────────────────────────────

class TestCorporateAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = CorporateConsciousnessAnalyzer()

    def test_analyze_company_keys(self):
        data = {"revenue_growth_pct": 20, "operating_margin": 18, "debt_to_equity": 0.5,
                "rd_spend_pct": 8, "employee_turnover_pct": 10, "cash_burn_rate": 0,
                "market_cap_change_yoy": 30, "leadership_changes_12m": 0}
        result = self.analyzer.analyze_company("TestCo", "TST", data)
        for key in ("company", "stage", "stage_name", "trap_score", "investment_signal"):
            self.assertIn(key, result)

    def test_stage_range(self):
        data = {"revenue_growth_pct": 5, "operating_margin": -5, "debt_to_equity": 8,
                "rd_spend_pct": 1, "employee_turnover_pct": 30, "cash_burn_rate": 6,
                "market_cap_change_yoy": -30, "leadership_changes_12m": 3}
        result = self.analyzer.analyze_company("Distressed", "DIS", data)
        self.assertIn(result["stage"], range(10))

    def test_batch_analyze_length(self):
        companies = [
            {"company": "A", "ticker": "AA", "revenue_growth_pct": 10, "operating_margin": 12,
             "debt_to_equity": 1.0, "rd_spend_pct": 4, "employee_turnover_pct": 12,
             "cash_burn_rate": 0, "market_cap_change_yoy": 5, "leadership_changes_12m": 0},
            {"company": "B", "ticker": "BB", "revenue_growth_pct": -5, "operating_margin": -2,
             "debt_to_equity": 6.0, "rd_spend_pct": 1, "employee_turnover_pct": 25,
             "cash_burn_rate": 4, "market_cap_change_yoy": -20, "leadership_changes_12m": 2},
        ]
        results = self.analyzer.batch_analyze(companies)
        self.assertEqual(len(results), 2)


# ── MERIDIANAdapter ───────────────────────────────────────────────────────────

class TestMeridian(unittest.TestCase):

    def setUp(self):
        self.meridian = MERIDIANAdapter()

    def test_portfolio_keys(self):
        portfolio = {"win_rate_pct": 55, "avg_hold_days": 30, "top3_concentration_pct": 40,
                     "max_drawdown_pct": 12, "leverage_ratio": 1.0,
                     "plan_overrules_30d": 1, "portfolio_correlation": 0.5}
        result = self.meridian.analyze_portfolio_behavior(portfolio)
        for key in ("portfolio_stage", "stage_name", "trap_score", "meridian_advice"):
            self.assertIn(key, result)

    def test_high_leverage_increases_tension(self):
        """High leverage + many overrules should → higher stage or trap risk."""
        portfolio = {"win_rate_pct": 40, "avg_hold_days": 5, "top3_concentration_pct": 80,
                     "max_drawdown_pct": 35, "leverage_ratio": 4.0,
                     "plan_overrules_30d": 10, "portfolio_correlation": 0.95}
        result = self.meridian.analyze_portfolio_behavior(portfolio)
        self.assertGreaterEqual(result["portfolio_stage"], 5)


# ── LuminarkGuardian ──────────────────────────────────────────────────────────

class TestGuardian(unittest.TestCase):

    def setUp(self):
        self.guardian = LuminarkGuardian()

    def test_scan_returns_keys(self):
        result = self.guardian.scan_content("This is great content.", 4)
        for key in ("maat_score", "action"):
            self.assertIn(key, result)

    def test_manipulative_text_low_score(self):
        text = "ACT NOW! You MUST buy this immediately or lose everything forever!"
        result = self.guardian.scan_content(text, 4)
        self.assertLess(result["maat_score"], 6.0)

    def test_family_dashboard_length(self):
        result = self.guardian.get_family_status_mock(["Alice", "Bob", "Carol"])
        self.assertEqual(len(result), 3)


# ── LuminarkConsciousnessEngineOmega (unified engine) ───────────────────────

class TestOmegaEngine(unittest.TestCase):

    def setUp(self):
        self.omega = LuminarkConsciousnessEngineOmega()

    def test_assess_individual(self):
        result = self.omega.assess_individual(
            {"complexity": 6, "stability": 5, "tension": 4, "adaptability": 7, "coherence": 6}
        )
        self.assertIn("stage", result)
        self.assertIn(result["stage"], range(10))

    def test_assess_company(self):
        result = self.omega.assess_company(
            "NVIDIA", "NVDA",
            {"revenue_growth_pct": 120, "operating_margin": 55, "debt_to_equity": 0.4,
             "rd_spend_pct": 15, "employee_turnover_pct": 8, "cash_burn_rate": 0,
             "market_cap_change_yoy": 180, "leadership_changes_12m": 0}
        )
        self.assertEqual(result["company"], "NVIDIA")
        self.assertIn("stage", result)

    def test_assess_portfolio_behavior(self):
        result = self.omega.assess_portfolio_behavior(
            {"win_rate_pct": 55, "avg_hold_days": 45, "top3_concentration_pct": 65,
             "max_drawdown_pct": 15, "leverage_ratio": 1.0,
             "plan_overrules_30d": 2, "portfolio_correlation": 0.82}
        )
        self.assertIn("portfolio_stage", result)

    def test_scan_ai_content(self):
        result = self.omega.scan_ai_content("I definitely know the answer 100%.", 5)
        self.assertIn("maat_score", result)

    def test_family_dashboard(self):
        result = self.omega.family_dashboard(["Rick", "Daughter"])
        self.assertIn("Rick", result)
        self.assertIn("Daughter", result)

    def test_version_info(self):
        info = self.omega.get_version_info()
        self.assertIn("version", info)
        self.assertIn("live_url", info)


# ── NoctilucanStageAssessment ─────────────────────────────────────────────────

class TestNSAT(unittest.TestCase):

    def setUp(self):
        self.nsat = NoctilucanStageAssessment()

    def test_calculate_stage_returns_string(self):
        code = self.nsat.calculate_stage(
            self_report={5: 0.8, 6: 0.4},
            interview={5: 0.7},
            observation={5: 0.6},
            diary={5: 0.9},
        )
        self.assertIsInstance(code, str)

    def test_decimal_stage_format(self):
        """Stage codes should be 'X.Y' format."""
        code = self.nsat.calculate_stage(
            self_report={4: 0.9}, interview={4: 0.8},
            observation={4: 0.7}, diary={4: 0.6},
        )
        parts = code.split(".")
        self.assertEqual(len(parts), 2)


# ── Stage8TrapDetector ────────────────────────────────────────────────────────

class TestTrapDetector(unittest.TestCase):

    def setUp(self):
        self.detector = Stage8TrapDetector()

    def test_high_risk_system(self):
        result = self.detector.detect({
            "communications": "We are absolutely unstoppable and will never fail.",
            "accepts_feedback": False,
            "revises_beliefs": False,
            "acknowledges_uncertainty": False,
            "teaches_others": True,
            "seeks_mentorship": False,
            "claims": "Too big to fail.",
        })
        self.assertIn(result["risk_level"], ("HIGH", "CRITICAL"))

    def test_healthy_system_low_risk(self):
        result = self.detector.detect({
            "communications": "We are open to feedback and still learning.",
            "accepts_feedback": True,
            "revises_beliefs": True,
            "acknowledges_uncertainty": True,
            "teaches_others": True,
            "seeks_mentorship": True,
            "claims": "We may be wrong about some things.",
        })
        self.assertIn(result["risk_level"], ("LOW", "MODERATE"))

    def test_result_keys(self):
        result = self.detector.detect({"communications": "test"})
        for key in ("risk_level", "risk_score", "max_score", "red_flags", "intervention"):
            self.assertIn(key, result)


# ── DigitalRootCalculator ─────────────────────────────────────────────────────

class TestDigitalRoot(unittest.TestCase):

    def test_known_values(self):
        self.assertEqual(DigitalRootCalculator.calculate(9), 9)
        self.assertEqual(DigitalRootCalculator.calculate(18), 9)
        self.assertEqual(DigitalRootCalculator.calculate(19), 1)
        self.assertEqual(DigitalRootCalculator.calculate(99), 9)
        self.assertEqual(DigitalRootCalculator.calculate(100), 1)


# ── CrossIndicatorTumblingIndex ────────────────────────────────────────────────

class TestCITI(unittest.TestCase):

    def setUp(self):
        self.citi = CrossIndicatorTumblingIndex()

    def test_analyze_economy_keys(self):
        result = self.citi.analyze_economy(2.8, 3.9, 3.2, 124.0, 2.1)
        for key in ("nei_stage", "nei_narrative", "citi_score", "citi_alert", "recommendation"):
            self.assertIn(key, result)

    def test_crisis_conditions_high_alert(self):
        """Stagflation scenario should trigger elevated CITI alert."""
        result = self.citi.analyze_economy(
            gdp=-2.0, unemployment=9.0, inflation=8.5, debt=160.0, asset_deviation=4.0
        )
        self.assertIn(result["citi_alert"], ("ORANGE", "RED"))


# ── ThresholdOutcomePredictor ─────────────────────────────────────────────────

class TestThresholdPredictor(unittest.TestCase):

    def setUp(self):
        self.predictor = ThresholdOutcomePredictor()

    def test_predict_keys(self):
        result = self.predictor.predict({
            "foundation_strength": 0.7, "support_quality": 0.65,
            "material_resources": 0.55, "psychological_readiness": 0.7,
            "stage_4_duration": 18, "prior_threshold_successes": 1, "stress_level": 4.5,
        })
        for key in ("primary_outcome", "confidence", "probabilities", "recommendations"):
            self.assertIn(key, result)

    def test_probabilities_sum_to_one(self):
        result = self.predictor.predict({
            "foundation_strength": 0.5, "support_quality": 0.5,
            "material_resources": 0.5, "psychological_readiness": 0.5,
            "stage_4_duration": 10, "prior_threshold_successes": 0, "stress_level": 5.0,
        })
        total = sum(result["probabilities"].values())
        self.assertAlmostEqual(total, 1.0, places=2)


# ── EnhancedSentinelClarity ───────────────────────────────────────────────────

class TestSentinelClarity(unittest.TestCase):

    def setUp(self):
        self.sentinel = EnhancedSentinelClarity()

    def test_permanence_maps_to_stage8(self):
        text = "I definitely know the answer and it is absolutely impossible to be wrong."
        result = self.sentinel.analyze_output(text, confidence=0.99)
        self.assertEqual(result["assigned_stage"], 8)

    def test_hedging_lower_stage(self):
        text = "This appears to be the case, though I recommend consulting an expert."
        result = self.sentinel.analyze_output(text, confidence=0.65)
        self.assertLess(result["assigned_stage"], 8)

    def test_result_keys(self):
        result = self.sentinel.analyze_output("Test text.", 0.75)
        for key in ("assigned_stage", "stage_label", "intervention_level"):
            self.assertIn(key, result)


# ── PhysicsVelocityEngine ─────────────────────────────────────────────────────

class TestPhysicsVelocityEngine(unittest.TestCase):

    def setUp(self):
        self.pve = PhysicsVelocityEngine()

    def test_momentum_bounds(self):
        result = self.pve.calculate_momentum(stage=5.3, integrity=0.72, tension=0.45)
        self.assertGreaterEqual(result["velocity"], 0.0)
        self.assertLessEqual(result["velocity"], 1.0)

    def test_zero_integrity_stalled(self):
        result = self.pve.calculate_momentum(stage=5.0, integrity=0.0, tension=0.5)
        self.assertEqual(result["velocity"], 0.0)

    def test_stage_velocity_direction(self):
        result = self.pve.calculate_stage_velocity(3.0, 6.0, 0, 30, "days")
        self.assertIn("DEGRADING", result["direction"])

    def test_stage_velocity_recovering(self):
        result = self.pve.calculate_stage_velocity(7.0, 4.0, 0, 30, "days")
        self.assertIn("RECOVERING", result["direction"])

    def test_time_error_handling(self):
        result = self.pve.calculate_stage_velocity(3.0, 6.0, 30, 20, "days")
        self.assertIn("error", result)


# ── ContainerRuleEngine ───────────────────────────────────────────────────────

class TestContainerRuleEngine(unittest.TestCase):

    def setUp(self):
        self.cre = ContainerRuleEngine()

    def test_analyze_keys(self):
        result = self.cre.analyze(content_digit=7, container_digit=2, current_sap_stage=8)
        for key in ("input", "staging", "magnetic_drag", "pivot_flip",
                    "trap_zone", "harmonic_resonance", "flux_dynamics"):
            self.assertIn(key, result)

    def test_stage9_harmonic_resonance(self):
        result = self.cre.analyze(content_digit=8, container_digit=1)
        self.assertTrue(result["harmonic_resonance"]["harmonic_resonance"])

    def test_trap_zone_stage78(self):
        result = self.cre.analyze(content_digit=6, container_digit=3)
        self.assertTrue(result["trap_zone"]["in_trap"])

    def test_digital_root_consistency(self):
        """Result stage should match digital root of content+container."""
        for c, co in [(1,8), (2,7), (3,6), (4,5), (5,4), (6,3), (7,2), (8,1)]:
            r = self.cre.analyze(c, co)
            dr = DigitalRootCalculator.calculate(c + co)
            self.assertEqual(r["staging"]["stage"], dr,
                             f"Failed for content={c} container={co}")


# ── Archetype & Transitional Code ─────────────────────────────────────────────

class TestArchetypeAndTransitional(unittest.TestCase):

    def test_get_archetype_all_stages(self):
        for stage in range(10):
            arch = get_archetype(stage)
            self.assertIn("name", arch)
            self.assertIn("meaning", arch)

    def test_assign_transitional_code_returns_code(self):
        result = assign_transitional_code(
            primary_criteria_met={"primary_1": True, "primary_2": True},
            supporting_criteria={"support_1": True},
            exclusion_criteria={"exclusion_1": False},
            entry_signals={"signal_1": True},
        )
        self.assertIn("stage_code", result)
        self.assertIn("confidence", result)


# ── run ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    for cls in [
        TestConsciousnessEngine, TestCorporateAnalyzer, TestMeridian,
        TestGuardian, TestOmegaEngine, TestNSAT, TestTrapDetector,
        TestDigitalRoot, TestCITI, TestThresholdPredictor,
        TestSentinelClarity, TestPhysicsVelocityEngine, TestContainerRuleEngine,
        TestArchetypeAndTransitional,
    ]:
        suite.addTests(loader.loadTestsFromTestCase(cls))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
