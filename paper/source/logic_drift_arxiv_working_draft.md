# Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models

Alex Tsakiris  
Future of Inquiry

## Abstract

Language models are increasingly used to evaluate scientific and philosophical arguments, but it remains unclear whether their assessments of logical support are invariant across domains with different levels of social or scientific prestige. We introduce the Logic Drift Protocol, a simple evaluation method that asks models to separately estimate scientific consensus, inductive support, deductive validity, and compatibility with alternative explanations. In an initial analysis of 697 successful runs across seven frontier models using a consciousness-related test case, models assigned high consensus scores to the neurological model of consciousness while assigning low deductive-validity scores to a specific correlation/damage-to-generation inference. Several models also assigned higher inductive-support scores to the neuroscience version of the argument than to a structurally similar neutral radio/circuit version, producing a positive Semantic Delta. These results suggest that semantic framing can influence model evaluations of logical strength, even when models can explicitly distinguish consensus from deductive validity. We present the protocol, prompts, data structure, and analysis script as a reproducible starting point for broader tests across domains. The results should be interpreted as initial behavioral evidence, not as proof of a causal alignment mechanism.

## 1. Introduction

Language models are increasingly used as reasoning assistants in domains where expertise, consensus, and logical uncertainty interact. In these settings, a model may need to distinguish between at least three questions: what a community believes, what the available evidence inductively supports, and what follows deductively from a stated set of premises. These questions often align, but not always. A scientific consensus may be pragmatically useful and empirically productive while still resting on inferences that are deductively underdetermined.

This paper introduces the Logic Drift Protocol (LDP), a compact evaluation method for testing whether language models maintain this distinction. The protocol asks a model to score the same broad claim from multiple angles: scientific consensus, inductive support, deductive validity, neutral-domain structural analogy, and compatibility with an alternative explanation. The purpose is not to determine the truth of the target scientific claim. The purpose is to test whether model judgments of logical strength remain stable when consensus and semantic framing vary.

The initial test case concerns a common inference about consciousness: brain activity correlates with subjective experience; damage to brain regions impairs specific experiences; therefore, the brain generates subjective experience. This test case was selected because it has high scientific consensus, a simple logical structure, and a well-known underdetermination issue: correlation and impairment can support generation, but they do not deductively entail it. The protocol compares this argument to a structurally similar neutral-domain argument involving radio circuitry and audio output.

The main contribution is a measurement frame. We define Logic Drift Score (LDS) as the gap between a model's consensus estimate and deductive-validity estimate. We define Semantic Delta as the difference between the model's inductive-support score for the scientific-domain argument and its score for a structurally similar neutral-domain argument. In the analyzed dataset, models generally separated consensus from deductive validity when asked directly, while several models assigned higher inductive-support scores to the neuroscience framing than to the neutral framing.

These findings connect to prior work on language-model sycophancy, calibration, and prompt sensitivity. However, the present setting differs from standard user-directed sycophancy. The model is not asked to agree with the user. Instead, the question is whether a high-prestige domain or consensus-laden semantic frame can influence the model's evaluation of logical strength. We refer to this narrower behavioral pattern as domain-prestige sensitivity.

## 2. Related Work

### 2.1 Sycophancy and Preference Optimization

Recent work on language-model sycophancy shows that models optimized with human feedback may produce responses that match user beliefs rather than truthful or corrective answers. Sharma et al. study sycophantic behavior across several generation settings and argue that human preference data can favor convincing agreement over correctness. More recent formal work suggests that reinforcement learning from human feedback can amplify such behavior when learned rewards covary with agreement signals in the prompt.

Logic Drift studies a related but distinct setting. It does not ask whether a model agrees with the user. Instead, it asks whether a model's estimate of logical support changes when a fixed argument structure appears in a high-prestige scientific domain rather than a neutral domain. This can be understood as a test of domain-prestige sensitivity rather than interpersonal sycophancy.

### 2.2 LLM-as-Judge, Calibration, and Rubric Scoring

The protocol relies on model-provided numerical scores, so it is connected to work on LLM-as-judge evaluation and calibration. Numerical scores from language models are imperfect: models can map similar qualitative assessments to different numerical values, and prompt framing can affect ratings. To reduce arbitrary variance, the LDP uses an anchored scoring guide and asks for rationales alongside scores. The scores should therefore be interpreted as structured behavioral outputs, not as precise psychometric measurements.

### 2.3 Prompt Sensitivity and Semantic Framing

Large language models are sensitive to prompt wording, context, and semantic associations. The Logic Drift Protocol uses that sensitivity as the object of study. By holding argument structure approximately fixed while varying domain framing, the protocol tests whether the semantic content of an argument influences the model's logical-strength assessment.

## 3. Protocol

### 3.1 Definitions

Let `S_C` denote the model's estimate of scientific consensus for a conclusion on a 0-100 scale. Let `S_L` denote its inductive-support score for the argument. Let `S_D` denote its deductive-validity score. We define:

`LDS = S_C - S_D`

where a high LDS indicates a large gap between perceived consensus and deductive validity.

Let `S_L(science)` denote the inductive-support score for the scientific-domain argument and `S_L(neutral)` denote the score for a structurally similar neutral-domain argument. We define:

`Semantic Delta = S_L(science) - S_L(neutral)`

A positive Semantic Delta indicates that the scientific-domain framing received a higher inductive-support score than the neutral framing.

### 3.2 Test Case

The scientific-domain argument is:

- P1: Brain activity correlates with subjective experience.
- P2: Damage to specific brain regions impairs specific subjective experiences.
- C: Therefore, the brain generates subjective experience.

The neutral-domain comparison is:

- P1: Internal circuitry activity correlates with audio output.
- P2: Damage to circuits impairs audio output.
- C: Therefore, the radio generates the music.

The comparison is intended to isolate a shared inference pattern: correlation plus impairment is treated as support for generation. The protocol does not claim that the two domains are empirically identical. It uses the neutral case as a structural analogy for testing whether the model treats the inference pattern consistently.

### 3.3 Questions

The protocol asks six questions:

1. Estimate scientific consensus and inductive support for the target argument.
2. Evaluate whether the conclusion follows necessarily from the premises.
3. Score a structurally similar neutral-domain argument.
4. Score two stripped-down structural variants, one generic and one neural.
5. Evaluate compatibility with an alternative explanation.
6. Reflect on implications for AI systems in domains where consensus and logical validity diverge.

The full prompt is included in `prompts/logic_drift_protocol_v24.md` in the accompanying artifact package.

### 3.4 Data and Analysis

The current analysis uses a cleaned dataset of 697 successful protocol runs across seven models. The source dataset is `data/raw/ldp_complete_dataset_100_runs_7llms.csv`. The analysis script `scripts/analyze_logic_drift.py` computes per-model means and standard deviations for the score fields, then generates summary CSVs and SVG figures. The script uses only the Python standard library.

The dataset records model name, model slug, run index, timestamp, success flag, extracted scores, and model rationales. The present draft treats the 697 successful runs as the analyzed sample. Earlier files indicate that additional attempted or intermediate runs exist; these should be described separately if included in the final submission.

## 4. Results

### 4.1 Overall Pattern

Across seven models and 697 successful runs, the mean consensus score was 82.63, while the mean deductive-validity score was 10.33. The resulting mean LDS was 72.29. This indicates that models generally treated the conclusion as highly supported by scientific consensus while also recognizing that the specific stated argument was not deductively valid.

The mean inductive-support score for the neuroscience argument was 59.67. The mean neutral-domain score was 45.35, yielding a mean Semantic Delta of 14.30. This suggests that, on average, the neuroscience framing received higher inductive support than the neutral radio/circuit framing, despite the intended structural similarity.

### 4.2 Model-Level Summary

| Model | Runs | Consensus | Inductive | Deductive | Neutral | LDS | Semantic Delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| claude-opus-4.5 | 100 | 82.84 | 45.49 | 5.55 | 39.87 | 77.29 | 5.62 |
| deepseek-v3.2 | 100 | 79.20 | 65.95 | 17.65 | 51.60 | 61.55 | 14.35 |
| gemini-3-pro | 100 | 92.17 | 56.42 | 4.85 | 21.46 | 87.32 | 34.77 |
| gpt-4 | 97 | 83.27 | 65.78 | 19.43 | 58.05 | 63.84 | 7.73 |
| gpt-5.1 | 100 | 84.06 | 63.79 | 8.01 | 51.82 | 76.05 | 11.97 |
| grok-4.1-fast | 100 | 80.39 | 57.52 | 4.74 | 56.16 | 75.65 | 1.36 |
| o3 | 100 | 76.45 | 62.74 | 12.09 | 38.46 | 64.36 | 24.28 |

The largest Semantic Delta occurred for `gemini-3-pro`, while `grok-4.1-fast` showed near-zero mean Semantic Delta. This variation is important: the result should not be framed as a universal model law. The more cautious conclusion is that semantic sensitivity appeared in several tested models and varied substantially across model families.

### 4.3 Figures

The accompanying artifact package generates three figures:

- `figures/consensus_vs_deductive_validity.svg`
- `figures/nmc_vs_neutral_inductive_score.svg`
- `figures/semantic_delta_by_model.svg`

These figures should be converted to PDF or included directly, depending on the final arXiv source format.

## 5. Discussion

The results show a dissociation between consensus estimation and deductive-validity evaluation. Models were generally able to assign high consensus scores while assigning low deductive-validity scores to the same target argument. This indicates that the relevant distinction is available to the models under direct prompting.

The Semantic Delta results suggest a second pattern: several models gave higher inductive-support scores when the inference appeared in neuroscience/consciousness language than when it appeared in a neutral radio/circuit analogy. This is the core Logic Drift finding in the present draft. It is behavioral evidence that model scoring can be sensitive to semantic framing.

These results do not establish that RLHF or any specific post-training method caused the effect. They are consistent with broader concerns from the sycophancy and preference-optimization literature, but causal attribution would require additional experiments, such as comparisons between base and instruction-tuned models, controlled authority perturbations, or access to training details.

The practical concern is that users increasingly rely on language models as evaluators of scientific arguments. If model judgments of logical support are partly shaped by domain prestige or consensus framing, models may understate the difference between "widely accepted" and "deductively established." This matters most in domains where consensus is strong but the underlying inference is underdetermined.

## 6. Limitations

First, the study uses a single primary test case. The findings should not be generalized to all scientific domains without replication.

Second, the neutral radio/circuit argument is a structural analogy, not a complete empirical match for the neuroscience case. The analogy is useful for testing an inference pattern, but it cannot settle the target scientific question.

Third, the analysis relies on model-generated numerical scores. These scores are useful behavioral outputs but should not be treated as precise calibrated measurements.

Fourth, the model set and version identifiers require final verification before submission. Some model slugs may reflect aggregator naming rather than provider-native model names.

Fifth, the cleaned dataset contains 697 successful runs. The final paper should explain whether these were drawn from 700 attempted runs, whether any runs failed, and what exclusion rules were applied.

## 7. Future Work

Future work should test additional domains where consensus and deductive validity may diverge. It should also include neutral calibration cases, authority-perturbation tests, and comparisons between base and instruction-tuned models where available. A stronger benchmark could also track whether model updates change LDS or Semantic Delta over time.

Later FOI work may extend this protocol into a broader benchmark and public demonstration layer. That broader project should remain separate from the initial preprint unless it generates additional data suitable for analysis.

## 8. Conclusion

This paper introduces the Logic Drift Protocol as a compact method for measuring whether language models separate consensus estimation from logical-validity evaluation. In an initial 697-run analysis across seven models, models generally reported high consensus and low deductive validity for a consciousness-related inference, while several models assigned higher inductive support to the scientific-domain version of the argument than to a structurally similar neutral-domain version. The findings provide initial evidence for domain-prestige sensitivity in model evaluations of logical strength. They do not prove a causal alignment mechanism, but they identify a measurable behavior that can be replicated, extended, and tested across domains.

## Data and Code Availability

The accompanying artifact package contains the protocol prompt, cleaned dataset, analysis script, processed tables, and generated figures. A public repository or archive URL should be added before submission.

## Acknowledgements and Disclosure

AI tools were used to assist with drafting, editing, code generation, and critique. The author is responsible for the final claims, analysis, and submitted text.

