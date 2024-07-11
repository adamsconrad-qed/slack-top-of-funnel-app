Overview
Our Slack bot listens for messages in a specific channel, extracts website domains from these messages, and provides information about the companies associated with these domains using the PitchBook API.
Making Changes
You can make changes to the bot's behavior and responses directly through the GitHub website. Here's how:

1. Navigating to the File

In the repository, you'll see a list of files and folders.
Click on the app folder.
Then click on the slack_bot.py file. This is where most of the bot's logic and responses are defined.

2. Editing the File

Once you're viewing the slack_bot.py file, click the pencil icon (🖊️) in the top right corner of the file view to edit the file.
You'll now be in edit mode and can make changes to the file.

3. Modifying Bot Responses
To change the bot's responses, look for the say() function calls. These are where the bot sends messages. For example:
pythonCopysay(
    text="No PitchBook data available for this company.",
    thread_ts=event["ts"]
)
You can modify the text within the quotes to change what the bot says.
4. Committing Your Changes

After making your changes, scroll to the bottom of the page.
You'll see a "Commit changes" section.
In the first box, write a short description of your changes (e.g., "Updated no data available message").
Optionally, you can add a more detailed description in the second box.
Ensure "Commit directly to the main branch" is selected.
Click the green "Commit changes" button.

5. Automatic Deployment
After you commit your changes:

GitHub will automatically trigger a deployment to Heroku.
This process usually takes a few minutes.
Once complete, your changes will be live in the Slack bot.

Testing Your Changes
To make sure your changes worked:

Go to the Slack channel where the bot is active.
Try sending a message that should trigger the bot's response.
Check if the bot responds with your updated message.

Need Help?
If you're unsure about making changes or encounter any issues:

Reach out to Owen.
Avoid making changes to files other than slack_bot.py unless you're confident in what you're doing.
If something goes wrong, we can always revert changes through GitHub.
