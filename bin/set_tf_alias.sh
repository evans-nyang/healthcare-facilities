#!/usr/bin/env bash

# Define the alias
alias_line='alias tf="terraform"'

# Check if the alias already exists in the bash_profile or bashrc
if [ -f ~/.bash_profile ]; then
    profile_file=~/.bash_profile
else
    profile_file=~/.bashrc
fi

if ! grep -q "$alias_line" "$profile_file"; then
    # If not, add the alias to the profile file
    echo "$alias_line" >> "$profile_file"
    echo "Alias 'tf' for 'terraform' has been added to $profile_file."
else
    # If the alias already exists, inform the user
    echo "Alias 'tf' for 'terraform' already exists in $profile_file."
fi

# Activate the changes in the current session
source "$profile_file"
