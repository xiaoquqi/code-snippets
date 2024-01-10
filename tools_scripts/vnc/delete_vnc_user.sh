#!/bin/bash

# Check if username parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

USERNAME="$1"

# Check if the user exists
if ! id "$USERNAME" &>/dev/null; then
    echo "Error: User '$USERNAME' does not exist."
    exit 1
fi

# System Path
VNC_SERVICE_PATH="/etc/systemd/system"

# Find the corresponding VNC server service file for the given username
service_files=$(grep -l "User=$USERNAME" $VNC_SERVICE_PATH/vncserver@*.service 2>/dev/null)

if [ -z "$service_files" ]; then
    echo "WARNING: VNC service file not found for user '$USERNAME'."
fi

# Extract the vnc_id from each service file, stop/disable the services,
# and remove the service files
for service_file in $service_files; do
    echo "Service file: $service_file"
    vnc_id=$(basename "$service_file" | sed 's/^.*vncserver@[^.]*.\(.*\).service$/\1/')
    sudo systemctl stop "vncserver@$USERNAME.$vnc_id.service"
    sudo systemctl disable "vncserver@$USERNAME.$vnc_id.service"
    sudo rm "$service_file"
    echo "Removing User '$USERNAME' associated VNC server (ID: $vnc_id) deleted."
done

# Stop all processes owned by the user
sudo pkill -u "$USERNAME"

# Delete the user and their home directory
sudo userdel -r "$USERNAME" 2>/dev/null

sudo systemctl daemon-reload

echo "User '$USERNAME' deleted."
