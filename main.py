import pandas as pd
import logging
from agents.research_agent import ResearchAgent
from agents.use_case_generation_agent import UseGenerationAgent
from agents.resource_collection_agent import ResourceCollectionAgent

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    # Initialize Research Agent with the dataset file
    dataset_path = "retail_sales_dataset.csv"  # Ensure this filename is correct
    research_agent = ResearchAgent(dataset_path)

    # Load data and print to confirm it's working
    logging.info("Loading dataset...")
    try:
        research_agent.load_dataset()
        logging.info("Loaded Data:")
        logging.info(f"\n{research_agent.data.head()}")  # Display the first few rows of the dataset
    except FileNotFoundError:
        logging.error(f"Error: The file {dataset_path} was not found.")
        return
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return

    # Validate data
    logging.info(f"Dataset shape: {research_agent.data.shape}")
    logging.info("Missing values:")
    logging.info(research_agent.data.isnull().sum())

    # Use Case Generation Agent
    company_focus = {
        "offerings": ["product optimization", "supply chain management"],
        "focus": ["customer experience", "AI integration"]
    }
    
    logging.info("Generating use cases...")
    use_case_agent = UseGenerationAgent(research_agent.data, company_focus)
    use_cases = use_case_agent.generate_use_cases()
    
    logging.info("Generated use cases:")
    for use_case in use_cases:
        logging.info(f"- {use_case}")

if __name__ == "__main__":
    main()
