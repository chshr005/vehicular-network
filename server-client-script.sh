#!/bin/bash

echo "Running script..."
source $1
tmux new-session -d "python3 Thread_Server.py" \;
sleep 20
tmux split-window "python3 Integrate.py" \; attach 
 