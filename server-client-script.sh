#!/bin/bash

echo "Running script..."

tmux new-session -d "./server.sh" \;
sleep 20
tmux split-window "./client.sh" \; attach 
 