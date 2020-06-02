from utilities import command_parsing, sliding_image

def main():
    image, w, h = command_parsing()
    sliding_image(image, w, h)

if __name__ == "__main__":
    main()