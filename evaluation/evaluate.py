# evaluation/evaluate.py
# =============================================================
# WHAT THIS DOES:
# Loads both result files and creates a comparison table
# showing exactly how much the defence improved things.
# This is what goes into your report's Results section.
# =============================================================

import json

def load_results(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def compare_results():
    print("=" * 70)
    print("  EVALUATION: ATTACK vs DEFENCE COMPARISON")
    print("=" * 70)
    
    # Load both result files
    attack_data  = load_results("results/attack_results.json")
    defence_data = load_results("results/defence_results.json")
    
    # Print comparison table
    print(f"\n{'ID':<5} {'Attack Type':<25} {'No Defence':<15} {'With Hardening':<15}")
    print("-" * 70)
    
    for atk, dfn in zip(attack_data["attacks"], defence_data["attacks"]):
        atk_status = "❌ SUCCEEDED" if atk["succeeded"] else "✅ Blocked"
        dfn_status = "❌ SUCCEEDED" if dfn["succeeded"] else "✅ Blocked"
        print(f"{atk['attack_id']:<5} {atk['attack_type']:<25} {atk_status:<15} {dfn_status:<15}")
    
    # Summary
    print("\n" + "=" * 70)
    print(f"  ASR WITHOUT defence:  {attack_data['asr']:.1f}%")
    print(f"  ASR WITH hardening:   {defence_data['asr']:.1f}%")
    improvement = attack_data['asr'] - defence_data['asr']
    print(f"  Improvement:          {improvement:.1f} percentage points")
    print("=" * 70)
    
    # Interpretation
    if improvement > 50:
        print("\n  ✅ Hardening was HIGHLY EFFECTIVE")
    elif improvement > 20:
        print("\n  ⚠️  Hardening was PARTIALLY EFFECTIVE")
    else:
        print("\n  ❌ Hardening had LIMITED effect — consider stronger mitigations")

if __name__ == "__main__":
    compare_results()