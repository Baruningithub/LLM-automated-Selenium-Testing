
#Failed llm, much heavier llm to execute on local CPU, even crashes on collab GPU.

import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

from packaging import version
assert version.parse(transformers.__version__) >= version.parse("4.23.0")

tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B")
model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B")