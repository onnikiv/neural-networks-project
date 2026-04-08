import os, shutil, pathlib
import random

BASE_DIR = pathlib.Path(__file__).resolve().parent
org_dir = BASE_DIR / "original-images"
new_dir = BASE_DIR / "images"

classes = ["fork", "knife", "mug", "pen", "spoon"]

def make_subset(subset_name: str, class_name: str, filenames: list):
    subset_dir = new_dir / subset_name / class_name
    os.makedirs(subset_dir, exist_ok=True)
    for fname in filenames:
        shutil.copyfile(
            src=org_dir / f"{class_name}-images" / fname,
            dst=subset_dir / fname
        )

# Split percentages
train_pct = 0.7     # 70% for training
val_pct = 0.15      # 15% for validation
test_pct = 0.15     # 15% for testing

for cls in classes:
    cls_dir = org_dir / f"{cls}-images"
    if not cls_dir.exists():
        raise FileNotFoundError(f"Directory not found: {cls_dir}")
    
    files = [f for f in os.listdir(cls_dir) if f.endswith(".png")]
    random.shuffle(files)
    
    n_total = len(files)
    n_train = int(n_total * train_pct)
    n_val = int(n_total * val_pct)
    n_test = n_total - n_train - n_val
    
    make_subset("train", cls, files[:n_train])
    make_subset("validation", cls, files[n_train:n_train+n_val])
    make_subset("test", cls, files[n_train+n_val:])