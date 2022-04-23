# mangaScrape

This program takes a list of manga chapters (provided by the user) and sends the updated chapters to the user's email.

## Getting started

>The latest version of this program only accomodates links from the [Mangakakalot](https://mangakakalot.com/) website. 

1. First off, open the `mangalist.txt` file. Here, you can add links to the landing pages of the manga you want updates for. Note that the link you need to use is the link for the landing page of the specific manga, not the links for the individual chapters. Note that each link must be placed on a new line.

2. You will need to create a dummy email account to send the manga chapters to your email. Open the `mangakakalot.py` file and replace the email details with your own. 

3. Run `mangakakalot.py` and enjoy!

## Automation

### Mac/Linux

We can choose to automate this program using the *crontab* utility of Unix-like operating systems. For a basic guide on the usage of crontabs, [click here](https://ostechnix.com/a-beginners-guide-to-cron-jobs/). Create a cron job that changes into the `Mangakakalot.com` directory and runs `mangakakalot.py`.

### Windows

Apply the process above to the [Task Scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10) program to automate on a Windows OS.