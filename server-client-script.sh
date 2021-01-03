#!/bin/bash

echo "Running script..."
source $1
tmux new-session -d "python3 base_server.py" \;
sleep 20
tmux split-window "python3 base_server2.py" \; attach 
 