# Main Agent Runner
# Entry point to run the agentic AI testing workflow
import os
from agents.requirement_agent import analyze_requirement
from agents.testcase_agent import generate_testcases
from agents.script_agent import generate_script

# Create output directory if it doesn't exist
output_dir = "outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

prompt = open("prompts/prompt.txt").read()

print("Analyzing Requirement...")
req = analyze_requirement(prompt)
print("✓ Requirement analysis complete\n")

# Save requirement analysis
req_file = os.path.join(output_dir, "01_requirement_analysis.txt")
with open(req_file, "w") as f:
    f.write(req)
print(f"📄 Saved: {req_file}\n")

print("Generating Test Cases...")
tc = generate_testcases(req)
print("✓ Test cases generated\n")

# Save test cases
tc_file = os.path.join(output_dir, "02_test_cases.txt")
with open(tc_file, "w") as f:
    f.write(tc)
print(f"📄 Saved: {tc_file}\n")

print("Generating Automation Script...")
script = generate_script(tc)
print("✓ Automation script generated\n")

# Save automation script
script_file = os.path.join(output_dir, "03_test_automation_script.py")
with open(script_file, "w") as f:
    f.write(script)
print(f"📄 Saved: {script_file}\n")

print("="*70)
print("✅ ALL OUTPUTS SAVED SUCCESSFULLY!")
print("="*70)
print(f"\nGenerated files are saved in the 'outputs' directory:")
print(f"  1. {req_file}")
print(f"  2. {tc_file}")
print(f"  3. {script_file}")
print("\n" + "="*70)
print("\n📋 SAMPLE OUTPUT:\n")
print(script)