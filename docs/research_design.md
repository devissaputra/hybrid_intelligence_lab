# Research design

## Project aim

AI-assisted learning decisions are often evaluated by comparing “human” against “model.” This repo makes the more interesting question executable: when do their errors complement one another, and what routing policies preserve human agency while using AI where it adds value?

## Research questions

1. When are human and AI errors complementary rather than redundant?
2. Can confidence-aware routing outperform always-human or always-AI baselines?
3. How much value comes from human override when the two disagree?

## Baseline analytic pipeline

1. Decision simulation
2. Confidence calibration
3. Complementarity analysis
4. Routing policy
5. Policy comparison

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- The simulator is a research harness, not evidence that one routing policy is optimal in classrooms.
- Confidence values are synthetic and should be calibrated in real deployments.
- Human defaulting is modeled as a policy choice, not as a claim that human judgment is always superior.

## Next experiments

- Add cost-sensitive routing and abstention.
- Model expertise-dependent human performance and calibrated AI confidence.
- Run counterbalanced user studies comparing different forms of AI advice and override control.
