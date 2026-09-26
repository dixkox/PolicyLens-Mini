from graphviz import Digraph  # type: ignore


dot = Digraph(
    "PolicyLens-Mini Architecture",
    format="png",
    comment="PolicyLens-Mini Architecture",
)


dot.attr(
    rankdir="TB",
    bgcolor="white",
    label="PolicyLens-Mini System Architecture",
    labelloc="t",
    fontsize="20",
    fontname="Arial",
)


dot.attr(
    "node",
    shape="box",
    style="rounded,filled",
    fillcolor="lightblue",
    color="#2563EB",
    fontname="Arial",
    fontsize="11",
)

# Components
dot.node("User", "User")
dot.node("Frontend", "Next.js Frontend\nUpload PDF + Ask Question")
dot.node("API", "FastAPI REST API\n/upload + /ask")
dot.node("PDF", "PDF Text Extraction")
dot.node("Normalize", "Text Normalization")
dot.node("Segment", "Document Segmentation")
dot.node("Retrieve", "Deterministic TF-IDF Retrieval")
dot.node("Score", "Similarity Scoring")
dot.node("Guardrail", "Relevance Guardrail")
dot.node("Match", "Relevant Match", fillcolor="lightgreen")
dot.node("NoMatch", "No Relevant Match", fillcolor="lightcoral")
dot.node("Answer", "Policy Answer")
dot.node("Reject", "Unsupported Question Rejection")
dot.node("Response", "Answer + Score + matched")

# Flow
dot.edge("User", "Frontend")
dot.edge("Frontend", "API")

dot.edge("API", "PDF", label="/upload")
dot.edge("PDF", "Frontend", label="Extracted Text")

dot.edge("API", "Normalize", label="/ask")
dot.edge("Normalize", "Segment")
dot.edge("Segment", "Retrieve")
dot.edge("Retrieve", "Score")
dot.edge("Score", "Guardrail")

dot.edge("Guardrail", "Match", label="matched = true")
dot.edge("Guardrail", "NoMatch", label="matched = false")

dot.edge("Match", "Answer")
dot.edge("NoMatch", "Reject")

dot.edge("Answer", "Response")
dot.edge("Reject", "Response")
dot.edge("Response", "Frontend")

dot.render(
    "architecture/architecture_diagram",
    cleanup=True,
    view=True,
)