
# Removing LayerNorm from GPT-2

The repository contains the code accompanying the paper [You can remove GPT2's LayerNorm by fine-tuning](https://arxiv.org/abs/2409.13710). See our [HuggingFace repository](https://huggingface.co/apollo-research/gpt2_noLN) for models with removed LayerNorm.
The code is based on [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT), with just some small [changes](https://github.com/ApolloResearch/gpt2_noLN/commit/1f6c25e454287b014e9ff8309abeb49ababd49a4) to the model and training script.