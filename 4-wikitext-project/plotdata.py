import matplotlib.pyplot as plt

def loss_plot():
    epochs = list(range(1, 25))
    loss = [
    5.8690, 5.0316, 4.7849, 4.6428, 4.5452, 4.4740, 4.4180, 4.3716,
    4.3336, 4.3008, 4.2715, 4.2465, 4.2239, 4.2045, 4.1867, 4.1715,
    4.1577, 4.1449, 4.1336, 4.1225, 4.1130, 4.1034, 4.0950, 4.0871
    ]
    val_loss = [
    5.1323, 4.7735, 4.6149, 4.5026, 4.4313, 4.3772, 4.3453, 4.3113,
    4.2772, 4.2569, 4.2362, 4.2113, 4.1974, 4.1843, 4.1683, 4.1631,
    4.1579, 4.1394, 4.1437, 4.1252, 4.1164, 4.1096, 4.1008, 4.0983
    ]
    plt.figure()
    plt.plot(epochs, loss, label="Training loss")
    plt.plot(epochs, val_loss, label="Validation loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss vs Epoch")
    plt.legend()
    plt.show()

def accuracy_plot():
    epochs = list(range(1, 25))
    accuracy = [
    0.1546, 0.1980, 0.2157, 0.2284, 0.2379, 0.2454, 0.2515, 0.2568,
    0.2612, 0.2653, 0.2690, 0.2723, 0.2751, 0.2776, 0.2799, 0.2817,
    0.2835, 0.2850, 0.2863, 0.2877, 0.2887, 0.2899, 0.2910, 0.2918
    ]
    val_accuracy = [
    0.1950, 0.2195, 0.2343, 0.2455, 0.2530, 0.2598, 0.2645, 0.2685,
    0.2726, 0.2760, 0.2795, 0.2823, 0.2844, 0.2861, 0.2882, 0.2893,
    0.2892, 0.2923, 0.2922, 0.2944, 0.2941, 0.2970, 0.2969, 0.2973
    ]
    plt.figure()
    plt.plot(epochs, accuracy, label="Training accuracy")
    plt.plot(epochs, val_accuracy, label="Validation accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy vs Epoch")
    plt.legend()
    plt.show()

def perplexity_plot():
    epochs = list(range(1, 25))
    perplexity = [
    353.9, 153.1, 119.6, 103.8, 94.1, 87.7, 82.9, 79.1,
    76.2, 73.7, 71.6, 69.8, 68.3, 66.9, 65.8, 64.8,
    63.9, 63.1, 62.4, 61.7, 61.1, 60.5, 60.0, 59.5
    ]
    val_perplexity = [
    169.4, 118.3, 100.9, 90.2, 84.0, 79.6, 77.1, 74.5,
    72.0, 70.5, 69.1, 67.4, 66.5, 65.6, 64.6, 64.2,
    63.9, 62.7, 63.0, 61.8, 61.3, 60.9, 60.3, 60.2
    ]
    plt.figure()
    plt.plot(epochs, perplexity, label="Train perplexity")
    plt.plot(epochs, val_perplexity, label="Val perplexity")
    plt.xlabel("Epoch")
    plt.ylabel("Perplexity")
    plt.title("Perplexity vs Epoch")
    plt.legend()
    plt.show()

def top5_plot():
    accuracy = [
    0.1546, 0.1980, 0.2157, 0.2284, 0.2379, 0.2454, 0.2515, 0.2568,
    0.2612, 0.2653, 0.2690, 0.2723, 0.2751, 0.2776, 0.2799, 0.2817,
    0.2835, 0.2850, 0.2863, 0.2877, 0.2887, 0.2899, 0.2910, 0.2918
    ]
    top5 = [
    0.3064, 0.3850, 0.4111, 0.4276, 0.4395, 0.4485, 0.4556, 0.4617,
    0.4667, 0.4713, 0.4751, 0.4784, 0.4814, 0.4839, 0.4863, 0.4882,
    0.4900, 0.4917, 0.4932, 0.4946, 0.4960, 0.4971, 0.4982, 0.4992
    ]

    epochs = list(range(1, 25))
    plt.figure()
    plt.plot(epochs, accuracy, label="Top-1 accuracy")
    plt.plot(epochs, top5, label="Top-5 accuracy")

    plt.title("Top-1 vs Top-5 Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid()
    plt.show()
