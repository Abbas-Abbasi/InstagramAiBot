import requests
import time
from datetime import datetime, timedelta
from PIL import Image
from io import BytesIO

# Import InstagramBot and AIGenerator classes from respective modules
from igbot import InstagramBot
from ai import AIGenerator

# Create an instance of the InstagramBot class with Instagram credentials
instagram_bot = InstagramBot("Username", "Password")
# Replace this with your actual OpenAI API key
api_key = "sk-"
# Create an instance of the AIGenerator class with the API key
generator = AIGenerator(api_key)


# Define a function to create and post content on Instagram
def make_post():
    print("Task Executed at:", datetime.now())

    # Generate a text prompt and image URLs using the AI generator
    res, images_url = generator.generate_prompt_and_image()

    print("Prompt:", res)
    print("Images:", images_url)

    # Download and save images locally
    for i in range(3):
        response = requests.get(images_url[i])
        img = Image.open(BytesIO(response.content))
        img.save(f"images/{i}.jpg")

    caption = res
    image_paths = ["images/0.jpg", "images/1.jpg", "images/2.jpg"]

    # Post the generated content on Instagram using the bot
    instagram_bot.post(caption, image_paths)


# Define the main function that controls the overall execution
def main():
    # Sign in to the Instagram account
    instagram_bot.sign_in()

    # Calculate the next scheduled post time (starting at the beginning of the next day)
    current_time = datetime.now()
    next_post_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

    # Run the content posting loop
    while True:
        if datetime.now() >= next_post_time:
            for _ in range(3):
                make_post()  # Create and post content
                time.sleep(3 * 60 * 60)  # Sleep for 3 hours between posts

            # Update the next scheduled post time for the next day
            next_post_time += timedelta(days=1)

        # Sleep for a shorter duration (e.g., 10 minutes) before checking again
        time.sleep(10 * 60)


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
