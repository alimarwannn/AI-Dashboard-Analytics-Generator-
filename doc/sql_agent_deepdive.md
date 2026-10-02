# LangGraph SQL Agent Architecture Deep-Dive

## 1. Core Tooling Pipeline
- **\sql_db_list_tables\**: Introspects available tables to keep the prompt context small.
- **\sql_db_schema\**: Retrieves column definitions, data types, and primary/foreign keys for selected tables.
- **\sql_db_query\**: Executes raw SQL queries against SQL Server and returns table records.

## 2. Guardrails & Safety
- **Dialect Enforcement**: Enforces T-SQL compliance (e.g., using \TOP n\ instead of \LIMIT n\).
- **Read-Only Restrictions**: Blocks dangerous DML actions (\DROP\, \DELETE\, \INSERT\, \UPDATE\).
- **Query Checker Node**: Intercepts queries prior to execution to validate syntax and table references.
- **Human-in-the-Loop (\interrupt\\)**: Pauses execution before query execution to allow human approval or edits.

## 3. The ReAct / Self-Healing Cycle
- **Cycle**: \gent\ -> \	ools_condition\ -> \	ools\ -> \gent\
- **Self-Healing**: When a query fails (e.g., \Msg 208\ or \Msg 8120\), the raw error message is written into \MessagesState\, allowing the LLM to inspect the failure, correct the SQL, and re-run automatically.
