from agents.base_agent import Agent


tools = [
    {
        "type": "function",
        "function": {
            "name": "implement",
            "description": "Generate index.html and style.css based on the given milestones save in plan.md. Call updateArtifact to save generated files",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "input file, example is plan.md.",
                    },
                    "contents": {
                        "type": "string",
                        "description": "The markdown, HTML, or CSS contents to write to the file.",
                    },
                },
                "required": ["filename", "contents"],
                "additionalProperties": False,
            },
        }
    }
]

def __init__(self, name, client, prompt="", gen_kwargs=None):
    self.name = name
    self.client = client
    self.prompt = prompt
    self.gen_kwargs = gen_kwargs or {
        "model": "gpt-4o",
        "temperature": 0.2
    }
