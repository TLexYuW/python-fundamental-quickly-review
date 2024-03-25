from PIL import Image
import os

def webp_to_gif(webp_file, gif_file):
    # Open the WebP file
    with Image.open(webp_file) as im:
        # Get the frame count and duration
        frame_count = im.n_frames
        print(frame_count)
        frame_duration = im.info.get("duration", 50)

        # Create the GIF from the frames
        frames = []
        for frame in range(frame_count):
            im.seek(frame)
            rgba_frame = im.convert("RGBA")
            frame_data = rgba_frame.tobytes()
            frame_bytes = len(frame_data)
            print(f"Frame {frame}: {frame_bytes} bytes")
            frames.append(im.copy())
        print(frames)

        # Save the frames as a GIF animation
        frames[0].save(
            gif_file,
            save_all=True,
            append_images=frames[1:],
            duration=frame_duration,
            loop=0,
        )


def gif_to_webp(gif_file, webp_file):
    with Image.open(gif_file) as im:
        frame_count = im.n_frames
        frame_duration = im.info.get("duration", 1000)

        frames = []
        for frame in range(frame_count):
            im.seek(frame)
            frames.append(im.copy())

        frames[0].save(
            webp_file,
            save_all=True,
            append_images=frames[1:],
            duration=frame_duration,
            optimize=True,
            loop=0,
            quality=10,
        )


if __name__ == "__main__":
    # Example usage
    # webp_file = "./sorted/pillow/output.webp"
    # gif_file = "./sorted/pillow/input.gif"
    input_directory = "./sorted/pillow/"
    output_directory = "./sorted/pillow/"
    
    # for filename in os.listdir(input_directory):
    #     if filename.endswith(".gif"):
    #         input_file = os.path.join(input_directory, filename)
    #         output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".webp")
    #         gif_to_webp(input_file, output_file)

    for filename in os.listdir(input_directory):
        if filename.endswith(".webp"):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".gif")
            webp_to_gif(input_file, output_file)


