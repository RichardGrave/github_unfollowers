#!/usr/bin/env python3
# coding: utf8

"""
    USAGE: python3 find_unfollowers.py user=your_github_name
"""

OVERWRITE = "w"
APPEND = "a"

from github import Github
import os
import sys

def main():
    github_user = get_user_from_params()

    # If we have found an user
    if github_user[0]:
        git_token = read_token_from_file()

        # If we found a token
        if git_token[0]:
            github_followers = get_followers_for_user(git_token[1], github_user[1])
            # Find unfollowers
            get_unfollowers(github_followers, github_user[1])


def get_unfollowers(followers, user):
    # Open file with followers
    file_name = "{name}.txt".format(name=user)

    followers_from_file = []

    # If it doesn't exits then create it.
    # No need to find unfollowers
    if not os.path.exists(file_name):
        print("Followers file '{file}' not found".format(file=file_name))
    else:
        # Followers file found
        with open(file_name, 'r') as reader:
            # Get the save followers from the previous search
            followers_from_file = [line.replace("\n", "") for line in reader]

        # Look at both lists and find the differences
        unfollower_names = [follower for follower in followers_from_file if follower not in followers]

        # Create the unfollowers file or append to existing unfollowers file
        create_file(user, unfollower_names, True, APPEND)

    # Now that we have the unfollowers, overwrite the followers file for the current state
    create_file(user, followers)


def get_followers_for_user(token, user):
    # Create empty follower array
    follower_names = []

    try:
        # Use the github token        
        g = Github(login_or_token=token)

        # Own github profile name
        github_user = g.get_user(user)
        followers = github_user.get_followers()

        # Get all the followers
        follower_names = [follower.login for follower in followers]

    except:
        print("Something went wrong trying to find the github_user")
        print("Maybe the user '{name}' doesn't exist?".format(name=user))
    
    return follower_names

def create_file(user, the_names, is_unfollowers=False, handling=OVERWRITE):
    filename = "{name}.txt"

    # Need a different name for the unfollowers file
    if is_unfollowers:
        filename = "{name}_unfollowers.txt"
    
    full_filename = filename.format(name=user)

    # Handling:
    # Overwrite for the followers file
    # Append for the unfollowers file
    file = open(full_filename, handling)

    for name in the_names:
        file.write(name+"\n")

    file.close()

    print("Saved to file: {file}".format(file=full_filename))

def get_user_from_params():
    user_name = ""
    proceed = False

    # Process command line arguments
    for text in sys.argv:
        if text.__contains__("user="):
            # We need the github profile name
            user_name = text.split("=")[1]
            proceed = True
            break
    
    if user_name == "":
        print("we need a user. E.g. -> 'user=github_user'")
 
    return (proceed, user_name)

def read_token_from_file():
    # File name for the github token
    file_name = "github_pat.txt"

    token = ""
    proceed = False

    # Check if github_pat.txt file exists
    # If not then try one directory higher
    if not os.path.exists(file_name):
        file_name = "../" + file_name

    if not os.path.exists(file_name):
        print("token file '{file}' not found".format(file=file_name))
    else:
        # Token file found
        with open(file_name, 'r') as reader:
            # Should contain only one line
            for line in reader:
                token = line
                proceed = True
                break

    if token == "":
        print("no token found")
    
    return (proceed, token)


main()