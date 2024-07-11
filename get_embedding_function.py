from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-west-2"
    # )
    embedder = OllamaEmbeddings(model="nomic-embed-text", temperature=0)

    return embedder
