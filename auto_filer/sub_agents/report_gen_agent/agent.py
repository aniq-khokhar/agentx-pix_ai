
from google.adk.agents import LlmAgent

report_gen_agent = LlmAgent(
    name="report_gen_agent",
    model="gemini-2.5-pro",
    description=(
        ""
    ),
    instruction=(
    """
    """
    ),
    output_key="",
)
