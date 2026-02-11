import os


def get_categories(base_path: str) -> list[str]:
    if not os.path.exists(base_path):
        return []
    return [d for d in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, d))]


def get_images_in_category(base_path: str, category: str) -> list[str]:
    category_path = os.path.join(base_path, category)
    if not os.path.exists(category_path):
        return []
    valid_ext = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    images = []
    for f in os.listdir(category_path):
        if f.lower().endswith(valid_ext):
            images.append(os.path.join(category_path, f))
    return images
