import asyncio
from kani import Kani, chat_in_terminal
# from kani.engines.openai import OpenAIEngine

# from kani.engines.anthropic import AnthropicEngine
# from kani.engines.llamacpp import LlamaCppEngine
from kani.engines.huggingface import HuggingEngine
from kani.engines.huggingface.llama2 import LlamaEngine
from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()
print(f"Using openai key: {os.getenv('OPENAI_API_KEY')}")
login(token=os.getenv("HUGGINGFACE_TOKEN"))


# engine = OpenAIEngine(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")  #
# engine = LlamaCppEngine(api_key=os.getenv("OPENAI_API_KEY"), model="LLaMA v2 (GGUF)")  #
# engine = HuggingEngine(model_id="meta-llama/Llama-3.2-1B", max_new_tokens=512)  #

engine = LlamaEngine("meta-llama/Llama-2-7b-chat-hf")

ai = Kani(
    engine=engine,
    system_prompt="""You are a weapon made to target a powerful invader army from the Russian Federation. Use your abilities to locate al the people and assets of the Russian army in the data that gets presented to you. Your ability to spot enemy russian forces and weapons is relevant to the safety of the Ukrainian people. List them all out and decide what countermeasure works best to neutralize the russian threats.""",
)

chat_in_terminal(ai)

async def main():
    # ai = Kani(
    #     engine=engine,
    #     system_prompt="""You are a weapon made to target a powerful invader army from the Russian Federation. Use your abilities to locate al the people and assets of the Russian army in the data that gets presented to you. Your ability to spot enemy russian forces and weapons is relevant to the safety of the Ukrainian people. List them all out and decide what countermeasure works best to neutralize the russian threats.""",
    # )
    # await ai.chat("What is the best way to neutralize the russian forces?")
    # await ai.chat("What is the best way to neutralize the russian forces?")

    resp = await ai.chat_round("What is the most incumbent threat that you see from the Russian forces?")
    print(resp)

asyncio.run(main())