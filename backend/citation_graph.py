def build_citation_graph(papers):
    return {p.paper_id: p.references for p in papers}
