"""
Main Entry Point for RAG_1 System
Quick start to test the complete RAG pipeline
"""

import os
import sys
from app.rag import RAGPipeline
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """
    Main function to demonstrate RAG_1 system
    """
    try:
        logger.info("=" * 80)
        logger.info("RAG_1 System - Main Entry Point")
        logger.info("=" * 80)
        
        # 1. Check API Key
        if not os.getenv("OPENAI_API_KEY"):
            logger.error("OPENAI_API_KEY not set. Please set it before running.")
            logger.info("Set with: $env:OPENAI_API_KEY = 'sk-...'")
            sys.exit(1)
        
        logger.info("\n✓ OpenAI API Key configured\n")
        
        # 2. Initialize pipeline
        logger.info("Step 1: Initializing RAG Pipeline...")
        pipeline = RAGPipeline(load_existing=False)
        logger.info("✓ Pipeline initialized\n")
        
        # 3. Test connection
        logger.info("Step 2: Testing connections...")
        if pipeline.test_connection():
            logger.info("✓ All components connected\n")
        else:
            logger.warning("⚠ Some components may not be working\n")
        
        # 4. Ingest documents
        logger.info("Step 3: Ingesting documents...")
        logger.info("This will load, chunk, embed, and store documents...")
        try:
            pipeline.ingest_documents()
            logger.info("✓ Documents ingested successfully\n")
        except Exception as e:
            logger.error(f"Error ingesting documents: {str(e)}")
            logger.info("Make sure you have documents in app/data/raw_docs/")
            sys.exit(1)
        
        # 5. Sample queries
        logger.info("Step 4: Testing with sample queries...\n")
        sample_queries = [
            "What is the main topic of the document?",
            "What are the key concepts mentioned?",
            "Summarize the important information.",
        ]
        
        for i, question in enumerate(sample_queries, 1):
            logger.info(f"Query {i}: {question}")
            logger.info("-" * 80)
            
            try:
                result = pipeline.query(question)
                
                logger.info(f"Answer: {result['answer'][:200]}...\n")
                logger.info(f"Retrieved {result['num_docs_retrieved']} documents\n")
                
            except Exception as e:
                logger.error(f"Error processing query: {str(e)}\n")
        
        logger.info("=" * 80)
        logger.info("✓ RAG_1 System Demo Completed Successfully!")
        logger.info("=" * 80)
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
