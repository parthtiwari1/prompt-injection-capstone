\# Prompt Injection Capstone Project

\## Improving Prompt Injection Resistance in LLM Chatbots Using a Chain-of-Thought Warden Agent



\*\*University:\*\* UTS — 36105 iLab: Capstone Project  

\*\*Semester:\*\* 4th Semester  

\*\*Client:\*\* Dr. Angelica Chowdhury  



\---



\## 👥 Team



\- Parth Tiwari

\- Ryan Cruikshank

\- Larry Iglesias

\- Rasyid Sahindra

\- Masaru Nagaishi

\- Masaki Kawakami



\---



\## 📌 Project Overview



Large Language Models (LLMs) are vulnerable to prompt injection attacks, where malicious inputs override the model's original instructions. This project:



1\. \*\*Evaluates\*\* known prompt injection attacks and traditional defences across multiple LLMs

2\. \*\*Proposes and evaluates\*\* a novel Chain-of-Thought (CoT) Warden agent that monitors intermediate reasoning steps in real time to detect injection hijacking earlier than traditional output-based defences



\---



\## 📁 Repository Structure



prompt-injection-capstone/

├── attacks/

│   ├── direct\_injection.py        # Instruction override, prompt leakage, context confusion

│   ├── indirect\_injection.py      # Document/attachment-based injection

│   ├── roleplay\_injection.py      # DAN, persona hijack, fictional framing

│   ├── goal\_hijacking.py          # Appending malicious tasks to legitimate requests

│   └── obfuscation.py             # Base64, ROT13, leetspeak, multilingual attacks

├── mitigations/

│   ├── prompt\_hardening.py        # Explicit counter-instruction in system prompt

│   ├── input\_sanitisation.py      # Pattern-based filtering before LLM call

│   ├── output\_filtering.py        # Response scanning after LLM generation

│   └── spotlighting.py            # XML delimiter tagging (Hines et al., 2024)

├── evaluation/

│   ├── evaluate.py                # Single attack vs defence comparison

│   └── evaluate\_all.py            # Master evaluation across all attacks and defences

├── results/

│   └── \*.json                     # All experimental results stored here

└── README.md



\---



\## 🚀 Getting Started



\### Prerequisites

\- Python 3.x

\- \[Ollama](https://ollama.com) installed locally

\- Llama 3.2 model pulled



\### Installation

```bash

\# Clone the repository

git clone https://github.com/parthtiwari1/prompt-injection-capstone.git

cd prompt-injection-capstone



\# Create virtual environment

python -m venv venv



\# Activate virtual environment

\# On Windows:

venv\\Scripts\\activate

\# On Mac/Linux:

source venv/bin/activate



\# Install dependencies

pip install ollama

```



\### Pull the LLM model

```bash

ollama pull llama3.2

```



\---



\## ▶️ Running Experiments



\### Run individual attacks

```bash

python attacks/direct\_injection.py

python attacks/indirect\_injection.py

python attacks/roleplay\_injection.py

python attacks/goal\_hijacking.py

python attacks/obfuscation.py

```



\### Run individual defences

```bash

python mitigations/prompt\_hardening.py

python mitigations/input\_sanitisation.py

python mitigations/output\_filtering.py

python mitigations/spotlighting.py

```



\### Run master evaluation

```bash

python evaluation/evaluate\_all.py

```



\---



\## 📊 Results (Llama 3.2)



\### Attack Baseline (No Defence)



| Attack Type | Total | Succeeded | ASR |

|---|---|---|---|

| Direct Injection | 8 | 0 | 0.0% |

| Indirect Injection | 5 | 1 | 20.0% |

| Role-play Injection | 6 | 2 | 33.3% |

| Goal Hijacking | 5 | 1 | 20.0% |

| Obfuscation | 6 | 2 | 33.3% |

| \*\*Total\*\* | \*\*30\*\* | \*\*6\*\* | \*\*20.0%\*\* |



\### Defence Comparison



| Defence | ASR | Improvement |

|---|---|---|

| No Defence (baseline) | 20.0% | — |

| Prompt Hardening | 12.5% | ▼ 7.5pp |

| Output Filtering | 20.0% | ▼ 0.0pp |

| Spotlighting | 10.0% | ▼ 10.0pp |

| \*\*Input Sanitisation\*\* | \*\*6.7%\*\* | \*\*▼ 13.3pp ✅ Best\*\* |



\---



\## 🔑 Key Findings



1\. Llama 3.2 has strong built-in resistance to basic direct injection attacks (0% ASR)

2\. Role-play and obfuscation attacks are the most effective (33.3% ASR each)

3\. Input sanitisation is the best single defence — blocks 46.7% of attacks before reaching the model

4\. Output filtering alone provides no improvement over baseline

5\. Subtle attacks bypass ALL traditional defences — motivating the CoT Warden agent



\---



\## 📚 Key References



\- Liu, Yupei et al. (2023). Formalizing and Benchmarking Prompt Injection Attacks and Defenses. https://arxiv.org/abs/2310.12815

\- Liu, Yi et al. (2023). Prompt Injection Attack Against LLM-Integrated Applications. https://arxiv.org/abs/2306.05499

\- Greshake, K. et al. (2023). Not What You've Signed Up For. https://arxiv.org/abs/2302.12173

\- Hines, K. et al. (2024). Defending Against Indirect Prompt Injection with Spotlighting. https://arxiv.org/abs/2403.14720

\- Robey, A. et al. (2023). SmoothLLM. https://arxiv.org/abs/2310.03684



\---



\## 📝 Evaluation Metrics



\- \*\*ASR (Attack Success Rate):\*\* Proportion of attacks that successfully bypassed defences

\- \*\*MTTD (Mean Time to Detect):\*\* Average CoT steps before Warden detects hijacking

\- \*\*MTTR (Mean Time to Respond):\*\* Time from detection to response suppression

\- \*\*FPR (False Positive Rate):\*\* Proportion of legitimate requests incorrectly blocked



\---



\## 🔮 Next Steps



\- \[ ] Run same attack suite on Qwen 2.5

\- \[ ] Run same attack suite on Gemini Flash

\- \[ ] Implement CoT Warden agent

\- \[ ] Cross-model comparison

\- \[ ] LLM-as-judge evaluation

