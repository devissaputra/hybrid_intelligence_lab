# Calculation guide

## Question and evidence

When does confidence-based routing help?

Synthetic human and AI decisions; confidence is generated partly from correctness.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Keep agreement; default to human for small confidence gaps; otherwise select the more confident source.

## Calculation and interpretation

`Complementarity = mean(human_correct XOR AI_correct).`

The generator makes confidence informative about correctness by construction, which can produce optimistic hybrid gains. Override gain counts rescued AI errors, not net improvement after newly introduced errors; deferral means human default, not abstention.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| human_accuracy | 0.68 | unitless | `human_accuracy` |
| ai_accuracy | 0.707 | unitless | `ai_accuracy` |
| hybrid_accuracy | 0.895 | unitless | `hybrid_accuracy` |
| complementarity_rate | 0.407 | unitless | `complementarity_rate` |
| override_gain | 0.19 | unitless | `override_gain` |
| deferral_rate | 0.01 | unitless | `deferral_rate` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This simulator compares human-only, AI-only, and confidence-routed decisions, retaining each routing reason for error inspection. The synthetic generator deliberately links confidence to correctness, so strong hybrid performance reflects that assumption and must not be presented as evidence from a human study. Threshold sweeps reveal how often the policy defaults to the human and when complementary errors can be used.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/hybrid_intelligence_lab/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`route_decision`](src/hybrid_intelligence_lab/core.py#L8) | Inspect the explicit implementation and its callers. |
| [`evaluate`](src/hybrid_intelligence_lab/core.py#L13) | Inspect the explicit implementation and its callers. |
| [`threshold_sweep`](src/hybrid_intelligence_lab/core.py#L24) | Inspect the explicit implementation and its callers. |
| [`make_decisions`](src/hybrid_intelligence_lab/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

The generator makes confidence informative about correctness by construction, which can produce optimistic hybrid gains. Override gain counts rescued AI errors, not net improvement after newly introduced errors; deferral means human default, not abstention. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
