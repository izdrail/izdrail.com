#!/bin/bash

# Get the current version from the package.json file
version=$(grep -oP '"version": "\K[^"]+' frontend/package.json)

# Check if the version is already released
if git tag | grep -q "$version"; then
    echo "Version $version is already released"
    exit 1
fi

# Create a new tag
git tag -a $version -m "Release $version"

# Push the tag
git push origin $version


