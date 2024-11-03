import os
import json

def generate_image_json(directory='img'):
    # List all PNG files in the specified directory
    image_files = [f"{directory}/{file}" for file in os.listdir(directory) if file.endswith('.png')]
    
    # Write the list of images to images.json
    json_path = os.path.join(directory, 'images.json')
    with open(json_path, 'w') as json_file:
        json.dump(image_files, json_file, indent=4)
    print(f"Updated {json_path} with {len(image_files)} images.")

# Run the function
if __name__ == "__main__":
    generate_image_json()
