#!/bin/bash

# Tested on Ubuntu 22.04

set -e

# Check if USERNAME parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <USERNAME>"
    exit 1
fi

USERNAME="$1"

# Check if the USERNAME already exists
if id "$USERNAME" &>/dev/null; then
    echo "Error: User '$USERNAME' already exists."
    exit 1
fi

# User Paths
USER_HOME_PATH="/home/$USERNAME"
USER_VNC_PATH="$USER_HOME_PATH/.vnc"
USER_VNC_STARTUP_PATH="$USER_VNC_PATH/xstartup"
USER_VNC_PASSWD="$USER_VNC_PATH/passwd"

# Generate an 8-character random password
PASSWORD=$(openssl rand -base64 12 | tr -dc 'a-zA-Z0-9' | head -c 8)

# System Path
VNC_SERVICE_PATH="/etc/systemd/system/"

# Create user
echo "Creating user $USERNAME..."
sudo useradd -m -p "$(openssl passwd -1 $PASSWORD)" -s /bin/bash "$USERNAME"
echo "Success to create user $USERNAME"

# Set up VNC desktop
sudo mkdir -p $USER_VNC_PATH
sudo chmod 700 $USER_VNC_PATH
tee $USER_VNC_STARTUP_PATH <<EOF
#!/bin/bash
xrdb \$HOME/.Xresources
autocutsel -fork
autocutsel -s PRIMARY -fork
startxfce4 &
EOF
sudo chmod +x $USER_VNC_STARTUP_PATH

# Use user's login password for VNC
user_password_hash=$(sudo grep "$USERNAME" /etc/shadow | cut -d':' -f2)

# Set VNC password using the user's login password hash
echo -n "$PASSWORD" | sudo vncpasswd -f > $USER_VNC_PASSWD
chmod 400 $USER_VNC_PASSWD

# Change owner under home path
chown -R $USERNAME:$USERNAME $USER_HOME_PATH

# Get the current maximum VNC server identifier
current_max_id=$(ls $VNC_SERVICE_PATH/vncserver@*.service | awk -F'[@.]' '{print $(NF-1)}' | sort -n | tail -n 1 2>/dev/null || echo 1)
echo "Current max vnc id: $current_max_id"

# Increment the VNC server identifier
vnc_id=$((current_max_id + 1))
echo "Generate new vnc id: $vnc_id"

VNC_SERVICE_NAME="$USERNAME.$vnc_id"

# Configure auto-start for VNC using systemd service
sudo tee "$VNC_SERVICE_PATH/vncserver@$VNC_SERVICE_NAME.service" <<EOF
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=$USERNAME
Group=$USERNAME
WorkingDirectory=/home/$USERNAME

PIDFile=/home/$USERNAME/.vnc/%H:$vnc_id.pid
ExecStartPre=-/usr/bin/vncserver -kill :$vnc_id > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 :$vnc_id
ExecStop=/usr/bin/vncserver -kill :$vnc_id

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the VNC server service
sudo systemctl daemon-reload
sudo systemctl enable "vncserver@$VNC_SERVICE_NAME.service"
sudo systemctl start "vncserver@$VNC_SERVICE_NAME.service"

echo "VNC desktop set up for user '$USERNAME' with password: $PASSWORD"
echo "Connect using VNC server ID: $vnc_id"
