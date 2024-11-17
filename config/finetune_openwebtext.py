import time

eval_interval = 50
eval_iters = 50
log_interval = 1
wandb_log = True
wandb_project = 'stefan_remove_layer_norm'
name = 'gpt2-noLN'
wandb_run_name = name + '-' + str(time.time())
out_dir = f'out/{name}/'
dropout = 0
dataset = 'openwebtext'
init_from = 'gpt2'
remove_layer_norm = True

# only save checkpoints if the validation loss improves?
always_save_checkpoint = True

block_size = 1024
# OAI paper uses batch size 0.5M tokens (~2**19):
desired_batch_size = 2**19 / block_size
# What fits comfortably on my A100 without random crashes:
batch_size = 48
# Use gradient accumulation steps to match the effective batch size.
gradient_accumulation_steps = int(desired_batch_size // batch_size)

# Compiling didn't work for me.
compile = False

# We're not actually going all the way to 3000 iters.
learning_rate = 6e-4
warmup_iters = 100
decay_lr = True
lr_decay_iters = 2_000
max_iters = 3_000
