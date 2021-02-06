# Alarme Buzzer

mosquitto_pub -h 192.168.101.1 -t /sensor/fadiga/0001/buzzer -m 1

## Build Docker
sudo docker build -t alarme-buzzer .
## Running Docker 
sudo docker run -d -v /dev:/dev --privileged  alarme-buzzer:latest


