import requests

def generate_image_from_text(prompt):
    url = "https://api.together.xyz/v1/generate"
    headers = {
        "Authorization": "Bearer 4a1a0518bdf928df50495d499dc1608062c01596480f4193b9f9fa979f8a0029"
    }
    data = {
        "model": "stability-ai/stable-diffusion",
        "prompt": prompt,
        "num_images": 1
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        img_url = response.json()["data"][0]["url"]
        img_data = requests.get(img_url).content
        with open("images/generated.png", "wb") as f:
            f.write(img_data)
        print("Image saved as images/generated.png")
    else:
        print("Image generation failed:", response.text)
