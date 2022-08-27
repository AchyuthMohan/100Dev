<h1 align="center">100Dev</h1>
<h4 align="center">Making developer workflow a byte more easier❤️</h4>

Demo: https://www.youtube.com/watch?v=0lE-1JQhWos

As developers, we tend to do a lot of repetitive tasks. 100Dev is a collection of tools that would help developers make their work, a byte more easier.The tool does the following:-

- Git Automation
- Automatic Stack Overflow Error finder
- Spotify playlist generator
- Resource utilization monitor
- Automated document generator
- Automated gmeet joiner


### Detailed description
1. Git Automation

Once the user starts working, Git Automation automates the workflow of creating the repo, installing packages and requirements and switching to working branch all in one single command. Instead of running multiple commands like git clone, setting up the virtual env, installing the packages, ignoring the .gitignore files and switching to another feature branch, we plan to automate it using a single command like:

```bash
python app.py --cmd clone --repo azuredeployment_ --lang py --branch abcde
```

Similarly instead of doing git pull, git add *, git commit -m and git push, we plan to automate the entire set of commands using a single command.

2. Stack Overflow Error Finder

Whenever developers encounter an error their go-to place is StackOverflow. We plan to automate this error such that, whenever an error is countered, the script automatically search the error message on StackOverflow and and shows the top solutions (based on score and view_count) to the users. This would eliminate the process of manually searching for that error in the net

3. Spotify playlist generator

What kind of developer doesn't love some cool music to vibe while programming? This feature allows the developer to create and play a random playlist based on the liveness, danceability and energy levels required instantly and automatically. The mood is set for work.

4. Resource utilization monitoring tool

Once the developer completes the code, he/she needs to check its resource utilization (like CPU, memory, disk usage, networking stats, etc) and ensure that it doesn't extend the threshold value

5. Auto doc generator

Once the development of a product is completed, the last step is documenting it. As developers, this is a tedious and boring process. That is why I try to automate it. This feature allows users to automatically generate doc based on the classes and function of their codebase

6. Gmeet auto joineer

Developers have a lot of standups, a daily and weekly meetings that they need to join This feature automatically joins these sessions for the developers

### Tech stack
Python, Spotify API , Stackoverflow API, pyautogui, pyfiglet, matplotlib, numpy, psutils, subprocess, PyQt5

