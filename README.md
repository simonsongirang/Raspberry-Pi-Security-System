# Raspberry Pi Security System
Raspberry Pi Security System using Raspberry Pi Camera Module and PIR sensor (HC-SR501).

## Software Requirements
* Python3.5

## Hardware Requirements
* Raspberry Pi (Tested with V1,2,3)
* Raspberry Pi Camera Module
* PIR Sensor (HC-SR501)

## Installation Instruction
```python
# Clone repository
git clone https://github.com/simonsongirang/Raspberry-Pi-Security-System.git
cd Raspberry-Pi-Security-System-master
# Install required dependencies
pip3 install -r requirements.txt
# Adding configuration. See Configuration instruction
vim config_default
cp config_default config
python3 sensor.py
```

## Configuration
```
[General]
# When s
Start_Counter = 10
# Not used at the moment
Mode = Monitoring

[Sensor]
# Where HC-SR501's sensor is connected to Raspberry Pi's GPIO
GPIO_Sensor_Pin = 7

[Camera]
# Not relevant at the moment
RPI_Camera = True

[AWS_Notification]
# See AWS SNS https://aws.amazon.com/sns/ for more information about AWS SNS
# Enable/Disable AWS Notification
AWS_Notification = ON
# AWS SNS Topic ARN
AWS_Topic_ARN = arn:aws:sns:us-east-1:323458187916:Motion_Alert

[Slack_Notification]
# See Slack Bots https://api.slack.com/bot-users for more information
# Enable/Disable Slack Notification
Slack_Notification = ON
# API Token for your Slack Bot
Token=
# Name of the channel where the notifications will be posted
Channel=#security-feed

[Notification]
# For AWS SNS
Start_Subject = Camera Started
# Start Message
Start_Message = Camera Started
# For AWS SNS
Motion_Subject = Motion Detected
# For motion message
Motion_Message = Motion Detected
# How many times the system should notify user
Notification_Limit = 1
# When should the system send notification after sending first message
Notification_Timeout = 30


```

## Supported Integrations
* AWS SNS - Message
* Slack - Message & Image
![alt text](https://github.com/simonsongirang/Home-Security/blob/master/diagrams/Supported%20Integrations.jpg)

## Hardware Design
![alt text](https://github.com/simonsongirang/Home-Security/blob/master/diagrams/Network%20Diagram.jpg)
