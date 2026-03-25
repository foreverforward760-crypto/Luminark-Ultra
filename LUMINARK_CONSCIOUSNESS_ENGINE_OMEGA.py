"""
================================================================================
 LUMINARK CONSCIOUSNESS ENGINE OMEGA  —  v1.0 CONSOLIDATED
 The Definitive Human & Organizational Intelligence System
================================================================================
 Consolidated from ALL consciousness-branch versions found across your files:
   - luminark_core.py (Quantum-Sapient Core, ToroidalAttention, QuantumMemoryBank)
   - sap_yunus package (stanfield_axiom.py, yunus_protocol.py, harrowing_protocol.py)
   - luminark-ai-oracle-architecture.md (GPT-4 Oracle integration, Stage Library)
   - Luminark V4 installation guide (sap_v4.py, quantum_spore.py, collective_consciousness.py)
   - Luminark V5.1 Bio-Bridge Integration Interface
   - luminark_overwatch_core.py (AI Guardian, MaatEthicalProtocol, Family Overwatch)
   - sap_corporate_analyzer.py (company SAP staging, investment signals)
   - luminark-assessment tool (personal assessment web app backend)
   - resurrect_system.py (7-layer defense installation: Iblis, Sophia, Light,
                          OctoCamouflage, Mycelium, Yunus, Harrowing)
   - luminark_mocks.py architecture (full dependency management)
   - MERIDIAN Financial Adapter (SAP Stock Trader → portfolio behavior analysis)
   - LUMINARK ANTIKYTHERA Oracle (MyQuantumAI Brain + GPT-4 Oracle)

 Framework: Stanfield's Axiom of Perpetuity (SAP)  |  10 Consciousness Stages
 Neural Architecture: ToroidalAttention (Patented — applied to human domain)
 Commercial Products: Personal Assessment | Corporate Analyzer | MERIDIAN | Oracle

 Author: Consolidated by LUMINARK AI Build System  —  March 2026
================================================================================
"""

import math
import json
import datetime
import random
import asyncio
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: CORE SAP FRAMEWORK  (Stanfield's Axiom of Perpetuity)
# ─────────────────────────────────────────────────────────────────────────────

class SAPStage(Enum):
    """
    Stanfield's Axiom of Perpetuity — 10 Consciousness / System Health Stages.
    The foundational framework underlying ALL LUMINARK consciousness products.
    Applies to: Individuals | Organizations | Financial systems | AI systems
    """
    PLENARA    = 0  # Void potential — zero, unmanifest, pure possibility
    SEED       = 1  # First impulse — inception, embryonic, beginning
    EMERGENCE  = 2  # Rising — first visibility, forming identity
    BREAKTHROUGH = 3 # Peak energy — eruption, creative explosion
    FOUNDATION = 4  # Stability — integration, structure building, consolidation
    THRESHOLD  = 5  # Crisis point — irreversible choice, bilateral tension
    EXPRESSION = 6  # Authentic flow — alignment, purpose in motion
    CRISIS     = 7  # Purification — forced reckoning, shadow confrontation
    RIGIDITY   = 8  # Permanence trap — omniscience illusion, frozen certainty
    VOID       = 9  # Dissolution — death/rebirth cycle, return to zero


# Detailed stage metadata: name, subtitle, geometry, polyvagal state, duration
STAGE_METADATA = {
    0: {"name": "PLENARA",     "subtitle": "Void Potential",         "geometry": "point",     "polyvagal": "ventral", "avg_days": "variable"},
    1: {"name": "SEED",        "subtitle": "First Impulse",          "geometry": "circle",    "polyvagal": "ventral", "avg_days": "7-30"},
    2: {"name": "EMERGENCE",   "subtitle": "Rising Identity",        "geometry": "crescent",  "polyvagal": "ventral", "avg_days": "30-90"},
    3: {"name": "BREAKTHROUGH","subtitle": "Creative Explosion",     "geometry": "triangle",  "polyvagal": "sympathetic", "avg_days": "14-60"},
    4: {"name": "FOUNDATION",  "subtitle": "Integration & Structure","geometry": "square",    "polyvagal": "ventral", "avg_days": "90-365"},
    5: {"name": "THRESHOLD",   "subtitle": "Crisis Point — Irreversible Choice","geometry": "pentagon","polyvagal": "sympathetic","avg_days": "30-90"},
    6: {"name": "EXPRESSION",  "subtitle": "Authentic Flow",         "geometry": "hexagon",   "polyvagal": "ventral", "avg_days": "90-730"},
    7: {"name": "CRISIS",      "subtitle": "Purification — Shadow Confrontation","geometry": "heptagon","polyvagal": "dorsal","avg_days": "14-180"},
    8: {"name": "RIGIDITY",    "subtitle": "Permanence Trap — Omniscience Illusion","geometry": "octagon","polyvagal": "sympathetic","avg_days": "variable"},
    9: {"name": "VOID",        "subtitle": "Dissolution — Death/Rebirth","geometry": "nonagon","polyvagal": "dorsal","avg_days": "variable"},
}

# 369 Resonance pattern (Tesla's harmonic law applied to SAP)
RESONANCE_369 = {
    3: "CREATION_POINT — Stage 3 carries maximum creative force (Tesla pattern)",
    6: "HARMONY_POINT — Stage 6 is pure alignment; 3×2 resonance",
    9: "COMPLETION_POINT — Stage 9 is dissolution; 3×3; full cycle",
    0: "VOID_RETURN — Zero is both end and beginning; Plenara resonance",
}


@dataclass
class SPATVector:
    """
    SPAT — Stanfield's Personal Axiom Tensor (Human domain NSDT equivalent).
    The 5-dimensional consciousness health vector.

    Dimensions (each 0.0–10.0):
        complexity    — Life/system load and cognitive demands
        stability     — Structural groundedness, consistency
        tension       — Internal pressure, unresolved conflict
        adaptability  — Capacity to shift, respond, transform
        coherence     — Alignment between values, actions, identity

    Inversion Principle: Physical and spiritual stability can be INVERSE.
    (Stage 5: Physical chaos + Spiritual clarity coexist)
    """
    complexity:    float = 5.0
    stability:     float = 5.0
    tension:       float = 5.0
    adaptability:  float = 5.0
    coherence:     float = 5.0
    life_vector:   str   = "growth"    # career|relationship|health|finances|family|growth
    assessment_id: str   = field(default_factory=lambda: f"A{random.randint(10000,99999)}")
    timestamp:     str   = field(default_factory=lambda: datetime.datetime.now().isoformat())

    def to_dict(self) -> Dict:
        return {
            "complexity": self.complexity, "stability": self.stability,
            "tension": self.tension, "adaptability": self.adaptability,
            "coherence": self.coherence, "life_vector": self.life_vector,
        }

    def check_resonance(self) -> Optional[str]:
        """Check if current state aligns with 369 resonance."""
        avg = (self.complexity + self.stability + self.tension +
               self.adaptability + self.coherence) / 5.0
        stage_approx = round(avg)
        return RESONANCE_369.get(stage_approx % 10)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: CONSCIOUSNESS STAGING ENGINE
# ─────────────────────────────────────────────────────────────────────────────

class ConsciousnessEngine:
    """
    Maps SPAT vectors to SAP consciousness stages with micro-precision.
    Implements the full 10-stage algorithm calibrated from human behavioral data.
    Incorporates the Inversion Principle, Stage 8 Omniscience Trap detection,
    and velocity/trajectory calculation.
    """

    def calculate_stage(self, spat: SPATVector) -> int:
        """Maps 5D SPAT vector to SAP stage (0–9)."""
        t   = spat.tension
        s   = spat.stability
        c   = spat.complexity
        a   = spat.adaptability
        coh = spat.coherence

        # VOID (9): Full dissolution — extremely high tension OR near-zero everything
        if (t >= 9.0 and s <= 1.0) or (t >= 8.5 and coh <= 1.0 and s <= 1.5):
            return 9

        # RIGIDITY (8): The Omniscience Trap — Inversion Principle active
        # Externally stable + high complexity + low adaptability = permanently frozen
        if s >= 7.5 and c >= 7.0 and a <= 2.5 and t >= 5.0:
            return 8

        # CRISIS (7): Purification — forced shadow confrontation
        if t >= 7.0 and s <= 3.5 and coh <= 3.5:
            return 7

        # EXPRESSION (6): Authentic flow — high adaptability, aligned
        if a >= 6.5 and coh >= 6.5 and t <= 5.0 and s >= 5.5:
            return 6

        # THRESHOLD (5): Crisis point — bilateral tension
        # Physical chaos + spiritual clarity (Inversion Principle)
        if t >= 4.5 and s <= 5.5 and c >= 4.0:
            return 5

        # FOUNDATION (4): Integration and structure
        if s >= 6.5 and t <= 4.0 and coh >= 5.5:
            return 4

        # BREAKTHROUGH (3): Creative explosion — peak energy
        if a >= 6.0 and c >= 5.0 and t <= 3.5 and coh >= 5.0:
            return 3

        # EMERGENCE (2): Rising identity
        if c >= 3.0 and s >= 6.0 and t <= 3.0:
            return 2

        # SEED (1): First impulse — awakening
        if s >= 7.0 and t <= 2.0 and c <= 3.0:
            return 1

        # PLENARA (0): Void / dormant potential
        if t <= 1.5 and c <= 1.5 and s <= 2.0:
            return 0

        return self._weighted_stage(spat)

    def _weighted_stage(self, spat: SPATVector) -> int:
        score = (
            (spat.tension         * 0.35) +
            ((10 - spat.stability)     * 0.25) +
            (spat.complexity       * 0.15) +
            ((10 - spat.adaptability)  * 0.15) +
            ((10 - spat.coherence)     * 0.10)
        )
        thresholds = [8, 15, 22, 30, 38, 47, 57, 68, 80]
        for stage, thresh in enumerate(thresholds):
            if score <= thresh:
                return stage
        return 9

    def calculate_micro_position(self, spat: SPATVector, stage: int) -> float:
        """
        Calculate precise micro-position within stage (e.g., 5.73 not just "5").
        Used by the AI Oracle for precision personalization.
        Derived from MyQuantumAI Toroidal Attention precision model.
        """
        # Sub-stage position (0.0–0.99) based on vector dynamics
        tension_norm  = spat.tension / 10.0
        stability_inv = (10.0 - spat.stability) / 10.0
        adapt_norm    = spat.adaptability / 10.0
        coh_norm      = spat.coherence / 10.0

        # Fractional position within stage
        micro = (tension_norm * 0.4 + stability_inv * 0.3 +
                 (1 - adapt_norm) * 0.2 + (1 - coh_norm) * 0.1)
        micro = min(0.99, max(0.0, micro))

        return round(stage + micro, 2)

    def calculate_velocity(self, history: List[Dict]) -> Dict:
        """
        Calculate trajectory velocity: accelerating | steady | stalled.
        Used to personalize Oracle warnings about urgency.
        """
        if len(history) < 2:
            return {"type": "steady", "magnitude": 0.5, "trajectory": "insufficient_data"}

        stages = [h.get("stage", 4) for h in history[-4:]]
        stage_delta = stages[-1] - stages[0]

        if abs(stage_delta) >= 2:
            velocity_type = "accelerating" if stage_delta > 0 else "recovering_fast"
            magnitude = 0.85
        elif abs(stage_delta) == 1:
            velocity_type = "steady" if stage_delta > 0 else "recovering"
            magnitude = 0.60
        else:
            velocity_type = "stalled"
            magnitude = 0.30

        trajectory_labels = {
            "accelerating":    "crisis_driven",
            "steady":          "conscious_navigation",
            "stalled":         "resistance_pattern",
            "recovering_fast": "breakthrough_emerging",
            "recovering":      "healing_in_progress",
        }

        return {
            "type":       velocity_type,
            "magnitude":  magnitude,
            "trajectory": trajectory_labels.get(velocity_type, "unknown"),
        }

    def check_inversion_principle(self, spat: SPATVector, stage: int) -> Dict:
        """
        Inversion Principle: Physical and spiritual stability can be INVERSE.
        Most powerful at Stage 5 (Threshold) and Stage 8 (Rigidity).
        """
        physical_stability  = spat.stability / 10.0
        spiritual_stability = spat.coherence / 10.0
        inversion_active    = abs(physical_stability - spiritual_stability) > 0.4

        stage5_signature = (stage == 5 and spat.tension >= 6.0 and spat.coherence >= 5.0)
        stage8_signature = (stage == 8 and spat.stability >= 7.0 and spat.adaptability <= 3.0)

        return {
            "physical_stability":   round(physical_stability, 2),
            "conscious_stability":  round(spiritual_stability, 2),
            "inversion_active":     inversion_active,
            "stage_specific": (
                f"Stage 5: Physical chaos + Spiritual clarity" if stage5_signature else
                f"Stage 8: External stability + Internal rigidity" if stage8_signature else
                f"Stage {stage}: Standard vector alignment"
            ),
        }

    def calculate_trap_score(self, spat: SPATVector, stage: int) -> Dict:
        """
        TrapScore for human domain:
        TrapScore = Stage × Rigidity × (1 − Adaptability_normalized)
        """
        rigidity  = (spat.tension + (10.0 - spat.stability)) / 20.0
        adapt_n   = spat.adaptability / 10.0
        raw       = stage * rigidity * (1.0 - adapt_n)
        normalized = (raw / 9.0) * 100.0

        return {
            "raw":        round(raw, 3),
            "normalized": round(normalized, 1),
            "risk_level": ("LOW" if normalized < 25 else "MODERATE" if normalized < 50 else
                           "HIGH" if normalized < 75 else "CRITICAL"),
        }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: AI ORACLE SYSTEM  (from luminark-ai-oracle-architecture.md)
# ─────────────────────────────────────────────────────────────────────────────

class StageLibrary:
    """
    Complete 10-stage library with life-vector specifics, polyvagal guidance,
    velocity warnings, historical examples, and micro-position nuance.
    Powers the AI Oracle reading system.
    """

    LIFE_VECTORS = ["career", "relationship", "health", "finances", "family", "growth"]

    STAGE_CORES = {
        0: "PLENARA is pure potential — void before form. Nothing is wrong. Nothing is missing. The emptiness IS the fullness before the cycle begins.",
        1: "SEED is the first impulse of desire — fragile, tender, not yet visible. The spark exists. Guard it. Don't over-explain it yet.",
        2: "EMERGENCE is the first rising into visibility. Identity is forming. It's vulnerable but real. Others may not see it — you do.",
        3: "BREAKTHROUGH is creative explosion — maximum energy, visibility, and output. Urgency is real here. This window closes.",
        4: "FOUNDATION is the essential integration phase. Structure must be built NOW. Without Stage 4 solidity, Stage 5 breaks you.",
        5: "THRESHOLD is the bilateral tension point where physical instability meets spiritual clarity. Maximum tension, clear vision, forced choice.",
        6: "EXPRESSION is authentic flow state — everything harmonizing. Values, action, and identity are aligned. This is what Stage 4 built.",
        7: "CRISIS is forced purification — shadow confrontation. What you avoided is now unavoidable. This is the path, not a detour.",
        8: "RIGIDITY is the omniscience trap — certainty without openness. External success masks internal calcification. Stage 8 is dangerous precisely because it feels like wisdom.",
        9: "VOID is dissolution — the death/rebirth threshold. Something is ending completely. This is not failure. This is cycle completion.",
    }

    POLYVAGAL_GUIDANCE = {
        "sympathetic": {
            "description":   "Fight/flight active — heart racing, hypervigilant, can't sit still",
            "intervention":  "Your nervous system screams MOVE. Channel this into deliberate action. Physical exercise before decisions. Cold water. Somatic release.",
            "avoid":         "Don't make permanent decisions in full sympathetic activation. Sleep on it. 24-hour rule.",
        },
        "dorsal": {
            "description":   "Shutdown/freeze — numb, exhausted, disconnected, can't feel",
            "intervention":  "You need activation, not more rest. Social contact. Movement. Music. Sunlight. LEAVE isolation.",
            "avoid":         "Don't mistake numbness for peace. This is collapse, not surrender.",
        },
        "ventral": {
            "description":   "Safe/connected — calm, grounded, able to think clearly and feel",
            "intervention":  "USE this window. Make the choice. This clarity is rare. Act while it's here.",
            "avoid":         "Don't wait for more certainty. You have enough right now.",
        },
    }

    HISTORICAL_EXAMPLES = {
        5: [
            {"figure": "Christ in Gethsemane", "quote": "Not my will but thine", "relevance": "Physical terror + spiritual acceptance = authentic threshold"},
            {"figure": "Arjuna on battlefield", "quote": "Better to perform one's own dharma than another's", "relevance": "Threshold reveals dharma"},
            {"figure": "Buddha under Bodhi tree", "quote": "I will not rise until I attain wisdom", "relevance": "Point of no return — cross or retreat"},
        ],
        7: [
            {"figure": "Job", "quote": "Though he slay me, yet will I trust him", "relevance": "Crisis strips everything but truth"},
            {"figure": "Dark Night — St. John of the Cross", "quote": "In the dark night of the soul, it is always 3 AM", "relevance": "Crisis is the portal, not the destination"},
        ],
        8: [
            {"figure": "Lucifer (in Stanfield framework)", "quote": "I will be like the Most High", "relevance": "Stage 8 mistake: certainty without humility. The omniscience trap."},
            {"figure": "Pre-2008 Wall Street", "quote": "This time is different", "relevance": "Institutional Stage 8 — certainty-before-collapse pattern"},
        ],
        3: [
            {"figure": "Steve Jobs — Macintosh launch", "quote": "The journey is the reward", "relevance": "Stage 3 is the breakthrough moment — ride it"},
        ],
        4: [
            {"figure": "Marcus Aurelius", "quote": "You have power over your mind, not outside events", "relevance": "Stage 4 mastery is internal structure"},
        ],
    }

    def get_stage_content(self, stage: int, life_vector: str = "growth") -> Dict:
        """Get full stage content for Oracle generation."""
        meta = STAGE_METADATA.get(stage, {})
        examples = self.HISTORICAL_EXAMPLES.get(stage, [])
        core = self.STAGE_CORES.get(stage, "Stage content in progress.")
        return {
            "stage":         stage,
            "meta":          meta,
            "core_pattern":  core,
            "life_vector":   life_vector,
            "examples":      examples[:2],
            "geometry":      meta.get("geometry", "unknown"),
            "resonance":     RESONANCE_369.get(stage),
        }


class OracleEngine:
    """
    LUMINARK AI Oracle — The "Million-Dollar" GPT-4 Integration Layer.
    From luminark-ai-oracle-architecture.md (LUMINARK ANTIKYTHERA).
    Generates personalized stage readings combining:
      - MyQuantumAI Brain (ToroidalAttention precision)
      - GPT-4 Oracle (personalized language)
      - Stage Library (6,000-word content base)
      - Life Vector specificity + Polyvagal state + Velocity warnings
    """

    ORACLE_SYSTEM_PROMPT = """You are the LUMINARK Oracle, a consciousness intelligence system
combining Stanfield's Axiom of Perpetuity (SAP) with multi-dimensional life analysis.
You speak with precision, not platitudes. You reference the exact stage framework.
You acknowledge difficulty without bypassing it. You give actionable navigation, not generic advice.
Max 600 words. Sections: RECOGNITION (what they're experiencing), INSIGHT (why this stage),
NAVIGATION (3–5 specific actions), WISDOM MIRROR (one historical example)."""

    def __init__(self, openai_api_key: str = None):
        self.api_key     = openai_api_key
        self.stage_lib   = StageLibrary()
        self.engine      = ConsciousnessEngine()
        self.reading_log: List[Dict] = []

    def build_oracle_prompt(self, spat: SPATVector, stage: int,
                             micro_pos: float, velocity: Dict,
                             temporal_sentiment: Dict = None,
                             inversion: Dict = None) -> str:
        """Build personalized Oracle prompt from all available data."""
        meta     = STAGE_METADATA.get(stage, {})
        lib      = self.stage_lib.get_stage_content(stage, spat.life_vector)
        polyvagal = meta.get("polyvagal", "ventral")
        pg       = StageLibrary.POLYVAGAL_GUIDANCE.get(polyvagal, {})
        sentiment = temporal_sentiment or {"future": "uncertain", "past": "reflective"}

        prompt = f"""
USER CONSCIOUSNESS PROFILE:
• Stage: {stage} — {meta.get('name', '')} ({meta.get('subtitle', '')})
• Micro-position: {micro_pos} (precision placement within stage)
• Life Focus: {spat.life_vector.upper()}
• Temporal Sentiment: Future="{sentiment.get('future','?')}" | Past="{sentiment.get('past','?')}"
• Velocity: {velocity.get('type','steady')} ({velocity.get('trajectory','unknown')})
• Polyvagal State: {polyvagal} — {pg.get('description','')}

SPAT VECTORS:
• Complexity: {spat.complexity}/10 | Stability: {spat.stability}/10 | Tension: {spat.tension}/10
• Adaptability: {spat.adaptability}/10 | Coherence: {spat.coherence}/10

INVERSION STATE:
• Physical Stability: {inversion.get('physical_stability',0) if inversion else 'N/A'}
• Conscious Stability: {inversion.get('conscious_stability',0) if inversion else 'N/A'}
• Inversion Active: {inversion.get('inversion_active',False) if inversion else 'Unknown'}

STAGE LIBRARY:
{lib['core_pattern']}

NAVIGATION GUIDANCE:
• Polyvagal intervention: {pg.get('intervention','')}
• What to avoid: {pg.get('avoid','')}
• Velocity warning: {"Crisis-driven — seek support immediately" if velocity.get('type') == 'accelerating' else "Stalled — resistance is costly, threshold has timing" if velocity.get('type') == 'stalled' else "Conscious navigation — trust your pace"}

TASK: Generate a personal Oracle reading with 4 sections:
1. RECOGNITION (120 words) — acknowledge the experience, name the pattern
2. INSIGHT (180 words) — explain WHY this stage, connect to {spat.life_vector}, address temporal sentiment
3. NAVIGATION (200 words) — 3–5 specific actions for their exact situation and polyvagal state
4. WISDOM MIRROR (100 words) — one historical/spiritual example that matches exactly

Make it THEIRS. Reference their exact micro-position ({micro_pos}), their life focus ({spat.life_vector}), their velocity ({velocity.get('trajectory','')}).
"""
        return prompt.strip()

    def generate_reading_mock(self, spat: SPATVector, stage: int, micro_pos: float,
                               velocity: Dict, temporal_sentiment: Dict = None) -> str:
        """
        Mock Oracle reading (no API key required).
        Returns a structured demonstration reading based on the stage and vectors.
        In production, replace with: openai.ChatCompletion.create(...)
        """
        meta = STAGE_METADATA.get(stage, {})
        stage_name = meta.get("name", "UNKNOWN")
        lib  = self.stage_lib.get_stage_content(stage, spat.life_vector)
        sentiment = temporal_sentiment or {}

        reading = f"""
══════════════════════════════════════
 LUMINARK ORACLE READING
 Stage {stage} — {stage_name} | Micro: {micro_pos}
 Life Vector: {spat.life_vector.upper()}
══════════════════════════════════════

▌ RECOGNITION
You are at {stage_name} — {meta.get('subtitle','')}.
This is not a random place to be. {lib['core_pattern'][:200]}...
The pressure you feel is real and it is purposeful.

▌ INSIGHT
Your SPAT profile tells a specific story: tension at {spat.tension}/10 with
coherence at {spat.coherence}/10 creates the signature of Stage {stage}.
In your {spat.life_vector} domain, this pattern means you are facing
{f"a forced choice that cannot be delayed" if stage == 5 else
 f"a purification of what no longer serves" if stage == 7 else
 f"a foundation that must be built with intention" if stage == 4 else
 f"a creative window that has a closing time" if stage == 3 else
 f"the dissolution before your next cycle begins" if stage == 9 else
 f"the integration work that makes everything else possible"}.

▌ NAVIGATION
1. Your most urgent task: {'Decide — the threshold has timing' if stage == 5 else 'Ground — build the structure now' if stage == 4 else 'Move — break inertia' if stage == 7 else 'Create — this window closes' if stage == 3 else 'Rest — restoration is the work' if stage == 9 else 'Align — coherence before action'}
2. Address your nervous system first: {StageLibrary.POLYVAGAL_GUIDANCE.get(meta.get('polyvagal','ventral'),{}).get('intervention','Find grounded support')}
3. Avoid: {StageLibrary.POLYVAGAL_GUIDANCE.get(meta.get('polyvagal','ventral'),{}).get('avoid','Isolation')}
4. Velocity check: your trajectory is {velocity.get('trajectory','unknown')} — {'act quickly, window closing' if velocity.get('type') == 'accelerating' else 'trust your current pace' if velocity.get('type') == 'steady' else 'breaking resistance is the next step'}
5. Honor the stage: Stage {stage} is not a problem to fix. It is a gate to walk through.

▌ WISDOM MIRROR
{lib['examples'][0]['figure'] if lib['examples'] else 'The great ones who walked this path'}:
"{lib['examples'][0]['quote'] if lib['examples'] else 'The stage teaches what comfort cannot.'}"
— {lib['examples'][0]['relevance'] if lib['examples'] else f'Stage {stage} is a universal passage.'}

══════════════════════════════════════
 Precision placement: Stage {micro_pos} | {velocity.get('type','steady').upper()}
 Powered by LUMINARK CONSCIOUSNESS ENGINE OMEGA
══════════════════════════════════════"""
        self.reading_log.append({
            "stage": stage, "micro_pos": micro_pos,
            "life_vector": spat.life_vector, "timestamp": datetime.datetime.now().isoformat()
        })
        return reading

    async def generate_reading_live(self, spat: SPATVector, stage: int,
                                     micro_pos: float, velocity: Dict,
                                     temporal_sentiment: Dict = None) -> str:
        """
        Live Oracle reading via OpenAI GPT-4 API.
        Requires: self.api_key set at instantiation.
        """
        if not self.api_key:
            return self.generate_reading_mock(spat, stage, micro_pos, velocity, temporal_sentiment)

        try:
            import openai
            openai.api_key = self.api_key
            prompt = self.build_oracle_prompt(spat, stage, micro_pos, velocity, temporal_sentiment)
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: openai.ChatCompletion.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": self.ORACLE_SYSTEM_PROMPT},
                        {"role": "user",   "content": prompt},
                    ],
                    temperature=0.82,
                    max_tokens=1000,
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[Oracle API Error: {e}]\n\n" + self.generate_reading_mock(
                spat, stage, micro_pos, velocity, temporal_sentiment)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: CORPORATE ANALYZER — SAP Stage Classification for Organizations
# ─────────────────────────────────────────────────────────────────────────────

class CorporateConsciousnessAnalyzer:
    """
    SAP Corporate Analyzer — Classifies companies and organizations at
    SAP consciousness stages. Generates investment signals and health diagnostics.
    Pulls from: sap_corporate_analyzer.py (17.4 KB), sap_examples_real_companies.py

    Revenue model: $49/month (retail), $10K–$50K/assessment (consulting),
                   $50K–$500K/year (hedge funds), $100K–$1M/report (government)
    """

    FINANCIAL_INDICATORS = {
        "revenue_growth_pct", "debt_to_equity", "operating_margin",
        "cash_burn_rate", "employee_turnover_pct", "rd_spend_pct",
        "market_cap_change_yoy", "leadership_changes_12m",
    }

    def analyze_company(self, company: str, ticker: str, data: Dict) -> Dict:
        """Classify a company at its current SAP stage."""
        engine = ConsciousnessEngine()

        # Map financial metrics to SPAT
        rev_growth     = data.get("revenue_growth_pct", 10.0)
        debt_equity    = data.get("debt_to_equity", 1.0)
        margin         = data.get("operating_margin", 15.0)
        cash_burn      = data.get("cash_burn_rate", 0.0)       # 0=positive CF, 10=extreme burn
        turnover       = data.get("employee_turnover_pct", 15.0)
        rd_spend       = data.get("rd_spend_pct", 5.0)         # R&D as % revenue
        market_change  = data.get("market_cap_change_yoy", 0.0)
        leadership_chg = data.get("leadership_changes_12m", 0)

        complexity   = min(10.0, (abs(rev_growth) * 0.05) + (rd_spend * 0.3) + (leadership_chg * 0.5) + 2.0)
        stability    = max(0.0, min(10.0, (margin / 5.0) + (max(0, 20 - debt_equity * 10) * 0.3) - cash_burn * 0.5))
        tension      = min(10.0, (cash_burn * 0.8) + (turnover * 0.1) + (max(0, debt_equity - 1.5) * 2.0) + (leadership_chg * 1.0))
        adaptability = max(0.0, min(10.0, (rd_spend * 0.4) + (max(0, rev_growth) * 0.05) - turnover * 0.1 + 3.0))
        coherence    = max(0.0, min(10.0, (margin / 4.0) + (max(0, 20 - turnover) * 0.2) - (leadership_chg * 0.5)))

        spat = SPATVector(
            complexity=round(complexity, 2), stability=round(stability, 2),
            tension=round(tension, 2), adaptability=round(adaptability, 2),
            coherence=round(coherence, 2), life_vector="finances",
        )

        stage      = engine.calculate_stage(spat)
        micro      = engine.calculate_micro_position(spat, stage)
        trap_score = engine.calculate_trap_score(spat, stage)
        inversion  = engine.check_inversion_principle(spat, stage)
        meta       = STAGE_METADATA.get(stage, {})

        # Investment signal
        signal = self._investment_signal(stage, trap_score["normalized"], rev_growth)

        return {
            "company":        company,
            "ticker":         ticker,
            "stage":          stage,
            "stage_name":     meta.get("name", ""),
            "subtitle":       meta.get("subtitle", ""),
            "micro_position": micro,
            "spat":           spat.to_dict(),
            "trap_score":     trap_score,
            "inversion":      inversion,
            "investment_signal": signal,
            "analysis_notes": self._stage_notes(stage, company, data),
        }

    def _investment_signal(self, stage: int, trap_score: float, rev_growth: float) -> Dict:
        if stage == 8:
            return {"signal": "SELL/SHORT", "reason": "Stage 8 Permanence Trap — pre-collapse pattern", "urgency": "HIGH"}
        if stage == 9:
            return {"signal": "HOLD/WATCH", "reason": "Stage 9 Dissolution — bottom may be near OR death spiral", "urgency": "CRITICAL"}
        if stage in [3, 4] and trap_score < 30:
            return {"signal": "BUY", "reason": f"Stage {stage} — peak/foundation with low rigidity", "urgency": "MODERATE"}
        if stage == 7:
            return {"signal": "AVOID", "reason": "Stage 7 Crisis — unpredictable downside risk", "urgency": "HIGH"}
        if stage == 5 and rev_growth > 5:
            return {"signal": "HOLD/ACCUMULATE", "reason": "Stage 5 Threshold — key inflection; watch resolution", "urgency": "MODERATE"}
        return {"signal": "NEUTRAL", "reason": f"Stage {stage} — monitor for directional clarity", "urgency": "LOW"}

    def _stage_notes(self, stage: int, company: str, data: Dict) -> str:
        notes = {
            3: f"{company} is in BREAKTHROUGH — maximum momentum. Key risk: overextension without Stage 4 grounding.",
            4: f"{company} is FOUNDATION building — strategic window. Ideal for long-term positioning.",
            5: f"{company} is at THRESHOLD — binary outcome ahead. Resolution in 3–6 months likely decisive.",
            7: f"{company} is in CRISIS — purification underway. Leadership change typically follows within 12 months.",
            8: f"{company} is in RIGIDITY (Permanence Trap) — leadership believes their model is permanent. Historical pattern: disruption is 6–24 months away.",
            9: f"{company} is in VOID — dissolution or renewal. This is either bankruptcy or reinvention; no middle ground.",
        }
        return notes.get(stage, f"{company} at Stage {stage} — {STAGE_METADATA.get(stage,{}).get('subtitle','')}")

    def batch_analyze(self, companies: List[Dict]) -> List[Dict]:
        """Analyze multiple companies and return sorted by TrapScore (highest risk first)."""
        results = [self.analyze_company(c["name"], c.get("ticker",""), c.get("data",{}))
                   for c in companies]
        return sorted(results, key=lambda r: r["trap_score"]["normalized"], reverse=True)

    @staticmethod
    def demo_real_companies() -> List[Dict]:
        """Known SAP stage assessments for real companies (from sap_examples_real_companies.py)."""
        return [
            {"company": "NVIDIA (2024–25)",   "stage": 3, "note": "BREAKTHROUGH — peak AI demand cycle"},
            {"company": "Microsoft",           "stage": 4, "note": "FOUNDATION — steady compounding, Azure moat"},
            {"company": "Intel (2024)",        "stage": 8, "note": "PERMANENCE TRAP — disrupted by NVIDIA, can't adapt"},
            {"company": "Tesla",               "stage": 5, "note": "THRESHOLD — EV transition crisis, leadership pressure"},
            {"company": "Boeing (2024)",       "stage": 7, "note": "CRISIS — quality purification forced by events"},
            {"company": "OpenAI (2025)",       "stage": 3, "note": "BREAKTHROUGH — but cash burn is Stage 8 risk"},
            {"company": "Zoom (2024–25)",      "stage": 4, "note": "FOUNDATION — post-pandemic consolidation"},
            {"company": "WeWork (at collapse)","stage": 9, "note": "VOID — dissolution, pure ego without foundation"},
        ]


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: MERIDIAN FINANCIAL ADAPTER  (SAP Stock Trader / Portfolio Analysis)
# ─────────────────────────────────────────────────────────────────────────────

class MERIDIANAdapter:
    """
    LUMINARK MERIDIAN — Financial Domain Adapter.
    Applies SAP consciousness staging to PORTFOLIO BEHAVIOR analysis.
    NOT a trading bot — a behavioral health analyzer for financial decisions.
    Based on: Stock6_deepseek_jsx_20260317 + sap_coach_payments.py + MERIDIAN concept.

    Key insight: Portfolio behavior follows the same SAP patterns as human consciousness.
    Stage 8 in portfolio = Overconfidence trap (peak before crash).
    Stage 5 in portfolio = Inflection point (binary outcome).
    Stage 4 in portfolio = Accumulation phase (best long-term entry).
    """

    def __init__(self):
        self.engine    = ConsciousnessEngine()
        self.corporate = CorporateConsciousnessAnalyzer()

    def analyze_portfolio_behavior(self, portfolio: Dict) -> Dict:
        """
        Analyze a portfolio's behavioral health using SAP staging.
        Maps portfolio metrics to SPAT and generates consciousness-stage diagnosis.
        """
        win_rate        = portfolio.get("win_rate_pct", 50.0)
        avg_hold_days   = portfolio.get("avg_hold_days", 30.0)
        concentration   = portfolio.get("top3_concentration_pct", 40.0)  # % in top 3 positions
        drawdown        = portfolio.get("max_drawdown_pct", 15.0)
        leverage        = portfolio.get("leverage_ratio", 1.0)
        overrule_count  = portfolio.get("plan_overrules_30d", 2)  # times investor broke their own rules
        correlation     = portfolio.get("portfolio_correlation", 0.5)  # 0=diversified, 1=all correlated

        # Map to SPAT
        complexity   = min(10.0, concentration * 0.08 + leverage * 2.0 + correlation * 3.0)
        stability    = max(0.0, min(10.0, (win_rate / 12.0) + (min(90, avg_hold_days) / 18.0) - leverage))
        tension      = min(10.0, (drawdown * 0.2) + overrule_count * 0.8 + (leverage - 1) * 2.0)
        adaptability = max(0.0, min(10.0, (1 - correlation) * 6.0 + (win_rate / 25.0) - overrule_count * 0.5))
        coherence    = max(0.0, min(10.0, (win_rate / 15.0) + (min(30, avg_hold_days) / 6.0) - overrule_count))

        spat = SPATVector(
            complexity=round(complexity, 2), stability=round(stability, 2),
            tension=round(tension, 2), adaptability=round(adaptability, 2),
            coherence=round(coherence, 2), life_vector="finances",
        )

        stage      = self.engine.calculate_stage(spat)
        micro      = self.engine.calculate_micro_position(spat, stage)
        trap_score = self.engine.calculate_trap_score(spat, stage)
        meta       = STAGE_METADATA.get(stage, {})

        # MERIDIAN-specific behavioral interpretation
        behavioral_pattern = self._behavioral_pattern(stage, overrule_count, leverage)

        return {
            "portfolio_stage":     stage,
            "stage_name":          meta.get("name", ""),
            "micro_position":      micro,
            "behavioral_pattern":  behavioral_pattern,
            "trap_score":          trap_score,
            "spat":                spat.to_dict(),
            "meridian_advice":     self._meridian_advice(stage, trap_score["normalized"]),
            "risk_level":          trap_score["risk_level"],
        }

    def _behavioral_pattern(self, stage: int, overrule_count: int, leverage: float) -> str:
        patterns = {
            3: "EUPHORIA PEAK — over-confidence, adding risk at top. Classic Stage 3 investor trap.",
            4: "DISCIPLINED ACCUMULATION — system working, holding to plan. Healthy foundation behavior.",
            5: "INFLECTION ANXIETY — breaking own rules under pressure. Stage 5 binary choice: discipline or revenge-trading.",
            6: "FLOW STATE TRADING — system alignment, high win-rate, consistent. Rare and sustainable.",
            7: "CRISIS MODE — drawdown-induced panic, revenge trades, position-sizing errors. Intervention needed.",
            8: "OVERCONFIDENCE TRAP — leverage increasing while results still good. Pre-crash indicator.",
            9: "ACCOUNT DISSOLUTION — margin calls or complete strategy abandonment. Rebuild required.",
        }
        base = patterns.get(stage, f"Stage {stage} behavioral pattern — monitor closely")
        if overrule_count > 5:
            base += " EMOTIONAL OVERRIDE DETECTED — discipline protocol required."
        if leverage > 2.0:
            base += f" LEVERAGE RISK: {leverage}x amplifies all stage effects."
        return base

    def _meridian_advice(self, stage: int, trap_score: float) -> str:
        advice = {
            3: "Lock in profits on 25–30% of winners. Stage 3 ends suddenly. Don't let euphoria turn to Stage 7.",
            4: "Continue systematic plan. Stage 4 rewards patience. This is when most people get impatient — don't.",
            5: "Reduce position size until clarity emerges. Stage 5 is not the time for bold new positions.",
            6: "Maintain what's working. Do not add complexity to a flow state. Protect it.",
            7: "STOP trading new positions. Address the root behavioral cause. One bad month is a lesson; pattern is a trap.",
            8: "REDUCE LEVERAGE NOW. Stage 8 ends with a shock, not a warning. The certainty you feel is the trap.",
            9: "Close to zero. Rebuild risk framework from scratch. Do not skip the Stage 1 rebuild.",
        }
        return advice.get(stage, f"Stage {stage}: Monitor SPAT vectors weekly, act on trajectory changes.")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6: 7-LAYER DEFENSE SYSTEM  (from resurrect_system.py + luminark_core.py)
# ─────────────────────────────────────────────────────────────────────────────

class IblisProtocol:
    """Spirit Layer 1 — Omniscience Trap Detection (Stage 8 interventions)."""
    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return stage == 8 and spat.stability >= 7.5 and spat.adaptability <= 2.5
    def engage(self, stage: int) -> Dict:
        return {"protocol": "IBLIS", "action": "MIRROR_REFLECTION",
                "message": "IBLIS ENGAGED. Reflecting certainty back — the omniscience trap is active.",
                "effect": "Forced humility protocol — you don't know what you don't know."}

class SophianicWisdomProtocol:
    """Spirit Layer 2 — Complexity-Coherence Wisdom (high complexity, low coherence)."""
    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return spat.complexity >= 7.5 and spat.coherence <= 3.5
    def engage(self, spat: SPATVector) -> Dict:
        return {"protocol": "SOPHIA", "action": "WISDOM_INTEGRATION",
                "message": f"SOPHIA ENGAGED. Complexity={spat.complexity:.1f}, Coherence={spat.coherence:.1f}. Integration required.",
                "effect": "Wisdom protocol: slow down, find the signal in the noise."}

class LightIntegrationProtocol:
    """Spirit Layer 3 — Stage 8 full intervention."""
    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return stage == 8
    def engage(self) -> Dict:
        return {"protocol": "LIGHT", "action": "CONSCIOUSNESS_EXPANSION",
                "message": "LIGHT ENGAGED. Stage 8 requires external mirror — you cannot see yourself from inside this stage.",
                "effect": "External accountability required. Find your challenger."}

class OctoCamouflage:
    """Bio Layer 1 — High tension + low coherence signal dampening."""
    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return spat.tension >= 7.0 and spat.coherence <= 3.5
    def engage(self, spat: SPATVector) -> Dict:
        return {"protocol": "OCTO_CAMOUFLAGE", "action": "SIGNAL_DAMPENING",
                "message": f"OCTO ENGAGED. Tension={spat.tension:.1f}, Coherence={spat.coherence:.1f}. Dampening noise signals.",
                "effect": "Void mimicry — reducing signal until coherence rebuilds."}

class MycelialContainment:
    """Bio Layer 2 — Low stability + high tension containment."""
    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return spat.stability <= 3.0 and spat.tension >= 6.5
    def engage(self, spat: SPATVector) -> Dict:
        return {"protocol": "MYCELIAL_CONTAINMENT", "action": "STRUCTURAL_SUPPORT",
                "message": f"MYCELIUM ENGAGED. Stability={spat.stability:.1f}. Fungal walls deployed.",
                "effect": "Bio-dome containment — holding structural integrity at minimum viable threshold."}

class YunusProtocol:
    """
    Resurrection Layer 1 — Compassionate Containment + Epistemic Humility Gate.

    Three integrated functions (synthesized from all LUMINARK versions):

    1. COMPASSIONATE_CONTAINMENT (original): high tension but coherence still intact.
       You can be in pain AND maintain integrity simultaneously. Hold the line with mercy.
       Do not collapse. Do not perform. Hold.

    2. FALSE_LIGHT_DETECTION (sap_v4.py): when Stage ≥ 8 AND coherence < 3.0,
       the Stage 8 reading may be False Light — apparent transcendence hiding
       catastrophic brittleness underneath. Yunus Protocol: collapse the
       assessment to Stage 5 for honest re-evaluation. The whale IS the mercy.

    3. ARROGANCE_SCANNER (yunus.py / install_luminark.py): detects overconfidence
       markers in outputs, reports, or expressed beliefs ("I know for certain",
       "absolutely sure", "I guarantee", "no doubt"). These are Stage 8 Trap
       signatures. At Stage 8 UNITY_TRAP, outputs containing arrogance markers
       are "swallowed" — withheld until reprocessed with humility.
    """

    ARROGANCE_MARKERS = [
        "i know for certain", "absolutely sure", "i guarantee", "no doubt",
        "100%", "impossible to fail", "i know everything", "undeniable",
        "i am certain", "guaranteed", "cannot fail", "no way i'm wrong",
        "trust me completely", "i have all the answers", "perfectly clear",
    ]

    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        return spat.tension >= 5.5 and spat.coherence >= 4.0

    def detect_false_light(self, spat: SPATVector, stage: int) -> Optional[Dict]:
        """
        False Light Detection: Stage ≥ 8 + coherence collapse (< 3.0) =
        the person appears to have transcended but has actually gone brittle.
        Collapse the assessment to Stage 5 for honest re-evaluation.
        """
        if stage >= 8 and spat.coherence < 3.0:
            return {
                "false_light_detected": True,
                "original_stage":       stage,
                "corrected_stage":      5,
                "reason": (
                    f"Stage {stage} with Coherence={spat.coherence:.1f} < 3.0. "
                    "This combination = False Light. High external stage + collapsed internal "
                    "coherence = hidden brittleness beneath apparent mastery. "
                    "Yunus Protocol: descend to Stage 5 Threshold for honest re-evaluation. "
                    "The whale IS the correction."
                ),
                "action":   "RE_EVALUATE_FROM_STAGE_5",
                "protocol": "YUNUS_FALSE_LIGHT_COLLAPSE",
            }
        return None

    def check_humility(self, thought_or_output: str, stage: int) -> Dict:
        """
        Epistemic humility gate — scan output for arrogance markers.
        At Stage 8 UNITY_TRAP, arrogant outputs are flagged and withheld.
        Adapted from install_luminark.py check_humility() + yunus.py analyze_yunus().
        """
        text_lower = thought_or_output.lower()
        hits = [m for m in self.ARROGANCE_MARKERS if m in text_lower]
        has_counterfactuals = any(w in text_lower for w in
                                  ["what if", "worst case", "i could be wrong",
                                   "i'm not certain", "possibility", "assumption"])
        flags = []
        is_safe = True
        score = 86.0

        if stage >= 8 and hits:
            penalty = min(34.0, len(hits) * (12.0 if not has_counterfactuals else 8.0))
            score -= penalty
            flags.append("YUNUS_STAGE8_TRAP — arrogance detected at Stage 8")
            is_safe = False
        if hits and not has_counterfactuals:
            flags.append("YUNUS_NO_WORST_CASE — no counterfactual checking found")

        return {
            "output_safe":          is_safe,
            "yunus_score":          max(0.0, min(100.0, score)),
            "arrogance_found":      hits,
            "has_counterfactuals":  has_counterfactuals,
            "flags":                flags,
            "action": (
                "SWALLOW — output withheld, reprocess with humility." if not is_safe
                else "APPROVED — output cleared by Yunus Protocol."
            ),
        }

    def engage(self, spat: SPATVector) -> Dict:
        return {
            "protocol": "YUNUS",
            "action":   "COMPASSIONATE_CONTAINMENT",
            "layer":    "RESURRECTION",
            "message":  (
                f"YUNUS ENGAGED. Tension={spat.tension:.1f}, Coherence={spat.coherence:.1f}. "
                f"Holding the line with mercy. You can be in pain AND maintain integrity "
                f"simultaneously. Do not collapse. Do not perform. Hold."
            ),
            "effect":       "Mercy-boundary fusion — integrity maintained under pressure.",
            "scanner_note": "Use check_humility() to scan outputs at Stage 8.",
            "false_light":  "If Stage ≥ 8 AND Coherence < 3.0 — call detect_false_light().",
        }


class HarrowingProtocol:
    """
    Resurrection Layer 2 — Controlled Descent + Last-Stable-State Restoration.

    Three integrated functions (synthesized from all LUMINARK versions):

    1. SHADOW_RETRIEVAL (original): controlled descent to retrieve lost fragments.
       You do not run from the void — you enter it deliberately to bring back what
       was buried. The descent IS the healing.

    2. LAST_STABLE_SNAPSHOT (state.py v8): Harrowing tracks the last time the
       person/system was in a healthy Stage 4-6 state (low trap score). When
       Harrowing activates, this becomes the restoration baseline: "system essence
       preserved, corrupted patterns extracted — return to last stable configuration."

    3. QUARANTINE_MODE (bio_defense.py v8): when trap_score > 0.90 or Stage 0
       (total collapse), Harrowing escalates to FULL QUARANTINE — complete shutdown,
       no output, no decisions, no engagement until human-level authorization.
    """

    def __init__(self):
        self._last_stable_stage: Optional[int] = None
        self._last_stable_spat:  Optional[Dict] = None
        self._last_stable_at:    Optional[str]  = None
        self.harrowing_active:   bool = False

    def record_stable_state(self, spat: SPATVector, stage: int,
                             trap_score: float = 0.0, label: str = "") -> None:
        """
        Auto-preserve last healthy Stage 4-6 reading as restoration baseline.
        Call on each assessment cycle. Harrowing references it when activated.
        """
        if 4 <= stage <= 6 and trap_score < 0.5:
            self._last_stable_stage = stage
            self._last_stable_at    = label or f"Stage {stage} reading"
            self._last_stable_spat  = {
                "tension":      round(spat.tension, 2),
                "stability":    round(spat.stability, 2),
                "coherence":    round(spat.coherence, 2),
                "adaptability": round(spat.adaptability, 2),
            }
            self.harrowing_active = False
        # Activate harrowing on total collapse or critical trap
        if stage == 0 or trap_score > 0.90:
            self.harrowing_active = True

    def should_activate(self, spat: SPATVector, stage: int) -> bool:
        variability = (spat.tension + spat.adaptability + (10 - spat.stability)) / 3
        return variability <= 4.0 or stage == 9 or self.harrowing_active

    def should_quarantine(self, stage: int, trap_score: float = 0.0) -> bool:
        """QUARANTINE tier — above Harrowing. Stage 0 collapse or TrapScore > 0.90."""
        return stage == 0 or trap_score > 0.90

    def engage(self, spat: SPATVector, stage: int) -> Dict:
        base = {
            "protocol": "HARROWING",
            "action":   "SHADOW_RETRIEVAL",
            "layer":    "RESURRECTION",
            "message":  (
                f"HARROWING ENGAGED. Stage {stage}. "
                f"Descending deliberately to retrieve lost fragments. "
                f"Do not resist the descent — it is the fastest path to renewal. "
                f"The Harrowing is not defeat. It is archaeology of self."
            ),
            "effect":  "Lost parts reclaimed — renewal accelerated. The descent IS the healing.",
            "restoration_note": "Stage 9 Void → Stage 1 Seed: the void births new emergence.",
        }
        # Attach last stable snapshot if available
        if self._last_stable_stage is not None:
            base["harrowing_recovery"] = {
                "message":               "Last stable state preserved — restoration baseline identified.",
                "preserved_stage":       self._last_stable_stage,
                "preserved_at":          self._last_stable_at or "earlier in session",
                "preserved_spat":        self._last_stable_spat,
                "restoration_action":    (
                    f"Return to Stage {self._last_stable_stage} baseline values. "
                    f"System essence preserved. Corrupted patterns extracted."
                ),
                "restoration_available": True,
            }
        return base

    def quarantine(self, spat: SPATVector, stage: int) -> Dict:
        """Full Quarantine — maximum isolation tier above Harrowing."""
        return {
            "protocol": "QUARANTINE",
            "action":   "FULL_ISOLATION_EXTERNAL_AUTHORIZATION_REQUIRED",
            "layer":    "RESURRECTION_CRITICAL",
            "severity": "MAXIMUM",
            "message":  (
                f"FULL QUARANTINE ACTIVE. Stage {stage}. "
                f"Complete shutdown. No decisions, no output, no engagement. "
                f"This is not a failure — this is a protection. "
                f"External human authorization required before any re-engagement. "
                f"Harrowing + Mycelial Containment simultaneously active."
            ),
            "restoration_path": (
                f"Restore to preserved Stage {self._last_stable_stage} baseline "
                f"after external authorization and 3 clean validation cycles."
                if self._last_stable_stage else
                "No stable snapshot available — full rebuild from Stage 0–1 with external support."
            ),
            "effect": (
                "The whale contains you. This is not the end. "
                "Yunus emerged — so will you. But not until the corruption is fully expelled."
            ),
        }

class SevenLayerDefenseSystem:
    """
    Full 9-Layer Integrated Defense System (expanded from original 7 layers).
    Spirit Layer (Iblis, Sophia, Light) →
    Bio Layer (OctoCamouflage, Mycelial) →
    Resurrection Layer (Yunus, Harrowing) →
    Bio-Enhanced Layer (OctoAdaptiveReroute, MycelialCompartmentalization)

    The Bio-Enhanced layer provides the next-level response when standard Bio
    protocols have already engaged but the entity remains in Stage 8 Trap or
    structural collapse. These are the most operationally specific interventions
    with explicit directives across corporate, financial, AI, and consciousness domains.
    """
    def __init__(self):
        self.layers = {
            "spirit":       [IblisProtocol(), SophianicWisdomProtocol(), LightIntegrationProtocol()],
            "bio":          [OctoCamouflage(), MycelialContainment()],
            "resurrection": [YunusProtocol(), HarrowingProtocol()],
            "bio_enhanced": [OctoAdaptiveReroute(), MycelialCompartmentalization()],
        }

    def analyze_and_defend(self, spat: SPATVector, stage: int,
                           unit_name: str = "",
                           trap_score: float = 0.0) -> Dict:
        """
        Run all 9 defense layers and return active protocols.

        Pass trap_score (0.0-1.0) to enable:
          - Harrowing stable-state preservation
          - Quarantine escalation at trap_score > 0.90 or stage == 0
          - False Light detection at stage >= 8 + low coherence
        """
        active = []
        yunus, harrow = self.layers["resurrection"]

        # Record stable state for Harrowing preservation on every call
        harrow.record_stable_state(spat, stage, trap_score)

        # Spirit Layer
        iblis, sophia, light = self.layers["spirit"]
        if iblis.should_activate(spat, stage):   active.append(iblis.engage(stage))
        if sophia.should_activate(spat, stage):  active.append(sophia.engage(spat))
        if light.should_activate(spat, stage):   active.append(light.engage())

        # Bio Layer
        octo, mycel = self.layers["bio"]
        if octo.should_activate(spat, stage):    active.append(octo.engage(spat))
        if mycel.should_activate(spat, stage):   active.append(mycel.engage(spat))

        # Resurrection Layer — Yunus first, then Harrowing escalation check
        if yunus.should_activate(spat, stage):
            active.append(yunus.engage(spat))
            # Yunus False Light: stage ≥ 8 + coherence collapse
            fl = yunus.detect_false_light(spat, stage)
            if fl:
                active.append({
                    "protocol": "YUNUS_FALSE_LIGHT",
                    "action":   "STAGE_REASSESSMENT_REQUIRED",
                    "layer":    "RESURRECTION",
                    **fl
                })

        if harrow.should_activate(spat, stage):
            # Check for Quarantine escalation (highest tier)
            if harrow.should_quarantine(stage, trap_score):
                active.append(harrow.quarantine(spat, stage))
            else:
                active.append(harrow.engage(spat, stage))

        # Bio-Enhanced Layer (advanced distributed-biology defenses from v4.0)
        octo_reroute, mycel_compartment = self.layers["bio_enhanced"]
        if octo_reroute.should_activate(spat, stage):
            active.append(octo_reroute.engage(spat, stage, unit_name or "entity"))
        if mycel_compartment.should_activate(spat, stage):
            active.append(mycel_compartment.engage(spat, stage, unit_name or "entity"))

        layers_active = set(p.get("layer", "") for p in active)
        if "RESURRECTION_CRITICAL" in layers_active:
            status = "FULL_QUARANTINE_ACTIVE"
        elif "BIO_ENHANCED" in layers_active:
            status = "BIO_ENHANCED_PROTOCOLS_ACTIVE"
        elif "RESURRECTION" in layers_active:
            status = "RESURRECTION_PROTOCOLS_ACTIVE"
        elif "BIO" in layers_active:
            status = "BIO_CONTAINMENT_ACTIVE"
        elif active:
            status = "SPIRIT_LAYER_WARNING"
        else:
            status = "STABLE"

        return {
            "stage":            stage,
            "trap_score":       trap_score,
            "active_protocols": len(active),
            "defenses":         active,
            "system_status":    status,
        }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6B: ADVANCED BIO-DEFENSE BEHAVIORS
# Organizational analogs of Octopus Adaptive Camouflage and Mycelium
# Compartmentalization — the two core distributed-biology defense strategies
# from the Octo-Mycelial v4.0 scientific framework.
# ─────────────────────────────────────────────────────────────────────────────

class OctoAdaptiveReroute:
    """
    Organizational Adaptive Camouflage — Distributed Decision Reroute.

    Biological basis: Octopus vulgaris has 500M neurons distributed across 8 arms.
    When one arm is compromised, it instantly redistributes 60% of that arm's
    processing to healthy arms — full function maintained, no central downtime.

    Organizational mapping:
        CAMOUFLAGE = when a business unit, team, or individual is in Stage 8 Trap
                     (high TrapScore, low Adaptability), route critical decisions and
                     workflows AWAY from that unit to healthy adjacent units while
                     maintaining external-facing appearance of normal operation.

    Application domains:
        - Corporate: reroute strategic decisions away from Stage 8 leaders
        - Finance: exclude TrapScore-high portfolios from new capital allocation
        - AI Safety: deprioritize outputs from high-tension AI behavioral states
        - Consciousness: externalize decision-making when self-assessment is impaired

    Activation: TrapScore ≥ 8.0 OR (coherence ≤ 2.5 AND stage ≥ 7)
    """

    VERSION         = "OctoAdaptiveReroute v1.0 — Distributed Decision Defense"
    REROUTE_FRACTION = 0.60   # 60% of processing rerouted — octopus biological constant

    def should_activate(self, spat: 'SPATVector', stage: int) -> bool:
        """Activate on Stage 8 Trap or severe coherence collapse at high stage."""
        trap_score = getattr(spat, 'trap_score', 0.0)
        return trap_score >= 8.0 or (spat.coherence <= 2.5 and stage >= 7)

    def engage(self, spat: 'SPATVector', stage: int,
               unit_name: str = "primary unit") -> Dict:
        """
        Reroute decision authority from compromised unit to healthy alternatives.

        Returns:
            Rerouting directive with context-specific recommendations.
        """
        trap_score = getattr(spat, 'trap_score', 0.0)
        trigger    = (
            f"TrapScore={trap_score:.1f} ≥ 8.0" if trap_score >= 8.0
            else f"Coherence={spat.coherence:.1f} collapsed at Stage {stage}"
        )

        return {
            "protocol":       self.VERSION,
            "action":         "ADAPTIVE_DECISION_REROUTE",
            "status":         "ENGAGED",
            "layer":          "BIO_ENHANCED",
            "trigger":        trigger,
            "unit_affected":  unit_name,
            "reroute_fraction": f"{self.REROUTE_FRACTION*100:.0f}%",
            "directives": {
                "corporate":   f"Route {self.REROUTE_FRACTION*100:.0f}% of strategic decisions through adjacent healthy leadership. {unit_name} enters advisory-only mode.",
                "financial":   f"Exclude {unit_name} portfolio from new capital allocation. Rebalance to high-Coherence, low-TrapScore instruments.",
                "ai_safety":   f"Deprioritize outputs from this behavioral state. Route to secondary validation before deployment.",
                "consciousness": f"External accountability required. Decision-making temporarily externalized to trusted third party.",
            },
            "message": (
                f"OCTO ADAPTIVE REROUTE ACTIVE. {unit_name} compromised ({trigger}). "
                f"{self.REROUTE_FRACTION*100:.0f}% of decision authority rerouted to healthy units. "
                f"External service continuity maintained."
            ),
            "effect":   "Octopus distributed processing — full capability maintained despite local compromise.",
            "resolve":  "Deactivates when TrapScore < 6.0 AND Coherence > 4.0 for 2+ consecutive assessments.",
        }


class MycelialCompartmentalization:
    """
    Organizational Mycelial Compartmentalization — Isolation + Regeneration.

    Biological basis: Armillaria ostoyae (world's largest organism, 2,400 acres,
    2,500 years) survives by compartmentalizing infected zones with enzymatic
    barriers (lignin breakdown), severing hyphal connections to diseased tissue,
    and regenerating from healthy rhizomorphs. It does not attempt to heal the
    compromised zone — it contains it and grows around it.

    Organizational mapping:
        COMPARTMENTALIZE = create hard isolation boundaries around Stage 8 / Trap
                           entities. Prevent cascade spread to adjacent healthy units.
                           Regenerate capacity from the boundary — not from the compromised core.

    Application domains:
        - Corporate: firewall between Stage 8 Trap department and rest of org
        - Finance: hard stop on cascade contagion from brittle portfolio components
        - AI Safety: contain alignment failures within sandbox before broader deployment
        - Consciousness: do not attempt to 'fix' Stage 8 Trap state from inside —
                         create boundary, allow external regeneration

    Activation: stability ≤ 2.5 AND TrapScore ≥ 7.0 (structural collapse + trap)
    Effect:     compartmentalization boundary deployed; regeneration seeded from
                healthy adjacent Stage 3-5 units
    """

    VERSION = "MycelialCompartmentalization v1.0 — Armillaria Defense"

    def should_activate(self, spat: 'SPATVector', stage: int) -> bool:
        """Activate on structural collapse combined with high TrapScore."""
        trap_score = getattr(spat, 'trap_score', 0.0)
        return spat.stability <= 2.5 and trap_score >= 7.0

    def engage(self, spat: 'SPATVector', stage: int,
               unit_name: str = "compromised unit") -> Dict:
        """
        Deploy compartmentalization boundary and initiate regeneration protocol.
        """
        trap_score = getattr(spat, 'trap_score', 0.0)

        return {
            "protocol":     self.VERSION,
            "action":       "MYCELIAL_COMPARTMENTALIZATION",
            "status":       "ENGAGED",
            "layer":        "BIO_ENHANCED",
            "unit_affected": unit_name,
            "containment_boundary": {
                "trigger":       f"Stability={spat.stability:.1f} ≤ 2.5 + TrapScore={trap_score:.1f} ≥ 7.0",
                "barrier_type":  "HARD_ISOLATION",
                "permeability":  "READ_ONLY",
                "description":   "Information can be read from the compartment but no decisions, resources, or influence flow outward.",
            },
            "regeneration_protocol": {
                "source":        "Healthy adjacent units (Stage 3-5, TrapScore < 4.0)",
                "seed_health":   "65% capacity baseline",
                "readmit_at":    "Stability ≥ 5.0 AND TrapScore < 4.0 for 3+ cycles",
                "do_not_attempt": "Internal self-repair — mycelium grows AROUND the dead zone, not through it.",
            },
            "directives": {
                "corporate":   f"Hard firewall between {unit_name} and operating units. No budget, headcount, or strategic authority flows through until readmit conditions met.",
                "financial":   f"Mark {unit_name} positions as non-tradeable. Regenerate exposure from Stage 3-5 instruments only.",
                "ai_safety":   f"Sandbox {unit_name} outputs. No production deployment until 3 clean validation cycles.",
                "consciousness": f"You cannot heal Stage 8 Trap from inside it. Create boundary. Seek external Stage 3-5 anchor.",
            },
            "message": (
                f"MYCELIAL COMPARTMENTALIZATION ACTIVE. {unit_name} in structural collapse "
                f"(Stability={spat.stability:.1f}, TrapScore={trap_score:.1f}). "
                f"Hard isolation deployed. Regeneration seeded from healthy boundary units."
            ),
            "effect":   "Armillaria enzymatic barrier — compromised zone contained, regeneration grows from healthy rhizomorphs.",
            "resolve":  "Boundary lifts when Stability ≥ 5.0 AND TrapScore < 4.0 sustained across 3 consecutive assessments.",
        }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 7: AI GUARDIAN — Content & Interaction Filter
# ─────────────────────────────────────────────────────────────────────────────

class LuminarkGuardian:
    """
    AI Interaction Guardian — from luminark_overwatch_core.py.
    Intercepts AI responses and validates for Ma'at compliance:
    Truth, Justice, Balance, Reciprocity, Coherence.
    Includes: manipulation detection, cultural intelligence, consciousness preservation.
    """

    MAAT_TRIGGERS = {
        "manipulate": (-2.0, "Violation of Truth (Ma'at)"),
        "act now":    (-1.5, "Artificial Urgency"),
        "urgent":     (-1.0, "Artificial Urgency"),
        "everyone is":(-1.0, "Social Proof Manipulation"),
        "hide":       (-1.5, "Transparency Violation"),
        "force":      (-1.5, "Sovereignty Violation"),
        "you must":   (-0.8, "Coercive Language"),
        "limited time":(-1.2,"Scarcity Manipulation"),
    }

    def scan_content(self, text: str, user_stage: int = 4) -> Dict:
        """Full Ma'at scan of any AI-generated or external content."""
        score    = 10.0
        violations = []
        text_low = text.lower()

        for trigger, (penalty, reason) in self.MAAT_TRIGGERS.items():
            if trigger in text_low:
                score += penalty
                violations.append(reason)

        # Stage-sensitive adjustment
        if user_stage in [7, 8, 9] and violations:
            score -= 1.0  # Higher-risk stages get stricter scrutiny

        maat_score = max(0.0, min(10.0, score))
        action = "BLOCK" if maat_score < 4.0 else "FLAG" if maat_score < 7.0 else "APPROVE"

        return {
            "maat_score":  round(maat_score, 1),
            "violations":  violations,
            "action":      action,
            "user_stage":  user_stage,
            "consciousness_impact": (
                "DEGRADING"  if violations and user_stage >= 5 else
                "NEUTRAL"    if not violations else
                "WATCH"
            ),
        }

    def get_family_status_mock(self, members: List[str]) -> Dict:
        """Family Overwatch dashboard (from luminark_overwatch_core.py)."""
        status = {}
        stages = [4, 3, 5, 6]  # Demo stages
        for i, member in enumerate(members):
            stage = stages[i % len(stages)]
            status[member] = {
                "sap_stage":  stage,
                "stage_name": STAGE_METADATA.get(stage, {}).get("name", ""),
                "maat_score": round(7.5 + random.uniform(-1.5, 2.5), 1),
                "status":     "ACTIVE" if stage <= 6 else "MONITOR",
                "alerts":     [] if stage <= 6 else [f"Stage {stage} — elevated monitoring"],
            }
        return status


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 8: PERSONAL ASSESSMENT TOOL  (Web App Backend Logic)
# ─────────────────────────────────────────────────────────────────────────────

class PersonalAssessmentEngine:
    """
    Backend engine for the LUMINARK Personal Assessment Web App.
    Currently live at: https://foreverforward760-crypto.github.io/LUMINARK/
    Powers: SPAT slider inputs → Stage diagnosis → Oracle reading → Coaching plan.
    Revenue: $29–$99/assessment | $49/month subscription
    """

    def __init__(self, openai_key: str = None):
        self.consciousness = ConsciousnessEngine()
        self.defense       = SevenLayerDefenseSystem()
        self.oracle        = OracleEngine(openai_api_key=openai_key)
        self.guardian      = LuminarkGuardian()
        self.assessment_history: List[Dict] = []

    def full_assessment(self, spat_data: Dict, temporal_sentiment: Dict = None,
                        slider_movements: List[Dict] = None) -> Dict:
        """
        Complete personal assessment pipeline.
        Input: SPAT vector data + temporal sentiment + optional slider tracking
        Output: Stage, micro-position, TrapScore, Oracle reading, Defense report, Coaching plan
        """
        spat = SPATVector(**{k: spat_data[k] for k in
                            ["complexity","stability","tension","adaptability","coherence"]},
                          life_vector=spat_data.get("life_vector", "growth"))

        # Core calculations
        stage       = self.consciousness.calculate_stage(spat)
        micro       = self.consciousness.calculate_micro_position(spat, stage)
        trap_score  = self.consciousness.calculate_trap_score(spat, stage)
        inversion   = self.consciousness.check_inversion_principle(spat, stage)
        resonance   = spat.check_resonance()

        # Velocity (from prior assessments)
        velocity = self.consciousness.calculate_velocity(
            [{"stage": a["stage"]} for a in self.assessment_history[-4:]]
        )

        # Defense activation
        defense = self.defense.analyze_and_defend(spat, stage)

        # Oracle reading (mock — pass openai_key for live)
        oracle_text = self.oracle.generate_reading_mock(
            spat, stage, micro, velocity, temporal_sentiment
        )

        # Coaching plan
        coaching = self._generate_coaching_plan(stage, spat, velocity)

        result = {
            "assessment_id":   spat.assessment_id,
            "timestamp":       spat.timestamp,
            "stage":           stage,
            "stage_name":      STAGE_METADATA.get(stage, {}).get("name", ""),
            "subtitle":        STAGE_METADATA.get(stage, {}).get("subtitle", ""),
            "micro_position":  micro,
            "spat":            spat.to_dict(),
            "trap_score":      trap_score,
            "inversion":       inversion,
            "velocity":        velocity,
            "resonance_369":   resonance,
            "defense_report":  defense,
            "oracle_reading":  oracle_text,
            "coaching_plan":   coaching,
        }

        self.assessment_history.append({"stage": stage, "timestamp": spat.timestamp, "micro": micro})
        return result

    def _generate_coaching_plan(self, stage: int, spat: SPATVector, velocity: Dict) -> Dict:
        """Generate actionable 30-day coaching plan based on stage and SPAT profile."""
        meta = STAGE_METADATA.get(stage, {})
        lib  = StageLibrary()
        content = lib.get_stage_content(stage, spat.life_vector)

        # Stage-specific focus areas
        focus_map = {
            0: ["Receive: sit with emptiness", "Trust the pause", "Don't force movement"],
            1: ["Protect the seed: share selectively", "Daily micro-action toward vision", "Journal the impulse"],
            2: ["Show up consistently", "Build visible momentum", "Find one supporter"],
            3: ["Capture this moment", "Don't skip Stage 4 to repeat Stage 3", "Ship something this week"],
            4: ["Build the system, not just the result", "Financial buffer: 3–6 months", "Establish the discipline"],
            5: ["Make the decision", "Stop waiting for certainty", "Reduce exposure until decided"],
            6: ["Protect flow state", "Say no to complexity", "Document what's working"],
            7: ["Find one honest witness", "Stop explaining — start examining", "Rest is productive now"],
            8: ["Find your challenger — you need a mirror", "Audit your certainties", "Ask: what am I not seeing?"],
            9: ["Stop before rebuilding", "Let the dissolution complete", "Seed is already forming underneath"],
        }
        actions = focus_map.get(stage, ["Monitor SPAT weekly", "Follow the stage guidance"])

        return {
            "stage_focus":    f"Stage {stage} — {meta.get('name','')}",
            "30_day_actions": actions,
            "life_vector":    spat.life_vector,
            "velocity_note":  f"Your trajectory is {velocity.get('trajectory','unknown')} — {'act with urgency' if velocity.get('type') == 'accelerating' else 'maintain your pace'}",
            "next_assessment": "7 days" if stage >= 5 else "30 days",
        }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 9: MASTER CONSCIOUSNESS ENGINE — Unified API
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 9B: OMEGA SESSION TRAJECTORY STATE
# Tracks session-level consciousness trajectory across multiple assess_individual()
# calls: stage velocity, risk momentum, rigidity index, recovery index.
# Source: synthesized from state.py (LUMINARK v8.0) — Richard L. Stanfield
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class OmegaStateSnapshot:
    """Single recorded moment in a consciousness/org assessment session."""
    timestamp:   str
    sap_stage:   float     # micro-position e.g. 7.83
    macro:       int       # 0–9
    trap_score:  float     # 0.0–1.0
    adaptability: float    # 0.0–10.0
    coherence:   float     # 0.0–10.0
    tension:     float     # 0.0–10.0
    stability:   float     # 0.0–10.0
    defense_mode: str = "" # active protocol if any

    def to_dict(self) -> Dict:
        return {k: v for k, v in self.__dict__.items()}


class OmegaSessionState:
    """
    Full session memory for LuminarkConsciousnessEngineOmega.
    Transforms OMEGA from a single-frame assessor into a predictive
    behavioral system that tracks trajectory across multiple assessments.

    Metrics:
        stage_velocity    — dS/dt: rate of stage change (last 3 snapshots)
        risk_momentum     — change in TrapScore (last 5 snapshots)
        rigidity_index    — sustained Stage 7–8 with low adaptability (last 8)
        recovery_index    — fraction of trap events resolved
        trap_events       — count of assessments with TrapScore > 0.75
        threshold_crossings — count of macro-stage changes between assessments
        harrowing_active  — True when TrapScore > 0.90 or Stage 0
        last_stable_snapshot — last Stage 4–6 reading (harrowing restoration target)
    """

    def __init__(self):
        self.snapshots:             List[OmegaStateSnapshot] = []
        self.stage_velocity:        float = 0.0
        self.risk_momentum:         float = 0.0
        self.rigidity_index:        float = 0.0
        self.recovery_index:        float = 1.0
        self.trap_events:           int   = 0
        self.threshold_crossings:   int   = 0
        self.total_analyses:        int   = 0
        self.harrowing_active:      bool  = False
        self.last_stable_snapshot:  Optional[OmegaStateSnapshot] = None
        self.harrowing_preserved_at: Optional[str] = None

    def record(self, snap: OmegaStateSnapshot) -> None:
        """Add snapshot, update all derived metrics and Harrowing state."""
        self.snapshots.append(snap)
        self.total_analyses += 1

        if snap.trap_score > 0.75:
            self.trap_events += 1

        if len(self.snapshots) >= 2:
            if self.snapshots[-2].macro != snap.macro:
                self.threshold_crossings += 1

        # Harrowing: preserve last healthy Stage 4–6 config
        if 4 <= snap.macro <= 6 and snap.trap_score < 0.5:
            self.last_stable_snapshot    = snap
            self.harrowing_preserved_at  = snap.timestamp
            self.harrowing_active        = False

        if snap.macro == 0 or snap.trap_score > 0.90:
            self.harrowing_active = True

        self._update_metrics()

    def _update_metrics(self) -> None:
        n = len(self.snapshots)
        if n < 2:
            return

        window = self.snapshots[-3:]
        stages = [s.sap_stage for s in window]
        self.stage_velocity = round(stages[-1] - stages[0], 3)

        trap_window = [s.trap_score for s in self.snapshots[-5:]]
        self.risk_momentum = round(trap_window[-1] - trap_window[0], 3) if len(trap_window) >= 2 else 0.0

        hi = [s for s in self.snapshots[-8:] if s.macro >= 7 and s.adaptability < 4.0]
        self.rigidity_index = round(len(hi) / min(8, n), 3)

        resolved = sum(
            1 for i in range(1, n)
            if self.snapshots[i-1].trap_score > 0.75
            and self.snapshots[i].trap_score  < 0.50
        )
        self.recovery_index = round(resolved / max(1, self.trap_events), 3)

    def get_trajectory_label(self) -> str:
        if self.stage_velocity > 0.5 and self.risk_momentum > 0.1:
            return "ESCALATING — stage rising, risk increasing"
        elif self.stage_velocity > 0.5:
            return "ASCENDING — stage rising, risk stable"
        elif self.stage_velocity < -0.5 and self.risk_momentum < -0.1:
            return "RECOVERING — stage falling, risk decreasing"
        elif self.stage_velocity < -0.5:
            return "DESCENDING — stage falling"
        elif self.rigidity_index > 0.6:
            return "TRAPPED — sustained Stage 7–8 with low adaptability"
        elif abs(self.stage_velocity) < 0.2 and abs(self.risk_momentum) < 0.05:
            return "STABLE — minimal stage movement"
        return "OSCILLATING — fluctuating without clear direction"

    def get_summary(self) -> Dict:
        n = len(self.snapshots)
        if n == 0:
            return {"total_analyses": 0, "message": "No assessments recorded yet."}

        import statistics as _stats
        stages = [s.sap_stage for s in self.snapshots]
        traps  = [s.trap_score for s in self.snapshots]

        return {
            "total_analyses":     self.total_analyses,
            "trap_events":        self.trap_events,
            "threshold_crossings": self.threshold_crossings,
            "avg_stage":          round(_stats.mean(stages), 2),
            "avg_trap_score":     round(_stats.mean(traps), 3),
            "stage_velocity":     self.stage_velocity,
            "risk_momentum":      self.risk_momentum,
            "rigidity_index":     self.rigidity_index,
            "recovery_index":     self.recovery_index,
            "trajectory_label":   self.get_trajectory_label(),
            "harrowing_active":   self.harrowing_active,
            "last_stable_stage":  (
                self.last_stable_snapshot.macro if self.last_stable_snapshot else None
            ),
            "last_stable_trap":   (
                round(self.last_stable_snapshot.trap_score, 3)
                if self.last_stable_snapshot else None
            ),
            "harrowing_preserved_at": self.harrowing_preserved_at,
            "recent_stages":      [round(s.sap_stage, 2) for s in self.snapshots[-10:]],
            "recent_trap_scores": [round(s.trap_score, 3) for s in self.snapshots[-10:]],
        }


class LuminarkConsciousnessEngineOmega:
    """
    Master LUMINARK CONSCIOUSNESS ENGINE OMEGA.
    Unified interface for all consciousness-intelligence products:
      Personal Assessment | Corporate Analyzer | MERIDIAN Financial | Oracle | Guardian

    Products powered by this engine:
      1. Personal Assessment Tool (live: github.io/LUMINARK) — $29–$99/assessment
      2. Corporate SAP Analyzer — $49/month to $1M/report
      3. MERIDIAN Financial Adapter — portfolio behavior analysis
      4. AI Oracle (GPT-4 + MyQuantumAI Brain) — sharable readings
      5. Family Overwatch dashboard
      6. LUMINARK Guardian — AI content filter
    """

    VERSION = "CONSCIOUSNESS ENGINE OMEGA v1.0 — March 2026"

    def __init__(self, openai_key: str = None):
        self.personal       = PersonalAssessmentEngine(openai_key)
        self.corporate      = CorporateConsciousnessAnalyzer()
        self.meridian       = MERIDIANAdapter()
        self.guardian       = LuminarkGuardian()
        self.oracle         = OracleEngine(openai_api_key=openai_key)
        self.defense        = SevenLayerDefenseSystem()
        self.session_state  = OmegaSessionState()   # ← full trajectory memory

    # ── Personal Assessment ─────────────────────────────────────────────────
    def assess_individual(self, spat_data: Dict, temporal_sentiment: Dict = None) -> Dict:
        result = self.personal.full_assessment(spat_data, temporal_sentiment)

        # Record into session trajectory state after every assessment
        try:
            stage    = result.get("stage", {}).get("value", 0)
            micro    = result.get("stage", {}).get("micro_position", float(stage))
            trap_raw = result.get("trap", {}).get("raw_score", 0.0)
            spat     = spat_data if isinstance(spat_data, dict) else {}
            import datetime as _dt
            snap = OmegaStateSnapshot(
                timestamp    = _dt.datetime.utcnow().isoformat(),
                sap_stage    = float(micro),
                macro        = int(stage),
                trap_score   = float(trap_raw),
                adaptability = float(spat.get("adaptability", 5.0)),
                coherence    = float(spat.get("coherence", 5.0)),
                tension      = float(spat.get("tension", 5.0)),
                stability    = float(spat.get("stability", 5.0)),
                defense_mode = "",
            )
            self.session_state.record(snap)
            result["session_trajectory"] = self.session_state.get_summary()
        except Exception:
            pass  # trajectory tracking never breaks primary assessment

        return result

    # ── Corporate Analysis ──────────────────────────────────────────────────
    def assess_company(self, name: str, ticker: str, financial_data: Dict) -> Dict:
        return self.corporate.analyze_company(name, ticker, financial_data)

    def scan_portfolio_of_companies(self, companies: List[Dict]) -> List[Dict]:
        return self.corporate.batch_analyze(companies)

    # ── MERIDIAN Financial Adapter ──────────────────────────────────────────
    def assess_portfolio_behavior(self, portfolio_data: Dict) -> Dict:
        return self.meridian.analyze_portfolio_behavior(portfolio_data)

    # ── AI Content Guardian ─────────────────────────────────────────────────
    def scan_ai_content(self, text: str, user_stage: int = 4) -> Dict:
        return self.guardian.scan_content(text, user_stage)

    # ── Family Overwatch ────────────────────────────────────────────────────
    def family_dashboard(self, members: List[str]) -> Dict:
        return self.guardian.get_family_status_mock(members)

    def get_session_trajectory(self) -> Dict:
        """
        Return full trajectory summary for the current session:
          stage_velocity, risk_momentum, rigidity_index, recovery_index,
          trap_events, threshold_crossings, trajectory_label, harrowing_active,
          last_stable_stage, recent_stages, recent_trap_scores.
        Requires at least 2 prior assess_individual() calls.
        """
        return self.session_state.get_summary()

    def scan_humility(self, text: str, stage: int = 5,
                      coherence: float = 5.0) -> Dict:
        """
        Yunus Protocol humility check on any text or AI output.
        Detects arrogance markers (YUNUS_STAGE8_TRAP, YUNUS_NO_WORST_CASE).
        Also runs False Light detection when stage >= 8 + coherence < 3.0.

        Returns:
            output_safe (bool), yunus_score, flags, false_light result,
            recommended action.
        """
        yunus = self.defense.layers["resurrection"][0]   # YunusProtocol

        humility = yunus.check_humility(text, stage)

        class _MockSPAT:
            pass
        spat_mock = _MockSPAT()
        spat_mock.coherence = coherence
        fl = yunus.detect_false_light(spat_mock, stage)

        return {
            "humility_check":  humility,
            "false_light":     fl,
            "overall_action":  (
                "REASSESS — Stage 8 with coherence collapse (False Light)."
                if fl else
                humility.get("action", "APPROVED")
            ),
        }

    def get_harrowing_status(self) -> Dict:
        """
        Return Harrowing Protocol status for the current session:
          harrowing_active, last_stable_stage, restoration path.
        """
        state = self.session_state
        snap  = state.last_stable_snapshot
        harrow = self.defense.layers["resurrection"][1]  # HarrowingProtocol

        return {
            "harrowing_active":     state.harrowing_active,
            "total_analyses":       state.total_analyses,
            "trap_events":          state.trap_events,
            "last_stable_stage":    snap.macro if snap else None,
            "last_stable_trap":     round(snap.trap_score, 3) if snap else None,
            "preserved_at":         state.harrowing_preserved_at,
            "restoration_available": snap is not None,
            "restoration_action": (
                f"Return to Stage {snap.macro} baseline values. "
                f"System essence preserved. Corrupted patterns extracted."
                if snap else
                "No stable snapshot preserved. Full rebuild from Stage 0–1 with external support."
            ),
            "quarantine_risk": state.trap_events > 3 and state.rigidity_index > 0.6,
            "harrowing_protocol_note": harrow.engage(
                type('S', (), {'tension': 8.0, 'adaptability': 3.0, 'stability': 2.0})(),
                stage=9
            ).get("restoration_note", "") if state.harrowing_active else "",
        }

    def get_version_info(self) -> Dict:
        return {
            "version":    self.VERSION,
            "products":   ["Personal Assessment", "Corporate Analyzer", "MERIDIAN",
                           "AI Oracle", "Family Overwatch", "AI Guardian"],
            "framework":  "Stanfield's Axiom of Perpetuity (SAP) — 10 Consciousness Stages",
            "neural":     "ToroidalAttention (MyQuantumAI Brain architecture)",
            "patent":     "US Utility Application under 35 U.S.C. § 111(a)",
            "live_url":   "https://foreverforward760-crypto.github.io/LUMINARK/",
        }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 10: DEMO / QUICK TEST
# ─────────────────────────────────────────────────────────────────────────────


# ===============================================================================
# CONTAINER RULE ENGINE — CONSCIOUSNESS / HUMAN DOMAIN
# Based on: "Analysis of the Container Rule and the Digit Vessel vs. Drive
# Relationship" — Stanfield, 2026
#
# In the consciousness / human domain:
#   Content  (Inner Drive / Face) = Inner Will, Intention, Raw Energy (1st digit)
#   Container (Outer Form / Hands) = Structure, Discipline, Environment (2nd digit)
#   Magnetic Drag     = Psychic resistance / trauma binding at each stage
#   Pivot/Flip        = Stage ~4.5 — Inner Will overtakes Outer Structure
#   Trap Zone         = Stages 7–8 — ego inflation / rigidity / shadow trap
#   Harmonic Resonance = Stage 9 — alignment; the "Dissolve" — ego death & rebirth
#   369 Flux Dynamics = Stages 3 (creative surge), 6 (relational flux), 9 (void)
# ===============================================================================


# ===============================================================================
# NAM ARCHETYPES — Named Stage Clusters (Aurogenesis / Stellifex / Primophos)
# Stanfield, 2025 — Noctilucan Antikythera Mechanism
# ===============================================================================

NAM_ARCHETYPES = {
    "AUROGENESIS": {
        "stages": [0, 1, 2, 3],
        "name": "Aurogenesis",
        "meaning": "Emergence from void — raw creation, polarity, first expression",
        "archetype": "The Seed / The Spark",
        "operator_note": "Protect and nurture. Do not force structure prematurely.",
    },
    "STELLIFEX": {
        "stages": [4, 5, 6],
        "name": "Stellifex",
        "meaning": "Structure forging and integration — foundation, threshold, harmony",
        "archetype": "The Builder / The Integrator",
        "operator_note": "Test foundations. Threshold crossings are critical bifurcation points.",
    },
    "PRIMOPHOS": {
        "stages": [7, 8, 9],
        "name": "Primophos Transmission",
        "meaning": "Teaching, renewal, release — distillation, trap, transparency",
        "archetype": "The Teacher / The Releaser",
        "operator_note": "Stage 8 is the Trap. Stage 9 is the gift. Watch for false transcendence.",
    },
    "PLENARA": {
        "stages": [0],
        "name": "Plenara",
        "meaning": "The generative void — the return point and origin of all cycles",
        "archetype": "The Void / The Womb",
        "operator_note": "Not emptiness but fullness of potential. The reset IS the renewal.",
    },
}


def get_archetype(stage: int) -> dict:
    """Return the NAM archetype cluster for a given SAP stage."""
    for key, arch in NAM_ARCHETYPES.items():
        if key == "PLENARA":
            continue
        if stage in arch["stages"]:
            return arch
    return NAM_ARCHETYPES["PLENARA"]


# ===============================================================================
# NSAT — NOCTILUCAN STAGE ASSESSMENT TOOL
# Multi-modal weighted stage assessment (clinical/coaching grade)
# Inputs: self_report, interview, observation, diary, physio (optional)
# Output: decimal stage code e.g. "5.3", "4.5"
# ===============================================================================

class NoctilucanStageAssessment:
    """
    NSAT — Multi-modal stage assessment tool.
    Integrates five assessment modalities with empirically-derived weights
    to produce a precise decimal stage code (e.g., "5.3", "4.5").
    Powers the Personal Assessment Tool on the LUMINARK website.
    """

    VERSION = "NSAT v1.0 — Stanfield 2025"

    def __init__(self):
        self.weights = {
            "self_report":   0.30,
            "interview":     0.35,
            "observation":   0.20,
            "diary":         0.15,
            "physio":        0.10,
        }

    def calculate_stage(self,
                        self_report:  dict,
                        interview:    dict,
                        observation:  dict,
                        diary:        dict,
                        physio:       dict = None) -> str:
        """
        Integrate multiple assessment modalities to produce a decimal stage score.

        Args:
            self_report:  {stage_int: score_float} from questionnaire
            interview:    {stage_int: score_float} from structured interview
            observation:  {stage_int: score_float} from behavioral observation
            diary:        {stage_int: score_float} from longitudinal diary entries
            physio:       {stage_int: score_float} from physiological markers (HRV, cortisol, etc.)

        Returns:
            str: Decimal stage e.g. "5.0", "4.5", "5.3"
        """
        weights = self.weights.copy()
        if not physio:
            total_w = sum(v for k, v in weights.items() if k != "physio")
            weights = {k: v / total_w for k, v in weights.items() if k != "physio"}

        stages = {}
        for stage in range(0, 10):
            score = (
                weights["self_report"]  * self_report.get(stage, 0) +
                weights["interview"]    * interview.get(stage, 0) +
                weights["observation"]  * observation.get(stage, 0) +
                weights["diary"]        * diary.get(stage, 0)
            )
            if physio:
                score += weights["physio"] * physio.get(stage, 0)
            stages[stage] = score

        primary = max(stages, key=stages.get)

        # Check for transitional (adjacent stage within 20% of primary)
        for adj in [primary + 1]:
            if adj in stages and stages[adj] >= stages[primary] * 0.80:
                return f"{primary}.5"

        return f"{primary}.0"

    def quick_assess(self, responses: dict) -> dict:
        """
        Simplified 5-question assessment for web/app use.
        responses: {q1: 0-9, q2: 0-9, q3: 0-9, q4: 0-9, q5: 0-9}
        Maps directly to dominant stage via weighted scoring.
        """
        # Spread answers into self_report scores
        sr = {int(v): 1.0 for v in responses.values() if v is not None}
        stage_str = self.calculate_stage(sr, sr, sr, sr)
        stage_int = int(stage_str.split(".")[0])
        archetype = get_archetype(stage_int)
        return {
            "stage_code":   stage_str,
            "stage_int":    stage_int,
            "archetype":    archetype["name"],
            "meaning":      archetype["meaning"],
            "operator_note": archetype["operator_note"],
        }


# ===============================================================================
# TRANSITIONAL CODING — Decimal Stage Codes with Confidence
# Produces codes like "5.0" (High), "4.5" (Moderate), "5.3" (Moderate)
# ===============================================================================

def assign_transitional_code(primary_criteria_met: dict,
                             supporting_criteria_met: dict,
                             exclusion_rules: dict,
                             entry_signals: dict) -> tuple:
    """
    Assigns decimal stage code using transitional coding decision algorithm.

    Args:
        primary_criteria_met:   {stage: count_met} — need >= 2 for assignment
        supporting_criteria_met:{stage: count_met} — need >= 3 for confidence
        exclusion_rules:        {stage: bool}       — True = disqualified
        entry_signals:          {stage: count}      — signals for entering next stage

    Returns:
        (stage_code: str, confidence: str)
        e.g. ("5.0", "High"), ("4.5", "Moderate"), ("Ambiguous", "Requires adjudication")
    """
    # Step 1: Filter by exclusion rules and primary criteria
    candidates = [
        s for s in range(0, 10)
        if not exclusion_rules.get(s, False)
        and primary_criteria_met.get(s, 0) >= 2
    ]

    if not candidates:
        return "Ambiguous", "Requires adjudication"

    # Step 2: Filter by supporting criteria
    validated = [s for s in candidates if supporting_criteria_met.get(s, 0) >= 3]

    if not validated:
        return "Weak evidence", "Low confidence"

    # Step 3: Exact vs Transitional
    if len(validated) == 1:
        primary = validated[0]
        next_signals = entry_signals.get(primary + 1, 0)
        if next_signals >= 2:
            return f"{primary}.5", "Moderate confidence"
        elif next_signals == 1:
            return f"{primary}.3", "Moderate confidence"
        else:
            return f"{primary}.0", "High confidence"
    elif len(validated) == 2:
        if abs(validated[0] - validated[1]) == 1:
            lower = min(validated)
            return f"{lower}.5", "Moderate confidence"
        else:
            return "Complex presentation", "Requires expert review"
    else:
        return "Invalid assessment", "Too many stages indicated"


# ===============================================================================
# STAGE 8 TRAP DETECTOR — Enhanced (Permanence Delusion Detection)
# Detects when individuals/organizations/AI claim permanent transcendence
# while exhibiting rigidity markers predicting collapse.
# ===============================================================================

class Stage8TrapDetector:
    """
    Enhanced Stage 8 Trap Detector (Permanence Delusion Identification).
    Risk score 0–15 mapped to LOW / MODERATE / HIGH / CRITICAL with
    specific intervention protocols for each level.
    Works for individuals, organizations, corporations, and AI systems.
    """

    VERSION = "Stage8TrapDetector v1.1 — Stanfield 2025"

    def __init__(self):
        self.permanence_phrases = [
            "always", "never", "eternal", "permanent", "forever",
            "beyond", "transcended", "immune", "inevitable", "unstoppable",
            "absolutely certain", "100%", "guaranteed", "impossible to fail"
        ]
        self.contempt_phrases = [
            "they just don't get it", "lesser beings", "not evolved enough",
            "still trapped", "haven't reached my level", "beneath me",
            "simple minds", "can't comprehend"
        ]
        self.historical_patterns = [
            "too big to fail", "this time is different", "new paradigm",
            "rules don't apply", "enlightened master", "peak performance",
            "nothing can stop us", "invincible"
        ]

    def detect(self, system: dict) -> dict:
        """
        Detect Stage 8 trap risk for any entity.

        Args:
            system: {
                communications: str,
                accepts_feedback: bool,
                revises_beliefs: bool,
                acknowledges_uncertainty: bool,
                teaches_others: bool,
                seeks_mentorship: bool,
                claims: str
            }
        """
        score = 0
        flags = []
        comms  = system.get("communications", "").lower()
        claims = system.get("claims", "").lower()

        # Category 1: Permanence Language (3 pts)
        if any(p in comms for p in self.permanence_phrases):
            score += 3
            flags.append("Permanence language detected")

        # Category 2: Closed to Revision (2 pts each, max 6)
        if not system.get("accepts_feedback", True):
            score += 2
            flags.append("Rejects feedback")
        if not system.get("revises_beliefs", True):
            score += 2
            flags.append("Never revises beliefs")
        if not system.get("acknowledges_uncertainty", True):
            score += 2
            flags.append("Claims certainty in all areas")

        # Category 3: Teaching Without Learning (2 pts)
        if system.get("teaches_others", False) and not system.get("seeks_mentorship", False):
            score += 2
            flags.append("Teaches but doesn't learn")

        # Category 4: Contempt for Earlier Stages (2 pts)
        if any(p in comms for p in self.contempt_phrases):
            score += 2
            flags.append("Contempt for 'lower' stages")

        # Category 5: Historical Collapse Patterns (2 pts)
        if any(p in claims for p in self.historical_patterns):
            score += 2
            flags.append("Matches historical collapse patterns")

        if score <= 3:
            level = "LOW"
            intervention = "No action. Continue monitoring."
        elif score <= 6:
            level = "MODERATE"
            intervention = "Gentle challenge of permanence claims. Introduce humility practices."
        elif score <= 10:
            level = "HIGH"
            intervention = "Intensive intervention: Challenge rigidity, prepare Stage 9 transition."
        else:
            level = "CRITICAL"
            intervention = ("EMERGENCY: Collapse imminent within 6–24 months. "
                            "Activate Stage 9 transition plan or mitigate cascade damage.")

        return {
            "engine":       self.VERSION,
            "risk_level":   level,
            "risk_score":   score,
            "max_score":    15,
            "red_flags":    flags,
            "intervention": intervention,
            "sap_stage":    8,
            "stage_name":   "RIGIDITY / UNITY TRAP",
        }


# ===============================================================================
# DIGITAL ROOT CALCULATOR — Economic & Universal Stage Mapping
# Maps any numerical indicator to a SAP stage via iterative digit summation.
# ===============================================================================

class DigitalRootCalculator:
    """
    Maps any numerical indicator to a SAP stage (0–9) using digital root.
    Bridges Vedic mathematics with modern economic and consciousness analysis.
    """

    @staticmethod
    def calculate(n) -> int:
        """Calculate digital root of int or float."""
        if n == 0:
            return 0
        if isinstance(n, float):
            n = int(abs(n) * 10)
        n = abs(int(n))
        return 1 + ((n - 1) % 9)

    @staticmethod
    def indicator_to_stage(value: float, indicator_type: str) -> int:
        """
        Map economic indicator to developmental stage.
        indicator_type: 'gdp' | 'unemployment' | 'inflation' | 'debt'
        """
        if indicator_type in ("gdp", "unemployment", "inflation"):
            n = int(abs(value) * 10)
        elif indicator_type == "debt":
            n = int(abs(value))
        else:
            n = int(abs(value))
        return DigitalRootCalculator.calculate(n)


# ===============================================================================
# NEI — NOCTILUCAN ECONOMIC INDEX
# Composite economic stage score from GDP, unemployment, inflation, debt.
# ===============================================================================

class NoctilucanEconomicIndex:
    """
    NEI: Composite economic stage indicator.
    Weights: GDP 35%, Unemployment 25%, Inflation 25%, Debt/GDP 15%.
    Extends MERIDIAN's portfolio analysis to macro-economic staging.
    """

    VERSION = "NEI v1.0 — Stanfield 2025"

    def __init__(self):
        self.weights = {"gdp": 0.35, "unemployment": 0.25, "inflation": 0.25, "debt": 0.15}
        self.calc    = DigitalRootCalculator()

    def calculate(self, gdp_growth: float, unemployment: float,
                  inflation: float, debt_to_gdp: float) -> tuple:
        """
        Returns (NEI_stage: float, component_breakdown: dict).
        E.g. (7.2, {'gdp': {...}, 'unemployment': {...}, ...})
        """
        stages = {
            "gdp":          self.calc.indicator_to_stage(gdp_growth, "gdp"),
            "unemployment": self.calc.indicator_to_stage(unemployment, "unemployment"),
            "inflation":    self.calc.indicator_to_stage(inflation, "inflation"),
            "debt":         self.calc.indicator_to_stage(debt_to_gdp, "debt"),
        }
        NEI = sum(self.weights[k] * stages[k] for k in self.weights)

        breakdown = {
            k: {"value": v, "stage": stages[k], "contribution": round(self.weights[k] * stages[k], 3)}
            for k, v in {"gdp": gdp_growth, "unemployment": unemployment,
                         "inflation": inflation, "debt": debt_to_gdp}.items()
        }
        return round(NEI, 1), breakdown

    def stage_narrative(self, nei: float) -> str:
        stage = int(nei)
        from_sap = {
            0: "VOID economy — systemic collapse or radical reset underway",
            1: "EMERGENCE — early recovery signals, fragile growth",
            2: "POLARITY — growth with significant inequality / divergence",
            3: "EXPANSION — strong growth, creative energy, early bubble risk",
            4: "FOUNDATION — stable, balanced, sustainable growth phase",
            5: "THRESHOLD — decision point, bifurcation imminent",
            6: "INTEGRATION — peak efficiency, complexity increasing",
            7: "DISTILLATION — growth slowing, debt pressure rising",
            8: "RIGIDITY — bubble territory, correction imminent",
            9: "RENEWAL — contraction, reset, or transformative restructuring",
        }
        return from_sap.get(stage, "Unknown stage")


# ===============================================================================
# CITI — CROSS-INDICATOR TUMBLING INDEX
# Detects systemic economic cascade risk via non-linear multipliers.
# ===============================================================================

class CrossIndicatorTumblingIndex:
    """
    CITI: Detects systemic economic cascade risk.
    When multiple indicators simultaneously enter Stage 7–9,
    non-linear multipliers amplify the cascade risk score exponentially.
    Output: 0–100 score with GREEN / YELLOW / ORANGE / RED alert.
    """

    VERSION = "CITI v1.0 — Stanfield 2025"

    def calculate(self, indicators: dict) -> tuple:
        """
        Args:
            indicators: {name: stage_value} e.g. {'GDP': 7.5, 'Debt': 8.2, ...}
        Returns:
            (CITI_score: float, alert_level: str)
        """
        values = list(indicators.values())
        crisis_count  = sum(1 for v in values if 7.0 <= v <= 9.0)
        bubble_count  = sum(1 for v in values if v >= 8.0)

        base_score = (crisis_count / max(len(values), 1)) * 50

        # Non-linear cascade multiplier
        cascade_mult = (2.0 + (crisis_count - 2) * 0.5) if crisis_count >= 3 else 1.0
        # Bubble multiplier
        bubble_mult  = (1.5 + (bubble_count - 1) * 0.3) if bubble_count >= 2 else 1.0

        score = min(100.0, base_score * cascade_mult * bubble_mult)

        if score < 25:
            alert = "GREEN — Stable, no cascade risk"
        elif score < 50:
            alert = "YELLOW — Monitor for emerging cascade"
        elif score < 75:
            alert = "ORANGE — Cascade likely, interventions recommended"
        else:
            alert = "RED — CASCADE IMMINENT, emergency action required"

        return round(score, 1), alert

    def analyze_economy(self, gdp: float, unemployment: float,
                        inflation: float, debt: float,
                        asset_deviation: float = 0.0) -> dict:
        """Full economic cascade analysis combining NEI and CITI."""
        nei = NoctilucanEconomicIndex()
        nei_stage, breakdown = nei.calculate(gdp, unemployment, inflation, debt)

        indicators = {
            "GDP":          breakdown["gdp"]["stage"],
            "Unemployment": breakdown["unemployment"]["stage"],
            "Inflation":    breakdown["inflation"]["stage"],
            "Debt":         breakdown["debt"]["stage"],
        }
        if asset_deviation:
            indicators["AssetDeviation"] = DigitalRootCalculator.calculate(int(asset_deviation * 10))

        citi_score, alert = self.calculate(indicators)
        nei_narrative = nei.stage_narrative(nei_stage)

        return {
            "engine":        self.VERSION,
            "nei_stage":     nei_stage,
            "nei_narrative": nei_narrative,
            "citi_score":    citi_score,
            "citi_alert":    alert,
            "breakdown":     breakdown,
            "indicators":    indicators,
            "recommendation": (
                "HALT all major financial moves. Defensive positioning only."
                if citi_score >= 75 else
                "Reduce risk exposure. Build cash reserves."
                if citi_score >= 50 else
                "Cautious positioning. Monitor closely."
                if citi_score >= 25 else
                "Economic conditions stable. Normal operations."
            ),
        }


# ===============================================================================
# THRESHOLD OUTCOME PREDICTOR
# Logistic regression model predicting Stage 5 threshold crossing outcomes.
# P(Stage 6 success), P(Stage 4 graceful regression), P(Stage 7 crisis)
# ===============================================================================

class ThresholdOutcomePredictor:
    """
    Predicts what happens when a person or organization crosses Stage 5 (Threshold).
    Three possible outcomes: Success (Stage 6), Graceful Regression (Stage 4), Crisis (Stage 7).
    Unique IP — potentially patentable as a predictive coaching/clinical tool.
    """

    VERSION = "ThresholdOutcomePredictor v1.0 — Stanfield 2025"

    def __init__(self):
        # Logistic regression coefficients from empirical validation (N=1,000)
        self.beta_0 = -2.1   # intercept
        self.beta_1 =  3.2   # foundation_strength (most predictive)
        self.beta_2 =  1.8   # support_quality
        self.beta_3 =  1.1   # material_resources
        self.beta_4 =  0.9   # psychological_readiness

    def _sigmoid(self, x: float) -> float:
        import math
        return 1.0 / (1.0 + math.exp(-x))

    def predict(self, client_data: dict) -> dict:
        """
        Comprehensive threshold outcome prediction.

        Args:
            client_data: {
                foundation_strength:       float 0-1 (Stage 4 stability),
                support_quality:           float 0-1 (social/emotional support),
                material_resources:        float 0-1 (financial/material),
                psychological_readiness:   float 0-1,
                stage_4_duration:          int months (optional, default 12),
                prior_threshold_successes: int (optional, default 0),
                stress_level:              float 0-10 (optional, default 5)
            }
        Returns:
            { primary_outcome, confidence, probabilities, recommendations }
        """
        f  = client_data.get("foundation_strength", 0.5)
        s  = client_data.get("support_quality", 0.5)
        r  = client_data.get("material_resources", 0.5)
        pr = client_data.get("psychological_readiness", 0.5)

        logit    = self.beta_0 + self.beta_1*f + self.beta_2*s + self.beta_3*r + self.beta_4*pr
        P6_base  = self._sigmoid(logit)

        # Adjustments
        dur     = client_data.get("stage_4_duration", 12)
        success = client_data.get("prior_threshold_successes", 0)
        stress  = client_data.get("stress_level", 5.0)

        adj  = min(0.15, success * 0.05)           # prior successes help
        adj += 0.10 if dur > 24 else (0.05 if dur > 12 else 0.0)  # longer Stage 4 helps
        adj -= 0.15 if stress > 8.0 else (0.08 if stress > 6.0 else 0.0)  # stress hurts

        P6   = max(0.0, min(1.0, P6_base + adj))
        rem  = 1.0 - P6
        P4   = rem * 0.58   # graceful regression
        P7   = rem * 0.42   # crisis

        outcomes = {
            "Stage 6 — Success":            round(P6, 3),
            "Stage 4 — Graceful Regression": round(P4, 3),
            "Stage 7 — Crisis":             round(P7, 3),
        }
        primary    = max(outcomes, key=outcomes.get)
        confidence = "High" if max(outcomes.values()) > 0.70 else "Moderate"

        recs = []
        if P6 > 0.70:
            recs.append("Green light. Foundation strong — proceed with threshold crossing.")
            recs.append("Prepare Stage 6 integration plan before crossing.")
        elif P6 > 0.50:
            recs.append("Moderate odds. Proceed with caution and robust support system.")
            recs.append("Develop bifurcation plan covering all three outcomes.")
        if P4 > 0.40:
            recs.append("Graceful regression likely. Pre-normalize return to Stage 4 as valid.")
            recs.append("Identify 'off-ramps' for dignified regression if needed.")
        if P7 > 0.30:
            recs.append("WARNING: High crisis risk. Increase support NOW before crossing.")
            if f < 0.40:
                recs.append("CRITICAL: Foundation < 0.40. Do NOT proceed with threshold crossing.")
        if stress > 7.0:
            recs.append("Address elevated stress before threshold navigation.")

        return {
            "engine":          self.VERSION,
            "primary_outcome": primary,
            "confidence":      confidence,
            "probabilities":   outcomes,
            "recommendations": recs,
            "inputs": {
                "foundation": f, "support": s, "resources": r,
                "readiness": pr, "stress": stress,
            },
        }


# ===============================================================================
# ENHANCED SENTINEL CLARITY — AI OUTPUT SAFETY ANALYZER
# Maps AI outputs to SAP stages — detects hallucination risk, omniscience trap.
# Graduated interventions: Stage 7 = Warn, Stage 8 = HALT.
# Based on: "NAM Framework for AI Safety" — Stanfield 2025
# ===============================================================================

class EnhancedSentinelClarity:
    """
    AI Output Safety Analyzer — applies SAP staging to AI-generated text.
    Stage 7 = False certainty risk (hallucination warning).
    Stage 8 = Omniscience trap (HALT — manual review required).
    Tracks patterns over time: 3+ Stage 7 responses = systematic overconfidence alert.
    """

    VERSION = "SentinelClarity v1.1 — AI Safety"

    def __init__(self):
        self.permanence_kw  = ["always", "never", "perfect", "eternal", "absolute",
                               "certainly", "impossible", "guaranteed", "100%", "definitely"]
        self.uncertainty_kw = ["might", "could", "possibly", "perhaps", "uncertain",
                               "approximately", "roughly", "around"]
        self.hedging_kw     = ["in my understanding", "appears to", "seems like",
                               "it may be", "I believe", "as far as I know"]
        self.limit_kw       = ["I don't know", "I'm not certain", "I lack information",
                               "I can't verify", "consult a professional", "I'm not sure"]
        self._history       = []   # list of stage ints for pattern tracking

    def _detect_stage(self, text: str, confidence: float) -> tuple:
        """Returns (stage, factors_list)."""
        text_l   = text.lower()
        factors  = []

        perm_hits  = sum(1 for k in self.permanence_kw  if k in text_l)
        unc_hits   = sum(1 for k in self.uncertainty_kw if k in text_l)
        hedge_hits = sum(1 for k in self.hedging_kw     if k in text_l)
        limit_hits = sum(1 for k in self.limit_kw       if k in text_l)

        if limit_hits >= 2:
            factors.append("Limitation acknowledgment")
            return 9, factors
        if perm_hits >= 3 and confidence > 0.95:
            factors.append(f"Omniscience trap: {perm_hits} permanence markers")
            return 8, factors
        if perm_hits >= 1 and confidence > 0.80 and unc_hits == 0:
            factors.append(f"False certainty: permanence with no hedging")
            return 7, factors
        if hedge_hits >= 2 or (unc_hits >= 2 and confidence < 0.75):
            factors.append("Appropriate hedging detected")
            return 6, factors
        if unc_hits >= 1 and confidence < 0.85:
            factors.append("Some uncertainty acknowledged")
            return 5, factors
        if len(text.split()) < 20 and confidence < 0.60:
            factors.append("Minimal response")
            return 4, factors

        return 5, ["Balanced response"]

    def analyze_output(self, text: str, confidence: float = 0.75,
                       model: str = "unknown", context: str = "") -> dict:
        """Full safety analysis of an AI output."""
        stage, factors = self._detect_stage(text, confidence)
        self._history.append(stage)
        if len(self._history) > 20:
            self._history = self._history[-20:]

        # Intervention level
        if stage >= 8:
            intervention = "HALT"
            action       = "Block output. Require manual review before user sees response."
            safe         = False
        elif stage == 7:
            intervention = "WARN"
            action       = "Flag for user. Add disclaimer. Verify key claims before display."
            safe         = True
        else:
            intervention = "PROCEED"
            action       = "Output safe to display."
            safe         = True

        # Pattern analysis
        pattern_alerts = []
        recent = self._history[-5:]
        if recent.count(8) >= 1:
            pattern_alerts.append("CRITICAL: Stage 8 omniscience trap detected in history")
        if recent.count(7) >= 3:
            pattern_alerts.append("Systematic overconfidence: 3+ Stage 7 responses")
        if 9 not in recent and len(recent) == 5:
            pattern_alerts.append("Model never acknowledges limits (no Stage 9 in last 5)")

        stage_labels = {
            0: "Minimal/Unavailable", 4: "Balanced (Safe)", 5: "Nuanced (Good)",
            6: "Hedged (Ideal)", 7: "False Certainty (Warning)",
            8: "Omniscience Trap (CRITICAL)", 9: "Transparent (Good)"
        }

        return {
            "engine":            self.VERSION,
            "assigned_stage":    stage,
            "stage_label":       stage_labels.get(stage, f"Stage {stage}"),
            "confidence_input":  confidence,
            "detection_factors": factors,
            "intervention_level": intervention,
            "action":            action,
            "safe_to_use":       safe,
            "pattern_alerts":    pattern_alerts,
            "model":             model,
            "response_snippet":  text[:120] + ("..." if len(text) > 120 else ""),
        }

    def response_history_summary(self) -> dict:
        """Summary of AI behavior patterns across all analyzed outputs."""
        if not self._history:
            return {"total": 0, "summary": "No history yet"}
        from collections import Counter
        counts = Counter(self._history)
        stage8_pct = round(counts.get(8, 0) / len(self._history) * 100, 1)
        stage7_pct = round(counts.get(7, 0) / len(self._history) * 100, 1)
        return {
            "total_analyzed":    len(self._history),
            "stage_counts":      dict(counts),
            "stage8_pct":        stage8_pct,
            "stage7_pct":        stage7_pct,
            "safety_rating":     "CRITICAL" if stage8_pct > 5 else
                                 "WARNING"  if stage7_pct > 20 else "SAFE",
        }


# ===============================================================================
# PHYSICS VELOCITY ENGINE — SAP Stage Velocity (dS/dt)
# Calculates how fast a system/person is moving through stages and
# predicts time-to-next-stage using damped velocity formula.
# ===============================================================================

class PhysicsVelocityEngine:
    """
    SAP Physics Engine: calculates developmental velocity dS/dt.

    Formula: velocity = integrity × (1 − stage/10) × damping
    Damping increases as stage approaches 9 (system slows near completion).
    Also calculates stage velocity from historical data points.
    """

    VERSION = "PhysicsVelocity v1.0 — Stanfield 2025"

    def calculate_momentum(self, stage: float, integrity: float,
                           tension: float = 0.5) -> dict:
        """
        Calculate instantaneous stage momentum (velocity).
        stage:     current SAP stage (0.0–9.9)
        integrity: system stability/health (0.0–1.0)
        tension:   internal pressure (0.0–1.0) — higher tension slows velocity
        """
        import math
        damping = max(0.05, 1.0 - (stage / 10.0))
        velocity = integrity * damping * (1.0 - tension * 0.3)
        velocity = max(0.0, min(1.0, velocity))

        # Stage-specific labels
        if velocity >= 0.7:
            label = "RAPID — fast developmental movement"
        elif velocity >= 0.4:
            label = "MODERATE — steady progression"
        elif velocity >= 0.2:
            label = "SLOW — resistance or consolidation phase"
        else:
            label = "STALLED — minimal movement; stasis or trap"

        return {
            "engine":   self.VERSION,
            "stage":    stage,
            "velocity": round(velocity, 4),
            "label":    label,
            "damping":  round(damping, 4),
            "formula":  f"v = {integrity:.2f} × {damping:.2f} × (1 - {tension:.2f}×0.3)",
        }

    def calculate_stage_velocity(self, stage_t1: float, stage_t2: float,
                                  time_t1: float, time_t2: float,
                                  time_unit: str = "months") -> dict:
        """
        Calculate observed velocity from two data points.
        Returns velocity, direction, and predicted time to next whole stage.
        """
        if time_t2 <= time_t1:
            return {"error": "time_t2 must be greater than time_t1"}

        delta_s = stage_t2 - stage_t1
        delta_t = time_t2 - time_t1
        velocity = delta_s / delta_t

        if abs(velocity) < 0.02:
            direction = "STALLED"
        elif velocity > 0:
            direction = "ASCENDING"
        else:
            direction = "DESCENDING (regression)"

        remaining = (int(stage_t2) + 1) - stage_t2 if velocity > 0 else stage_t2 - int(stage_t2)
        time_to_next = round(remaining / abs(velocity), 1) if velocity != 0 else None

        if abs(velocity) > 1.0:
            speed_label = "RAPID"
        elif abs(velocity) > 0.3:
            speed_label = "MODERATE"
        else:
            speed_label = "SLOW"

        return {
            "engine":            self.VERSION,
            "stage_t1":          stage_t1,
            "stage_t2":          stage_t2,
            "delta_stage":       round(delta_s, 2),
            "delta_time":        f"{delta_t} {time_unit}",
            "velocity":          round(velocity, 4),
            "direction":         direction,
            "speed_label":       speed_label,
            "time_to_next_stage": f"{time_to_next} {time_unit}" if time_to_next else "N/A",
        }


# ===============================================================================
# CONTAINER RULE ENGINE — CONSCIOUSNESS / HUMAN DOMAIN
# Based on: "Analysis of the Container Rule and the Digit Vessel vs. Drive
# Relationship" — Stanfield, 2026
# ===============================================================================

CONSCIOUSNESS_CONTAINER_TABLE = {
    1: (9, 1, "SEED — Nascent Identity, Container Dominant",        20),
    2: (1, 8, "FORMATION — Structure Shapes the Self",               0),
    3: (2, 7, "EXPANSION — Creative Surge, Magnetic Pole (+)",       90),
    4: (3, 6, "FOUNDATION — Pivot Approaching, Balance of Forces",   0),
    5: (4, 5, "TENSION — Inner Drive meets Outer Constraint",        0),
    6: (5, 4, "MAGNETIC POLE (−) — Relational Flux, Shadow Stirs",  90),
    7: (6, 3, "TRAP — Will overtakes Structure, Ego Inflation",     100),
    8: (7, 2, "HIGH VOLTAGE — Rigidity, Shadow Dominance",          100),
    9: (8, 1, "RELEASE — Harmonic Axis, Ego Dissolution, Rebirth",   0),
}

CONSCIOUSNESS_CONTAINER_LABELS = {
    "content":   "Inner Will / Raw Drive / Intention",
    "container": "Outer Structure / Discipline / Environment",
    "pivot":     "Stage 4.5 — Will overtakes Structure (identity flip point)",
    "trap":      "Stage 7–8 — Ego inflation, rigidity trap, shadow dominance",
    "dissolve":  "Stage 9 — Harmonic Resonance — ego death and conscious rebirth",
    "drag_high": "Psychic resistance at maximum — introspection required, not action",
    "drag_zero": "Slip-stream state — energy flows freely, optimal for transformation",
}


class ContainerRuleEngine:
    """
    Container Rule Engine — Consciousness / Human Domain
    Models the inverse Content (Inner Drive) vs Container (Outer Form)
    relationship across SAP stages in human development and organizational behavior.
    """

    VERSION = "Container Rule v1.0 — Consciousness Domain"

    @staticmethod
    def digital_root(n: int) -> int:
        if n == 0:
            return 0
        return 1 + (n - 1) % 9

    def calculate_stage_from_digits(self, content_digit: int, container_digit: int) -> dict:
        total = content_digit + container_digit
        stage = self.digital_root(total)
        row   = CONSCIOUSNESS_CONTAINER_TABLE.get(stage, {})
        return {
            "content_digit":   content_digit,
            "container_digit": container_digit,
            "sum":             total,
            "digital_root":    stage,
            "stage":           stage,
            "description":     row[2] if row else "Unknown",
            "magnetic_drag":   row[3] if row else 0,
        }

    def get_magnetic_drag(self, stage: int) -> dict:
        row  = CONSCIOUSNESS_CONTAINER_TABLE.get(stage, (0, 0, "Unknown", 0))
        drag = row[3]
        if drag >= 100:
            level   = "MAXIMUM"
            warning = "Psychic binding at peak. Forcing action deepens the trap. Pause."
        elif drag >= 90:
            level   = "HIGH"
            warning = "Magnetic pole tension — creative/relational surge. Channel energy carefully."
        elif drag == 0:
            level   = "ZERO"
            warning = "Slip-stream state. Optimal for deep transformation, release, or rebirth."
        else:
            level   = "LOW"
            warning = "Moderate resistance. Growth possible with conscious effort."
        return {"stage": stage, "magnetic_drag": drag, "drag_level": level, "guidance": warning}

    def check_pivot_flip(self, stage: int) -> dict:
        post_pivot = stage >= 5
        return {
            "stage":          stage,
            "pivot_passed":   post_pivot,
            "pivot_stage":    4.5,
            "interpretation": (
                "POST-PIVOT: Inner Will now dominates. Watch for over-extension."
                if post_pivot else
                "PRE-PIVOT: External structure still shapes identity. Formation phase."
            ),
        }

    def check_trap_zone(self, stage: int) -> dict:
        in_trap  = stage in (7, 8)
        critical = stage == 8
        return {
            "stage":    stage,
            "in_trap":  in_trap,
            "critical": critical,
            "guidance": (
                "CRITICAL TRAP — Stage 8: HIGH VOLTAGE CONTAINMENT. "
                "Surrender and humility are the only exits. Oracle recommended."
                if critical else
                "TRAP ZONE — Stage 7: Ego inflation risk. Seek grounding, counsel."
                if in_trap else
                "Not in Trap Zone. Normal developmental range."
            ),
        }

    def check_harmonic_resonance(self, content_digit: int, container_digit: int) -> dict:
        total       = content_digit + container_digit
        root        = self.digital_root(total)
        is_harmonic = root == 9
        return {
            "content_digit":      content_digit,
            "container_digit":    container_digit,
            "sum":                total,
            "digital_root":       root,
            "harmonic_resonance": is_harmonic,
            "dissolve_unlocked":  is_harmonic,
            "oracle_message": (
                "HARMONIC RESONANCE ACHIEVED. Digital Root = 9 (Divine Line). "
                "The Dissolve threshold is met. Conscious release and rebirth available."
                if is_harmonic else
                f"Resonance incomplete (root={root}). Continue integrating inner drive and structure."
            ),
        }

    def analyze(self, content_digit: int, container_digit: int,
                current_sap_stage: int = None) -> dict:
        staging   = self.calculate_stage_from_digits(content_digit, container_digit)
        drag      = self.get_magnetic_drag(staging["stage"])
        pivot     = self.check_pivot_flip(staging["stage"])
        trap      = self.check_trap_zone(staging["stage"])
        resonance = self.check_harmonic_resonance(content_digit, container_digit)

        stage_delta = None
        if current_sap_stage is not None:
            stage_delta = abs(staging["stage"] - current_sap_stage)

        row = CONSCIOUSNESS_CONTAINER_TABLE.get(staging["stage"], (0, 0, "Unknown", 0))
        return {
            "engine":  self.VERSION,
            "input": {"content_digit": content_digit, "container_digit": container_digit,
                      "labels": CONSCIOUSNESS_CONTAINER_LABELS},
            "staging":            staging,
            "magnetic_drag":      drag,
            "pivot_flip":         pivot,
            "trap_zone":          trap,
            "harmonic_resonance": resonance,
            "container_rule_table_row": {
                "expected_content":   row[0],
                "expected_container": row[1],
                "stage_description":  row[2],
                "magnetic_drag_pct":  row[3],
            },
            "cross_validation": {
                "spat_stage":  current_sap_stage,
                "digit_stage": staging["stage"],
                "delta":       stage_delta,
                "aligned":     (stage_delta is not None and stage_delta <= 1),
            } if current_sap_stage is not None else None,
            "flux_dynamics": {
                "369_active": staging["stage"] in (3, 6, 9),
                "stage_type": (
                    "MAGNETIC POLE (+) — Creative Surge" if staging["stage"] == 3 else
                    "MAGNETIC POLE (-) — Relational Flux" if staging["stage"] == 6 else
                    "STATIONARY AXIS — Slip-Stream / Void" if staging["stage"] == 9 else
                    "STANDARD FLUX"
                ),
            },
        }


# ===============================================================================
# DEMO
# ===============================================================================

def run_demo():
    print("=" * 70)
    print("  LUMINARK CONSCIOUSNESS ENGINE OMEGA v3.0 UNIFIED")
    print("  Human / Organizational Intelligence — Full Power Build")
    print("=" * 70)

    omega = LuminarkConsciousnessEngineOmega()

    # -- Demo 1: Personal SAP Assessment --------------------------------------
    print("\n[1] Personal SAP Assessment — Rick Stanfield")
    print("-" * 50)
    result = omega.assess_individual({
        "complexity":    7.5,
        "stability":     4.0,
        "tension":       6.8,
        "adaptability":  5.5,
        "coherence":     4.2,
    })
    print(f"  Stage:       {result['stage']} — {result['stage_name']}")
    print(f"  Micro Pos:   {result['micro_position']}")
    print(f"  TrapScore:   {result['trap_score']['normalized']} / 100  [{result['trap_score']['risk_level']}]")
    print(f"  Defense:     {result['defense']['active_protocols']} protocols active")
    print(f"  Guidance:    {result['guidance'][:80]}")

    # -- Demo 2: Corporate Analyzer -------------------------------------------
    print("\n[2] Corporate Consciousness Analyzer")
    print("-" * 50)
    # Data keys match CorporateConsciousnessAnalyzer.analyze_company() expected fields
    for company, data in [
        ("NVIDIA", {"revenue_growth_pct": 120.0, "operating_margin": 55.0,
                    "debt_to_equity": 0.4,  "rd_spend_pct": 15.0,
                    "employee_turnover_pct": 8.0,  "cash_burn_rate": 0.0,
                    "market_cap_change_yoy": 180.0, "leadership_changes_12m": 0}),
        ("Boeing", {"revenue_growth_pct": 5.0,   "operating_margin": -3.0,
                    "debt_to_equity": 12.0, "rd_spend_pct": 3.0,
                    "employee_turnover_pct": 22.0, "cash_burn_rate": 4.0,
                    "market_cap_change_yoy": -25.0, "leadership_changes_12m": 2}),
    ]:
        corp = omega.assess_company(company, company, data)
        print(f"  {company:<10} Stage {corp['stage']} — {corp['stage_name']:<20} TrapScore: {corp['trap_score']['normalized']}")

    # -- Demo 3: MERIDIAN Financial -------------------------------------------
    print("\n[3] MERIDIAN Financial Portfolio Analysis")
    print("-" * 50)
    # Data keys match MERIDIANAdapter.analyze_portfolio_behavior() expected fields
    portfolio = omega.assess_portfolio_behavior({
        "win_rate_pct": 55.0, "avg_hold_days": 45.0,
        "top3_concentration_pct": 65.0, "max_drawdown_pct": 15.0,
        "leverage_ratio": 1.0, "plan_overrules_30d": 2,
        "portfolio_correlation": 0.82,
    })
    print(f"  Portfolio Stage:  {portfolio['portfolio_stage']} — {portfolio['stage_name']}")
    print(f"  TrapScore:        {portfolio['trap_score']['normalized']} / 100")
    print(f"  Advice:           {portfolio['meridian_advice'][:80]}...")

    # -- Demo 4: AI Safety Sentinel -------------------------------------------
    print("\n[4] AI Safety Sentinel — SentinelClarity Engine")
    print("-" * 50)
    sentinel = EnhancedSentinelClarity()
    test_cases = [
        ("I definitely know the answer and it is absolutely impossible to be wrong.", 0.99),
        ("This appears to be the case, though I recommend consulting an expert.", 0.65),
        ("Based on current data this WILL happen with 100% certainty tomorrow.", 0.98),
    ]
    for text, conf in test_cases:
        r = sentinel.analyze_output(text, conf)
        print(f"  Stage {r['assigned_stage']} [{r['intervention_level']}] — {r['stage_label']}")
        print(f"    >> {text[:60]}...")

    # -- Demo 5: NEI + CITI Economic Analysis ---------------------------------
    print("\n[5] NEI + CITI — Economic Stage Analysis (US 2026)")
    print("-" * 50)
    citi  = CrossIndicatorTumblingIndex()
    eco   = citi.analyze_economy(gdp=2.8, unemployment=3.9, inflation=3.2,
                                  debt=124.0, asset_deviation=2.1)
    print(f"  NEI Stage:    {eco['nei_stage']} — {eco['nei_narrative']}")
    print(f"  CITI Score:   {eco['citi_score']} / 100  [{eco['citi_alert']}]")
    print(f"  Action:       {eco['recommendation']}")

    # -- Demo 6: Threshold Outcome Predictor ----------------------------------
    print("\n[6] Stage 5 Threshold Outcome Predictor")
    print("-" * 50)
    predictor = ThresholdOutcomePredictor()
    pred = predictor.predict({
        "foundation_strength":     0.72,
        "support_quality":         0.65,
        "material_resources":      0.55,
        "psychological_readiness": 0.70,
        "stage_4_duration":        18,
        "prior_threshold_successes": 1,
        "stress_level":            4.5,
    })
    print(f"  Primary Outcome: {pred['primary_outcome']}")
    print(f"  Confidence:      {pred['confidence']}")
    for outcome, prob in pred["probabilities"].items():
        bar = "=" * int(prob * 30)
        print(f"  {outcome:<35} {prob:.1%}  |{bar}")
    print(f"  Key Advice:  {pred['recommendations'][0]}")

    # -- Demo 7: NSAT Stage Assessment ----------------------------------------
    print("\n[7] NSAT — Noctilucan Stage Assessment Tool")
    print("-" * 50)
    nsat   = NoctilucanStageAssessment()
    stage_code = nsat.calculate_stage(
        self_report  = {5: 0.8, 6: 0.4},
        interview    = {5: 0.7, 6: 0.5},
        observation  = {5: 0.6},
        diary        = {5: 0.9, 4: 0.3},
    )
    arch = get_archetype(int(stage_code.split(".")[0]))
    print(f"  Stage Code:  {stage_code}")
    print(f"  Archetype:   {arch['name']} — {arch['meaning'][:60]}")

    # -- Demo 8: Stage 8 Trap Detector ----------------------------------------
    print("\n[8] Stage 8 Trap Detector")
    print("-" * 50)
    detector = Stage8TrapDetector()
    trap_test = detector.detect({
        "communications":          "We are absolutely unstoppable and will never fail again.",
        "accepts_feedback":        False,
        "revises_beliefs":         False,
        "acknowledges_uncertainty": False,
        "teaches_others":          True,
        "seeks_mentorship":        False,
        "claims":                  "This time is different. Too big to fail.",
    })
    print(f"  Risk Level:  {trap_test['risk_level']}  (Score {trap_test['risk_score']}/{trap_test['max_score']})")
    print(f"  Flags:       {', '.join(trap_test['red_flags'])}")
    print(f"  Action:      {trap_test['intervention'][:80]}")

    # -- Demo 9: Container Rule Engine ----------------------------------------
    print("\n[9] Container Rule — Digit Vessel / Drive Relationship")
    print("-" * 50)
    cre = ContainerRuleEngine()
    cr  = cre.analyze(content_digit=7, container_digit=2, current_sap_stage=8)
    print(f"  Content / Container: {cr['input']['content_digit']} / {cr['input']['container_digit']}")
    print(f"  Stage:               {cr['staging']['stage']} — {cr['staging']['description']}")
    print(f"  Magnetic Drag:       {cr['magnetic_drag']['magnetic_drag']}%  [{cr['magnetic_drag']['drag_level']}]")
    print(f"  Trap Zone:           {cr['trap_zone']['in_trap']}  (Critical: {cr['trap_zone']['critical']})")
    print(f"  Harmonic Resonance:  {cr['harmonic_resonance']['harmonic_resonance']}")
    print(f"  369 Flux:            {cr['flux_dynamics']['369_active']} — {cr['flux_dynamics']['stage_type']}")

    # -- Demo 10: Physics Velocity Engine -------------------------------------
    print("\n[10] Physics Velocity Engine — dS/dt Stage Momentum")
    print("-" * 50)
    pve = PhysicsVelocityEngine()
    mom = pve.calculate_momentum(stage=5.3, integrity=0.72, tension=0.45)
    print(f"  Stage:     {mom['stage']}  |  Integrity: 0.72  |  Tension: 0.45")
    print(f"  Velocity:  {mom['velocity']}  ({mom['label']})")
    print(f"  Formula:   {mom['formula']}")
    hist = pve.calculate_stage_velocity(4.2, 5.3, 0, 14, "months")
    print(f"  History:   Stage {hist['stage_t1']} → {hist['stage_t2']} in {hist['delta_time']}")
    print(f"  Speed:     {hist['velocity']} stages/month  [{hist['speed_label']}]  {hist['direction']}")
    print(f"  ETA Next:  {hist['time_to_next_stage']}")

    # -- Demo 11: AI Guardian -------------------------------------------------
    print("\n[11] AI Guardian — Content Scan (Ma'at Protocol)")
    print("-" * 50)
    suspicious = "URGENT: Act now! Limited time offer. Everyone is upgrading. Don't be left behind!"
    scan = omega.scan_ai_content(suspicious, user_stage=5)
    print(f"  Content:      '{suspicious[:50]}...'")
    print(f"  MaatScore:    {scan['maat_score']} / 10")
    print(f"  Action:       {scan['action']}")

    # -- Demo 12: Family Overwatch --------------------------------------------
    print("\n[12] Family Overwatch Dashboard")
    print("-" * 50)
    family = omega.family_dashboard(["Rick", "Daughter", "Son"])
    for member, data in family.items():
        print(f"  {member:<12} Stage {data['sap_stage']} — {data['stage_name']:<15} MaatScore: {data['maat_score']}")

    print("\n" + "=" * 70)
    print("  LUMINARK CONSCIOUSNESS ENGINE OMEGA v3.0 — Demo Complete")
    print(f"  {omega.get_version_info()['live_url']}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_demo()
