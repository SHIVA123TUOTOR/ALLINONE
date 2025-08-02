from modules.image_generator import generate_image_from_text
from modules.background_remover import remove_background
from modules.voice_to_image import voice_to_image
from modules.object_detection import detect_objects
from modules.memory_timeline import add_memory, get_memories

def main():
    print("Welcome to Jarvis AI")
    # Example use
    text = "a cat flying in the sky"
    generate_image_from_text(text)
    voice_to_image()
    remove_background("images/input.png")
    detect_objects()
    add_memory("User met Elon Musk at 2 PM")
    print(get_memories())

if _name_ == "_main_":
    main()
