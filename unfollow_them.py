#!/usr/bin/env python3
# coding: utf8

"""
    USAGE: python3 unfollow_them.py user=your_github_name
"""

from github import Github, NamedUser
import os
import sys

def main():
    github_user = get_user_from_params()

    # If we found an user
    if github_user[0]:
        git_token = read_token_from_file()

        # If we found a token
        if git_token[0]:
            # File to use
            file_name = "{name}_unfollowers.txt".format(name=github_user[1])
            # Find unfollowers
            unfollowers = get_unfollowers_from_file(file_name)
            # If we have unfollowers
            if len(unfollowers) > 0:
                unfollow_them(git_token[1],github_user[1], unfollowers)
                # After unfollowing them, we clean the unfollowers file
                open(file_name, 'w').close()


def get_unfollowers_from_file(file_name):
    unfollowers_from_file = []

    # Should exist, but just to be sure
    if not os.path.exists(file_name):
        print("Unfollowers file '{file}' not found".format(file=file_name))
    else:
        # Followers file found
        with open(file_name, 'r') as reader:
            # Get followers from file and also remove any line endings
            unfollowers_from_file = [line.replace("\n", "") for line in reader]

    return unfollowers_from_file

def unfollow_them(token, user, unfollowers):
    try:
        # Use the github token        
        g = Github(login_or_token=token)

        # Our own github profile
        # Don't use a github name, or we won't get our authenticated user
        authenticated_user = g.get_user()
        # Named_user is our own profile and only for checking profile stuff
        named_user = g.get_user(user)
  
        # Unfollow all the unfollowers
        for unfollower in unfollowers:
            try:
                the_unfollower = g.get_user(unfollower)
                
                # If we follow them then try to unfollow
                if authenticated_user.has_in_following(the_unfollower):
                    # Maybe he/she is following us again (could have unfollowed by mistake)
                    # So only unfollow if they really don't follow anymore
                    if not the_unfollower.has_in_following(named_user):
                        # Remove the unfollower
                        authenticated_user.remove_from_following(the_unfollower)
                        print("Unfollowed:", unfollower)
            except:
                print("Unfollower '{unfollower}' not found".format(unfollower=unfollower))

    except:
        print("Something went wrong trying to unfollow")
        print("Maybe the user '{name}' doesn't exist".format(name=user))

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