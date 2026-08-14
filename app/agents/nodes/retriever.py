import logfire
from app.agents.state import AgentState
from app.services.retrieval.qdrant_service import search_enterprise_knowledge
from app.services.retrieval.ranking_service import rerank_documents

def retrieve_node(state: AgentState):
    """
    Performs vector search and semantic reranking for technical queries.
    """
    query = state["current_query"]
    
    
    # Standard Retrieval Logic
    with logfire.span("🔍 Knowledge Retrieval"):
        logfire.info(f"Searching Qdrant for: {query}")
        raw_results = search_enterprise_knowledge(query, limit=15)
        logfire.info(f"Retrieved {len(raw_results)} candidates from Vector DB")

        # Debug: dekh lo actual similarity scores kya aa rahe hain
        for r in raw_results:
            logfire.info(f"Score: {r['score']:.3f} | Source: {r['source']}")

        
        doc_contents = [doc['content'] for doc in raw_results]
        
        with logfire.span("⚖️ Semantic Reranking"):
            reranked_contents = rerank_documents(query, doc_contents, top_n=5)
            logfire.info("Reranking complete. Kept top 5 most relevant chunks.")

        # Source ko wapas map karo reranked content ke against
        formatted_docs = []
        for reranked_text in reranked_contents:
            match = next((r for r in raw_results if r["content"] == reranked_text), None)
            source = match["source"] if match else "Unknown"
            formatted_docs.append(f"[Source: {source}]\nCONTENT: {reranked_text}")
            
        formatted_docs = [f"CONTENT: {doc}" for doc in reranked_contents]
    
    return {
        "documents": formatted_docs,
        "status": f"Found technical context.",
        "plan": state["plan"] + ["Context Retrieved"]
    }