import torch
import torch.nn as neural_network
import torchvision
import torchvision.transforms as transforms

import cv2


def run(weights_path, images_path, device='cpu'):

    model = torchvision.models.resnet101()
    model.fc = neural_network.Linear(in_features=model.fc.in_features, out_features=2, bias=True)

    weights = torch.load(weights_path, map_location=torch.device('cpu'))
    model.load_state_dict(weights["state_dict"])

    model.to(device=device)

    print('0 for clusters, 1 for without clusters, image required shape 674x674x3')
    transform = transforms.Compose([transforms.ToTensor()])
    for path in images_path:
        image = cv2.imread(path)
        # print(image.shape)
        image = image / image.max()
        image = transform(image).float()

        inputs = image.unsqueeze(0)

        model.eval()
        with torch.no_grad():
            inputs = inputs.to(device=device)
            model_output = model(inputs)

            soft_max = neural_network.Softmax(dim=1)
            soft_max_output = soft_max(model_output)

            _, prediction = model_output.max(1)

        print(path, '-', soft_max_output[0].tolist(), '-', prediction.item())
        
run(weights_path = "PRETRAINED_RESNET101_ADAM_LR5e-06_WD0.001_BS8.tar", images_path = ["images/calc.png","images/mass.png"], device='cpu')
