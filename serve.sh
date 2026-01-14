#!/bin/bash
# Helper script to start Jekyll server with proper PATH configuration

# Add user gem bin directory to PATH
export PATH="$HOME/.gem/ruby/2.6.0/bin:$PATH"

# Navigate to project directory
cd "$(dirname "$0")"

# Start Jekyll server with watch mode
bundle exec jekyll serve --watch


