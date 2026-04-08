import matplotlib.pyplot as plt
import numpy as np

class_names = ['forks', 'knives', 'mugs', 'pens', 'spoons']

def collect_images(dataset: list, model):
    if dataset is None or model is None:
        return [], []
    
    correct, wrong = [], []
    for images, labels in dataset.take(1):
        preds = model.predict(images)
        pred_labels = np.argmax(preds, axis=1)
        true_labels = np.argmax(labels.numpy(), axis=1)
        for img, t, p in zip(images, true_labels, pred_labels):
            entry = (img.numpy().astype("uint8"), class_names[t], class_names[p])
            if t == p:
                correct.append(entry)
            else:
                wrong.append(entry)
    return correct, wrong



def plot_images(images_list: list, title: str, n=8):   # n = amount of images
    if len(images_list.file_paths) < 1:
        print(f"No {title} found!")
        return
    num = min(n, len(images_list))
    plt.figure(figsize=(6,6))
    for i in range(num):
        ax = plt.subplot(4,4,i+1)
        plt.imshow(images_list[i][0])
        plt.title(f"True: {images_list[i][1]}\nPred: {images_list[i][2]}", fontsize=10)
        plt.axis("off")
    plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()