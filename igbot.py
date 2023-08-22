from instagrapi import Client


# Define a class for interacting with Instagram using instagrapi library
class InstagramBot:
    # Initialize the bot with Instagram credentials
    def __init__(self, username, password):
        self.username = username  # Instagram username
        self.password = password  # Instagram password
        self.client = Client()  # Initialize an instance of instagrapi Client

    # Method to sign in to the Instagram account
    def sign_in(self):
        self.client.login(self.username, self.password)  # Use the instagrapi login method

    # Method to sign out from the Instagram account
    def sign_out(self):
        self.client.logout()  # Use the instagrapi logout method

    # Method to post an image along with a caption
    def post(self, image, caption):
        self.client.photo_upload(image, caption)  # Use the instagrapi photo_upload method

    # Method to post an album (multiple images) along with a caption
    def post_album(self, caption, images):
        self.client.album_upload(images, caption)  # Use the instagrapi album_upload method


# Create an instance of the InstagramBot class with Instagram credentials
ig_bot = InstagramBot("Username", "Password")

# Sign in to the Instagram account
ig_bot.sign_in()

# Post a single image with a caption
ig_bot.post("image.jpg", "caption")

# Post an album (multiple images) with a caption
ig_bot.post_album("caption", ["image1.jpg", "image2.jpg", "image3.jpg"])

# Sign out from the Instagram account
ig_bot.sign_out()
