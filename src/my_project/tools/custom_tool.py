class CustomTool:
    """A tool for processing text."""

    def run(self, inputs):
        # Example: Summarize text by extracting the first few sentences
        text = inputs.get("text", "")
        if not text:
            return "No input text provided."
        summary = text[:100] + "..." if len(text) > 100 else text
        return {"summary": summary}