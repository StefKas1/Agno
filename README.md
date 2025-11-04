# Agno

## Links

- Repository: https://github.com/agno-agi/agno
- Documentation: https://docs.agno.com/introduction
- Self-hosted agent UI: https://docs.agno.com/agent-ui/introduction
- Supported models: https://docs.agno.com/concepts/models/introduction
- Supported storage databases: https://docs.agno.com/concepts/db/overview
- Model compatibility: https://docs.agno.com/concepts/models/compatibility
- Model usage examples (see left sidebar for more): https://docs.agno.com/concepts/models/openai-like
- Available built-in toolkits: https://docs.agno.com/concepts/tools/toolkits/toolkits
- MCP servers: https://github.com/modelcontextprotocol/servers?tab=readme-ov-file

## Collection information

- Enable debug mode in `.env` by `AGNO_DEBUG=true`
- When using `AgentStorage`, the SQL-based storage classes have fixed schemas. As new Agno features are released, the schemas might need to be updated. Automatic upgrades are done when the `auto_upgrade_schema` parameter is set to `True` in the storage class constructor. You only need to set this once for an agent run and the schema would be upgraded.

  ```python
  db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
  storage = PostgresStorage(table_name="agent_sessions", db_url=db_url, auto_upgrade_schema=True)
  ```

- Manual schema upgrades can be done by calling the `upgrade_schema` method on the storage class:
  ```python
  db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
  storage = PostgresStorage(table_name="agent_sessions", db_url=db_url)
  storage.upgrade_schema()
  ```
