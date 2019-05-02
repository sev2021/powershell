#!/bin/bash

# Set the home page.
echo "<html><body><h3>Welcome to Azzure! My name is $(hostname).</h3></body></html>" | sudo tee -a /var/www/html/index2.html
