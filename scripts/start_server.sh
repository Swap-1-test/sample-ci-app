#!/bin/bash
sudo systemctl start httpd
sudo systemctl enable httpd
sudo cp /home/ec2-user/index.html /var/www/html/index.html
