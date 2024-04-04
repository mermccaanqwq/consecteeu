import random

def RandomFrom(repos):
    # Ensure the repos list is not empty to avoid IndexError
    if repos:
        # Return a random repository from the list
        return random.choice(repos)
    else:
        # Return None or raise an exception if the list is empty
        return None

# Example usage:
# Assuming 'repos' is a predefined list of repository names
repos = ['repo1', 'repo2', 'repo3', 'repo4']
repo = RandomFrom(repos)

# 'repo' will contain a randomly selected repository name from 'repos'
