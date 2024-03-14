from PIL import Image


def webp_to_gif(webp_file, gif_file):
    # Open the WebP file
    with Image.open(webp_file) as im:
        # Get the frame count and duration
        frame_count = im.n_frames
        frame_duration = im.info.get("duration", 50)

        # Create the GIF from the frames
        frames = []
        for frame in range(frame_count):
            im.seek(frame)
            frames.append(im.copy())

        # Save the frames as a GIF animation
        frames[0].save(
            gif_file,
            save_all=True,
            append_images=frames[1:],
            duration=frame_duration,
            loop=0,
        )


# Example usage
webp_file = "./pillow/input.webp"
gif_file = "./pillow/output.gif"

webp_to_gif(webp_file, gif_file)
