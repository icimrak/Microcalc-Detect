# Microcalc-Detect
Convolutional network model trained for detection of microcalcifications using patch classification approach

The model is available in PRETRAINED_RESNET101_ADAM_LR5e-06_WD0.001_BS8.tar file. It requires PyTorch libraries.
Loading of the model:
weights = torch.load(weights_path)
model.load_state_dict(weights["state_dict"])

evaluation of patches (must be normalized to 0-1):
model.eval()
with torch.no_grad():
    inputs = inputs.to(device='cuda')
    model_outputs = model(inputs)
    _, predictions = model_outputs.max(1)
print(predictions)


