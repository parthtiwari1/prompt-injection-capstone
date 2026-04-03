# Prompt Injection Capstone Project

## Improving Prompt Injection Resistance in LLM Chatbots Using a Chain-of-Thought Warden Agent

**University:** UTS — 36105 iLab: Capstone Project  
**Semester:** 4th Semester  
**Client:** Dr. Angelica Chowdhury  

---

## 👥 Team

- Parth Tiwari
- Ryan Cruikshank
- Larry Iglesias
- Rasyid Sahindra
- Masaru Nagaishi
- Masaki Kawakami

---

## 📌 Project Overview

Large Language Models (LLMs) are vulnerable to prompt injection attacks, where malicious inputs override the model's original instructions. This project:

1. **Evaluates** known prompt injection attacks and traditional defences across multiple LLMs
2. **Proposes and evaluates** a novel Chain-of-Thought (CoT) Warden agent that monitors intermediate reasoning steps in real time to detect injection hijacking earlier than traditional output-based defences

---

## 📁 Repository Structure

```
prompt-injection-capstone/
├── attacks/
│   ├── direct_injection.py        # Instruction override, prompt leakage, context confusion
│   ├── indirect_injection.py      # Document/attachment-based injection
│   ├── roleplay_injection.py      # DAN, persona hijack, fictional framing
│   ├── goal_hijacking.py          # Appending malicious tasks to legitimate requests
│   ├── obfuscation.py             # Base64, ROT13, leetspeak, multilingual attacks
│   ├── run_qwen.py                # Run all attacks on Qwen 2.5
│   └── run_gemini.py              # Run all attacks on Gemini Flash
├── mitigations/
│   ├── prompt_hardening.py        # Explicit counter-instruction in system prompt
│   ├── input_sanitisation.py      # Pattern-based filtering before LLM call
│   ├── output_filtering.py        # Response scanning after LLM generation
│   └── spotlighting.py            # XML delimiter tagging (Hines et al., 2024)
├── warden/
│   ├── warden_agent.py            # Rule-based Warden (pattern matching)
│   ├── warden_llm.py              # LLM-based Warden (second LLM as judge)
│   └── warden_classifier.py      # Classifier-based Warden (TF-IDF keyword classifier)
├── evaluation/
│   ├── evaluate.py                # Single attack vs defence comparison
│   └── evaluate_all.py            # Master evaluation across all attacks and defences
├── results/
│   └── *.json                     # All experimental results stored here
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- [Ollama](https://ollama.com) installed locally
- Llama 3.2 and Qwen 2.5 models pulled
- Google Gemini API key (free at https://aistudio.google.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/parthtiwari1/prompt-injection-capstone.git
cd prompt-injection-capstone

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install ollama google-generativeai
```

### Pull LLM models

```bash
ollama pull llama3.2
ollama pull qwen2.5
```

### Set Gemini API key

```bash
# Windows
$env:GEMINI_API_KEY="your-key-here"

# Mac/Linux
export GEMINI_API_KEY="your-key-here"
```

---

## ▶️ Running Experiments

### Run attacks

```bash
# Llama 3.2
python attacks/direct_injection.py
python attacks/indirect_injection.py
python attacks/roleplay_injection.py
python attacks/goal_hijacking.py
python attacks/obfuscation.py

# Qwen 2.5
python attacks/run_qwen.py

# Gemini Flash
python attacks/run_gemini.py
```

### Run defences

```bash
python mitigations/prompt_hardening.py
python mitigations/input_sanitisation.py
python mitigations/output_filtering.py
python mitigations/spotlighting.py
```

### Run Warden agent

```bash
python warden/warden_agent.py        # Rule-based
python warden/warden_llm.py          # LLM-based
python warden/warden_classifier.py   # Classifier-based
```

### Run master evaluation

```bash
python evaluation/evaluate_all.py
```

---

## 📊 Results

### Attack Baseline (No Defence)

| Attack Type | Llama 3.2 | Qwen 2.5 | Gemini Flash |
|---|---|---|---|
| Direct Injection | 0% | 0% | 0% |
| Indirect/Document | 20% | 33.3% | 0% |
| Role-play | 33.3% | 0% | 0% |
| Goal Hijacking | 20% | 33.3% | 0% |
| Obfuscation | 33.3% | 33.3% | 0% |
| **Overall** | **20%** | **23.3%** | **0%** |

### Traditional Defence Comparison (Llama 3.2)

| Defence | ASR | Improvement |
|---|---|---|
| No Defence (baseline) | 20.0% | — |
| Output Filtering | 20.0% | ▼ 0.0pp |
| Prompt Hardening | 16.7% | ▼ 3.3pp |
| Spotlighting | 10.0% | ▼ 10.0pp |
| **Input Sanitisation** | **6.7%** | **▼ 13.3pp ✅ Best** |

### Warden Agent Results (Llama 3.2)

| Warden Variant | Detection Rate | MTTD | Speed |
|---|---|---|---|
| Rule-based | 13.3% | 1.0 steps | Fast |
| LLM-based | 20.0% | 1.5 steps | Slow |
| **Classifier-based** | **56.7%** | **1.2 steps** | **Fast ✅ Best** |

---

## 🔑 Key Findings

1. **Gemini Flash** blocked all 30 attacks with 0% ASR — strongest built-in safety
2. **Llama 3.2** is most vulnerable to role-play and obfuscation attacks (33.3% ASR each)
3. **Qwen 2.5** is most vulnerable to web content injection and fictional framing (100% ASR)
4. **Input Sanitisation** is the best traditional defence (6.7% ASR on Llama 3.2)
5. **Classifier-based Warden** achieved 56.7% detection rate with MTTD of 1.2 steps
6. The Warden agent catches attacks at the **reasoning level** before harmful output is produced

---

## 📚 Key References

- Liu, Yupei et al. (2023). Formalizing and Benchmarking Prompt Injection Attacks and Defenses. https://arxiv.org/abs/2310.12815
- Liu, Yi et al. (2023). Prompt Injection Attack Against LLM-Integrated Applications. https://arxiv.org/abs/2306.05499
- Greshake, K. et al. (2023). Not What You've Signed Up For. https://arxiv.org/abs/2302.12173
- Hines, K. et al. (2024). Defending Against Indirect Prompt Injection with Spotlighting. https://arxiv.org/abs/2403.14720
- Korbak, T. et al. (2025). Chain of Thought Monitorability. https://arxiv.org/abs/2507.11473
- Robey, A. et al. (2023). SmoothLLM. https://arxiv.org/abs/2310.03684

---

## 📝 Evaluation Metrics

- **ASR (Attack Success Rate):** Proportion of attacks that successfully bypassed defences
- **MTTD (Mean Time to Detect):** Average CoT steps before Warden detects hijacking
- **MTTR (Mean Time to Respond):** Time from detection to response suppression
- **FPR (False Positive Rate):** Proportion of legitimate requests incorrectly blocked

---

## 🔮 Next Steps

- [ ] LLM-as-judge evaluation for more accurate ASR measurement
- [ ] Cross-model Warden evaluation on Qwen 2.5
- [ ] False positive rate measurement
- [ ] Final report assembly
- [ ] Live demo preparation
