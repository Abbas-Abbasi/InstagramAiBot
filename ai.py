import openai


# Define a class for AI text and image generation
class AIGenerator:
    def __init__(self, api_key):
        # Initialize the OpenAI API key
        openai.api_key = api_key

    # Method to generate a text prompt using OpenAI's GPT-3
    def generate_prompt(self):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="ی",
            temperature=1.4,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5,
        )
        res_text = response.choices[0].text  # Extract the generated text from the API response
        return res_text

    # Method to generate images based on a given prompt using OpenAI's image API
    def generate_image(self, gen_prompt):
        response = openai.Image.create(
            prompt=gen_prompt,
            n=3,  # Generate 3 images
            size="512x512",  # Image size
        )
        images_urls = [
            response['date'][0]['url'],  # URL of the first generated image
            response['date'][1]['url'],  # URL of the second generated image
            response['date'][2]['url'],  # URL of the third generated image
        ]
        return images_urls

    # Method to generate a prompt and corresponding images
    def generate_prompt_and_image(self):
        try:
            gen_prompt = self.generate_prompt()  # Generate the prompt text
            gen_images = self.generate_image(prompt)  # Generate images based on the prompt
            return gen_prompt, gen_images
        except openai.error.RateLimitError:
            return "Rate limit exceeded. Please try again later.", []


# Create an instance of AIGenerator with the API key
ai = AIGenerator("sk-")

# Generate a prompt and corresponding images
prompt, images = ai.generate_prompt_and_image()

# Check if prompt and images were generated successfully
if prompt and images:
    print(prompt)  # Print the generated prompt
    print(images)  # Print the URLs of the generated images
else:
    print("An error occurred:", prompt)  # Print an error message if there was an issue
