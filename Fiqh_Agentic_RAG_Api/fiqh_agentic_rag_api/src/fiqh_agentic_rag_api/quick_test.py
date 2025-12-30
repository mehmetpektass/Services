import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.abspath(os.path.join(current_dir, "../../"))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.fiqh_agentic_rag_api.tools import FiqhSearchTool

def quick_test():
    print(f"📍 Working Path: {project_root}")
    print("🧪 Test is Starting...\n")

    try:
        tool = FiqhSearchTool()
        
        question = "{question_here}" 
        print(f"❓ Question: {question}")
        print("⏳ Checking Database...")

        result = tool._run(question)

        print("\n" + "="*40)
        print("📄 Results")
        print("="*40)
        print(result)
        print("="*40)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()