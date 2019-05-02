#!/bin/bash

# Set the home page.
echo "<html><body><h2>Welcome to Azzure! My name is $(hostname).</h2></body></html>" | sudo tee -a /var/www/html/index2.html
