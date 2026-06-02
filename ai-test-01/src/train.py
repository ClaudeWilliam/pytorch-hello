import torch
import torch.nn as nn
import torch.optim as optim


from dataset import get_dataloader
from model import Net
from utils import get_device
torch.backends.cudnn.enabled = False

def train():
    device = get_device()

    train_loader, test_loader = get_dataloader()

    model = Net().to(device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 训练
    for epoch in range(3):
        model.train()
        total_loss = 0

        for x, y in train_loader:
            x, y = x.to(device), y.to(device)

            pred = model(x)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

    # 测试
    model.eval()
    correct = 0

    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            pred = model(x)
            predicted = pred.argmax(dim=1)
            correct += (predicted == y).sum().item()

    accuracy = correct / len(test_loader.dataset)
    print("Accuracy:", accuracy)

    # 保存模型
    torch.save(model.state_dict(), "../models/mnist_model.pt")
    print("Model saved to models/mnist_model.pt")


if __name__ == "__main__":
    train()