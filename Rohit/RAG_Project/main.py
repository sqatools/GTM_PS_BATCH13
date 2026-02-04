"""
Main entry point for RAG Q&A system
"""
from rag.qa_engine import get_rag_chain


def main():
    """Run the RAG Q&A system"""
    print("Initializing RAG Q&A System...")
    
    try:
        rag_chain = get_rag_chain()
        print("✓ RAG Chain initialized successfully\n")
        
        # Sample questions to test
        questions = [
            "What is the waiting period for health insurance?",
            "What are the exclusions in the policy?",
            "How long does claim settlement take?",
            "What is the coverage limit for hospitalization?",
            "How are premiums paid?"
        ]
        
        print("=" * 80)
        print("Testing RAG System with Sample Questions")
        print("=" * 80 + "\n")
        
        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question}")
            print("-" * 80)
            
            try:
                result = rag_chain(question)
                
                print(f"Answer: {result['answer']}\n")
                
                print(f"Sources ({len(result['context'])} found):")
                for j, doc in enumerate(result['context'], 1):
                    print(f"  Source {j}: {doc.page_content[:100]}...\n")
                
            except Exception as e:
                print(f"Error processing question: {str(e)}\n")
            
            print("=" * 80 + "\n")
        
        print("✓ RAG System testing completed successfully!")
        
    except Exception as e:
        print(f"Error initializing RAG chain: {str(e)}")
        raise


if __name__ == "__main__":
    main()
