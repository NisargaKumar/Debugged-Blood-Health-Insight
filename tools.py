from crewai_tools.tools import SerperDevTool, WebsiteSearchTool

# Define tools
search_tool = SerperDevTool()

web_search_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-2.5-flash",
                temperature=0.7,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)
