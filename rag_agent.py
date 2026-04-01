"""
RAG-Powered Resume Agent — Karim Osman Portfolio
FAISS vector store + sentence-transformers for in-session retrieval
"""

import streamlit as st
import numpy as np
import re

# ==== KNOWLEDGE BASE ====
KARIM_KB = [
    # Identity
    "Karim Osman is a Senior AI Engineer and LLM Architect with 7+ years of experience specializing in RAG systems, LLM orchestration, and production-grade MLOps.",
    "Karim is fluent in Arabic (native), English (C1/C2), Italian (professional), French (professional), and German (intermediate).",
    "Karim is based in Italy and France, having worked with global organizations including Baker Hughes and UniqMaster.",
    "Contact: karim.osman.ai@gmail.com | LinkedIn: linkedin.com/in/karimosman89 | GitHub: github.com/karimosman89",

    # Education
    "Karim completed a Machine Learning Engineering program at Paris 1 Panthéon-Sorbonne University from September 2023 to August 2024.",
    "Karim holds a Master's Degree in Finance from Università di Siena (Italy), completed 2022.",
    "Karim participated in an Erasmus program at Universität Liechtenstein (2019) and an Overseas program at Akita International University, Japan (2020-2021).",

    # Baker Hughes
    "At Baker Hughes (Italy, 2022–present), Karim architected the RAG-as-a-Service platform for 500+ global engineering members.",
    "The Baker Hughes RAG platform achieved 99.9% uptime using blue/green deployments on Kubernetes.",
    "Karim built the 'Chunk-as-a-Service' platform at Baker Hughes, processing 10,000+ engineering documents daily with 95% accuracy.",
    "Karim built the 'LLM-as-a-Service' platform at Baker Hughes enabling teams to query complex technical documentation via natural language.",
    "At Baker Hughes, Karim delivered over €2 million in revenue impact through automation, efficiency gains, and AI-powered workflows.",
    "The RAG system at Baker Hughes reduced document review time by 60% across engineering teams.",
    "Karim's systems at Baker Hughes served 100,000+ daily users across global operations.",
    "At Baker Hughes, Karim implemented YOLO v8 for real-time defect detection in industrial equipment, achieving a 22% boost in defect detection accuracy.",
    "Karim fine-tuned LLMs using LoRA and QLoRA techniques at Baker Hughes for domain-specific engineering tasks.",
    "Karim built multi-modal AI pipelines at Baker Hughes combining NLP, Computer Vision, and structured data analysis.",

    # UniqMaster
    "At UniqMaster (Germany, 2020–2022), Karim led ML engineering projects focused on data pipelines, NLP, and predictive analytics.",
    "At UniqMaster, Karim built automated ETL pipelines processing 50+ data sources using Apache Kafka and Airflow.",
    "At UniqMaster, Karim developed recommendation systems and demand forecasting models deployed on AWS.",

    # Technical Skills — Core AI
    "Karim's core AI skills include LangChain, LlamaIndex, OpenAI API, RAG systems, FAISS, ChromaDB, Pinecone, Weaviate, vector databases.",
    "Karim is expert in Python, TypeScript, Go, C++, Java, SQL, and Bash scripting.",
    "Karim specializes in PyTorch, TensorFlow, JAX, Hugging Face Transformers, ONNX Runtime, TensorRT, and model optimization.",
    "Karim has deep expertise in LLM fine-tuning: LoRA, QLoRA, PEFT, instruction tuning, RLHF, DPO.",
    "Karim's Computer Vision skills: YOLOv8, OpenCV, real-time object detection, edge deployment on NVIDIA Jetson, TensorRT INT8 quantization.",

    # Technical Skills — MLOps & Cloud
    "Karim's MLOps stack: Kubernetes, Docker, Helm, Triton Inference Server, KServe, MLflow, Weights & Biases, Ray, Prometheus/Grafana, Datadog.",
    "Karim is certified and experienced in AWS (SageMaker, Lambda, S3, EKS), Google Cloud (Vertex AI, GCS), and Azure (ML, AKS).",
    "Karim builds CI/CD pipelines for ML using GitHub Actions, ArgoCD, Terraform, and Ansible.",
    "Karim implements feature stores with Feast, data versioning with DVC, and experiment tracking with MLflow.",

    # Technical Skills — Data Engineering
    "Karim's data engineering skills: Apache Spark, Kafka, Airflow, dbt, Snowflake, PostgreSQL, MongoDB, Redis, Elasticsearch.",
    "Karim designs real-time data pipelines handling millions of events per second for AI inference.",
    "Karim implements RAG evaluation frameworks measuring faithfulness, toxicity, bias, and relevance using RAGAS and custom harnesses.",

    # Certifications
    "Karim holds IBM Generative AI Professional Certificate (completed).",
    "Karim holds DeepLearning.AI LLMOps Certificate (completed).",
    "Karim holds Microsoft Azure AI Engineer Associate certificate (completed).",
    "Karim is pursuing AWS Machine Learning Specialty certification (in-progress).",
    "Karim is pursuing Google Cloud Professional Machine Learning Engineer certification (in-progress).",
    "Karim is pursuing Databricks Certified ML Professional (in-progress).",

    # Projects & Impact
    "Karim's Multilingual RAG Assistant achieved 42% ticket deflection, 68% faster resolution, 35% cost reduction, and +12 CSAT points.",
    "Karim's Real-time Edge Vision Inspection system achieved 98.7% recall, 96.2% precision, and cut defect escape rate from 1.8% to 0.3%.",
    "Karim built automated ML platforms that reduced model deployment time from weeks to hours.",
    "Karim published research on cross-lingual embeddings and domain adaptation for technical documentation.",
    "Karim's GitHub profile (karimosman89) contains 30+ repositories covering NLP, Computer Vision, MLOps, and Generative AI.",

    # Philosophy
    "Karim believes in production-first AI: every model must ship with monitoring, evaluation harnesses, and safety guardrails.",
    "Karim's engineering philosophy: measure everything, automate ruthlessly, and always tie AI to business outcomes.",
    "Karim mentors junior engineers and contributes to open-source AI tools.",
]

@st.cache_resource(show_spinner=False)
def build_rag_index():
    """Build FAISS index from knowledge base using sentence-transformers."""
    try:
        from sentence_transformers import SentenceTransformer
        import faiss

        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(KARIM_KB, show_progress_bar=False, normalize_embeddings=True)
        embeddings = np.array(embeddings, dtype=np.float32)

        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)  # Inner product = cosine on normalized vecs
        index.add(embeddings)

        return {"index": index, "model": model, "docs": KARIM_KB, "ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def retrieve_context(query: str, rag_state: dict, top_k: int = 4) -> list[str]:
    """Retrieve top-k relevant KB chunks for a query."""
    if not rag_state.get("ok"):
        return []
    try:
        query_vec = rag_state["model"].encode([query], normalize_embeddings=True)
        query_vec = np.array(query_vec, dtype=np.float32)
        D, I = rag_state["index"].search(query_vec, top_k)
        return [rag_state["docs"][i] for i in I[0] if i < len(rag_state["docs"])]
    except Exception:
        return []


def simple_rag_answer(query: str, context_docs: list[str]) -> str:
    """Rule-based RAG answer synthesizer (no API key required)."""
    context = " ".join(context_docs)
    q_lower = query.lower()

    # Pattern matching for common questions
    if any(w in q_lower for w in ["revenue", "money", "€", "eur", "business impact", "financial"]):
        return ("💰 **Revenue Impact:** Karim delivered **€2M+** in quantified revenue impact at Baker Hughes through "
                "AI-powered automation, RAG systems, and intelligent document processing. This includes direct cost "
                "savings from 60% reduction in document review time and efficiency gains across 500+ global members.")

    if any(w in q_lower for w in ["uptime", "reliability", "sla", "production", "99.9"]):
        return ("⚡ **Production Reliability:** Karim's systems maintain **99.9% uptime** using blue/green "
                "Kubernetes deployments, circuit breakers, health checks, and automated rollback mechanisms. "
                "The RAG-as-a-Service platform at Baker Hughes serves 100,000+ daily users with sub-200ms P95 latency.")

    if any(w in q_lower for w in ["rag", "retrieval", "langchain", "llamaindex", "vector", "faiss", "knowledge"]):
        return ("🔍 **RAG Expertise:** Karim architected the RAG-as-a-Service platform at Baker Hughes for 500+ engineers, "
                "processing **10,000+ documents daily** with 95% accuracy. Tech stack: LangChain/LlamaIndex, FAISS/PGVector, "
                "cross-lingual embeddings, evaluation harnesses (faithfulness, toxicity, bias), prompt versioning, "
                "and safety guardrails. Fine-tuned Llama 3.1 8B on engineering conversation transcripts.")

    if any(w in q_lower for w in ["vision", "yolo", "defect", "computer vision", "detection", "opencv"]):
        return ("👁️ **Computer Vision:** Karim trained custom **YOLOv8** models with targeted augmentations and hard-negative "
                "mining for industrial defect detection, achieving **98.7% recall** and a **22% boost in defect detection**. "
                "Deployed on NVIDIA Jetson with TensorRT INT8 quantization (3.1s cycle time vs 7.5s before). "
                "Defect escape rate cut from 1.8% to 0.3%.")

    if any(w in q_lower for w in ["finetun", "lora", "qlora", "peft", "llm", "gpt", "llama", "training"]):
        return ("🧠 **LLM Fine-tuning:** Karim is an expert in **LoRA/QLoRA** (PEFT) fine-tuning for domain adaptation. "
                "Applied at Baker Hughes to fine-tune Llama 3.1 8B on engineering documentation, "
                "instruction tuning for technical Q&A, and RLHF alignment. Expertise in DPO, PPO, and "
                "efficient training with gradient checkpointing, mixed precision, and quantization.")

    if any(w in q_lower for w in ["skill", "technolog", "stack", "python", "pytorch", "tensorflow", "know"]):
        return ("🛠️ **Tech Stack:** Core AI: Python, PyTorch, TensorFlow, JAX, HuggingFace, LangChain, LlamaIndex, "
                "OpenAI API, FAISS, Pinecone. MLOps: Kubernetes, Docker, Triton, KServe, MLflow, W&B, Ray. "
                "Cloud: AWS (SageMaker, EKS), GCP (Vertex AI), Azure (ML). "
                "Data: Spark, Kafka, Airflow, Snowflake, PostgreSQL, MongoDB.")

    if any(w in q_lower for w in ["certif", "aws", "google", "ibm", "azure", "credential", "course"]):
        return ("📜 **Certifications:** ✅ IBM Generative AI Professional Certificate | ✅ DeepLearning.AI LLMOps | "
                "✅ Microsoft Azure AI Engineer Associate | "
                "🔄 AWS Machine Learning Specialty (in-progress) | "
                "🔄 Google Cloud Professional ML Engineer (in-progress) | "
                "🔄 Databricks Certified ML Professional (in-progress).")

    if any(w in q_lower for w in ["education", "degree", "university", "study", "master", "paris", "sorbonne"]):
        return ("🎓 **Education:** Machine Learning Engineering — Paris 1 Panthéon-Sorbonne University (2023–2024) | "
                "Master of Finance — Università di Siena, Italy (2017–2022) | "
                "Erasmus — Universität Liechtenstein (2019) | "
                "Overseas — Akita International University, Japan (2020-2021).")

    if any(w in q_lower for w in ["experience", "work", "job", "baker hughes", "uniqmaster", "career"]):
        return ("💼 **Experience:** Currently Senior AI Engineer at **Baker Hughes** (Italy, 2022–present) — "
                "architecting RAG-as-a-Service, LLM-as-a-Service, and Computer Vision platforms for 500+ engineers. "
                "Previously ML Engineer at **UniqMaster** (Germany, 2020–2022) — ML pipelines, NLP, and predictive analytics. "
                "€2M+ revenue impact, 99.9% uptime, 100k+ daily users.")

    if any(w in q_lower for w in ["language", "speak", "arabic", "french", "italian", "english", "german", "multilingual"]):
        return ("🌍 **Languages:** Arabic (native) | English (C1/C2 professional) | "
                "Italian (professional, based in Italy) | French (professional, studied in Paris) | German (intermediate). "
                "Karim's multilingual ability enables him to lead AI projects across EMEA and build truly global RAG systems.")

    if any(w in q_lower for w in ["contact", "hire", "reach", "email", "linkedin", "github"]):
        return ("📬 **Contact Karim:** Email: karim.osman.ai@gmail.com | "
                "LinkedIn: linkedin.com/in/karimosman89 | GitHub: github.com/karimosman89 | "
                "Available for senior AI engineering roles, consulting engagements, and speaking opportunities.")

    if any(w in q_lower for w in ["mlops", "deploy", "kubernetes", "docker", "pipeline", "cicd", "infra"]):
        return ("🚀 **MLOps:** Karim designs production ML infrastructure using Kubernetes (EKS/GKE/AKS), "
                "Triton Inference Server, KServe, MLflow, W&B, Ray, Prometheus/Grafana, and Datadog. "
                "CI/CD via GitHub Actions + ArgoCD. Feature stores with Feast. "
                "Achieved 99.9% uptime across all production systems.")

    if any(w in q_lower for w in ["scale", "user", "100k", "daily", "throughput", "performance"]):
        return ("📊 **Scale:** Karim's systems serve **100,000+ daily users** at Baker Hughes with sub-200ms latency. "
                "The document processing pipeline handles **10,000+ documents/day**. "
                "Real-time inference on Triton with GPU autoscaling handles burst traffic automatically.")

    # Fallback: synthesize from retrieved context
    if context_docs:
        # Pick the most relevant sentences
        relevant = context_docs[:3]
        answer = "Based on Karim's profile: " + " ".join(relevant[:2])
        if len(answer) > 500:
            answer = answer[:500] + "..."
        return answer

    return ("I'm Karim's AI assistant with deep knowledge of his work. Try asking about: "
            "**RAG systems**, **revenue impact**, **Baker Hughes projects**, **tech stack**, "
            "**certifications**, **computer vision**, **LLM fine-tuning**, or **contact info**.")


def render_rag_sidebar():
    """Render the RAG assistant in the sidebar."""
    lang = st.session_state.get("lang", "en")
    is_ar = (lang == "ar")

    st.sidebar.markdown("""
    <div class="rag-header">
        <div class="rag-title">
            <span class="rag-pulse"></span>
            AI RESUME AGENT
        </div>
        <div style="font-size:0.7rem; color:#9CA3AF; margin-top:0.4rem;">
            Powered by RAG · FAISS · MiniLM
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Suggested questions
    with st.sidebar.expander("💡 Suggested Questions", expanded=False):
        suggestions = [
            "What's Karim's revenue impact?",
            "Tell me about the RAG system at Baker Hughes",
            "What is Karim's tech stack?",
            "What certifications does Karim have?",
            "How to contact Karim?",
        ]
        for s in suggestions:
            if st.button(s, key=f"sug_{s[:20]}", use_container_width=True):
                st.session_state["rag_query"] = s

    # Chat history
    if "rag_history" not in st.session_state:
        st.session_state.rag_history = []

    # Display history
    for msg in st.session_state.rag_history[-6:]:  # last 3 exchanges
        role_label = "You" if msg["role"] == "user" else "🤖 Karim AI"
        css_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
        st.sidebar.markdown(f'<div class="{css_class}"><strong>{role_label}:</strong> {msg["content"]}</div>',
                           unsafe_allow_html=True)

    # Query input
    default_q = st.session_state.pop("rag_query", "")
    query = st.sidebar.text_input(
        "Ask about Karim...",
        value=default_q,
        placeholder="e.g. What's the revenue impact?",
        key="rag_input"
    )

    col_ask, col_clear = st.sidebar.columns([3, 1])
    with col_ask:
        ask_btn = st.button("Ask →", key="rag_ask", use_container_width=True)
    with col_clear:
        if st.button("Clear", key="rag_clear"):
            st.session_state.rag_history = []
            st.rerun()

    if ask_btn and query.strip():
        with st.sidebar:
            with st.spinner("Searching knowledge base..."):
                rag_state = build_rag_index()
                context = retrieve_context(query, rag_state)
                answer = simple_rag_answer(query, context)

        st.session_state.rag_history.append({"role": "user", "content": query})
        st.session_state.rag_history.append({"role": "assistant", "content": answer})
        st.rerun()

    # Footer info
    st.sidebar.markdown("""
    <div style="font-size:0.65rem; color:#4B5563; text-align:center; margin-top:1rem; padding-top:0.5rem; border-top:1px solid #1F2937;">
        Knowledge base: Baker Hughes · UniqMaster<br>RAG · FAISS · sentence-transformers
    </div>
    """, unsafe_allow_html=True)
