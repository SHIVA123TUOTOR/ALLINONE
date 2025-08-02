import requests

def remove_background(image_path):
    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(image_path, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": "FRZPYZmMn895ZCh5GoctrSqK"},
    )
    if response.ok:
        with open("images/removed_bg.png", "wb") as out:
            out.write(response.content)
        print("Background removed and saved to images/removed_bg.png")
    else:
        print("Error:", response.text)
