# agents/resource_collection_agent.py

class ResourceCollectionAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases

    def fetch_datasets(self):
        # Search datasets for each use case
        dataset_links = []
        for use_case in self.use_cases:
            query = use_case["use_case"].replace(" ", "+")
            dataset_links.append(f"https://www.kaggle.com/search?q={query}")
        return dataset_links

# Example usage:
# agent = ResourceCollectionAgent(use_cases)
# datasets = agent.fetch_datasets()
