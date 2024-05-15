import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from packaging import version
assert version.parse(transformers.__version__) >= version.parse("4.23.0")

tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B", torch_dtype=torch.float16,
 variant="fp16")
model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B",  torch_dtype=torch.float16,
 variant="fp16")