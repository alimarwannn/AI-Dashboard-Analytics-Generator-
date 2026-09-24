# Business Model Document: AI Dashboard & Analytics Generator

## 1. Executive Summary
The **AI Dashboard & Analytics Generator** is an enterprise AI solution designed to democratize internal data access. It enables non-technical business stakeholders, managers, and operational teams to query relational databases using plain natural language. The system converts conversational questions into safe, executable SQL queries, runs them against target schemas, visualizes findings via interactive Plotly charts, and summarizes key insights in plain English.

## 2. Problem Statement
- **BI Bottlenecks**: Centralized data teams spend substantial time fulfilling routine ad-hoc SQL requests for simple metrics.
- **Decision Latency**: Decision-makers often experience delays waiting for custom reports and dashboards.
- **SQL Knowledge Barrier**: Front-line managers lack schema familiarity and query syntax skills, creating reliance on data engineers.

## 3. Value Proposition
- **Conversational Querying**: Zero SQL knowledge required; users ask questions in natural language.
- **Automated Visualization**: Direct generation of interactive charts (via Plotly) dynamically rendered in Streamlit.
- **Narrative Explanations**: Automated plain-language synthesis highlighting key trends, drivers, and outliers behind the numbers.
- **Multi-Database Support**: Connects to standard relational backends (SQLite, SQL Server, PostgreSQL) via SQLAlchemy.

## 4. Target Personas
- **Operational Managers**: Require quick operational metrics (e.g., daily sales, regional support performance) without ticket delays.
- **Executive Leadership**: Require immediate high-level performance metrics and visual trend summaries on demand.
- **Data Analysts**: Can leverage the agent for rapid exploratory queries and prototyping initial visualizations.

## 5. System Architecture & Tech Stack
- **Interface & Visualization**: Streamlit (web UI), Plotly Express (interactive charts).
- **Agent Framework**: LangChain SQL Agent with database schema inspection and safe read-only query limits.
- **Data Layer**: SQLAlchemy abstraction over SQLite / SQL Server.
- **LLM Engine**: Natural language to SQL generation and contextual result summarization.

## 6. Implementation Scope (8-Day Roadmap)
- **Phase 1 (Days 1–2)**: Database configuration, schema introspection, and SQLAlchemy connection layer.
- **Phase 2 (Days 3–4)**: LangChain SQL Agent configuration, prompt design, and execution validation.
- **Phase 3 (Days 5–6)**: Streamlit user interface, Plotly chart generation, and narrative explanation engine.
- **Phase 4 (Days 7–8)**: End-to-end evaluation using 5 business queries and final presentation preparation.
