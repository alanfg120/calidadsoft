FROM jenkins/jenkins:lts

# Cambia a root para instalar Python
USER root

# Instala Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean

# Cambia de nuevo al usuario Jenkins
USER jenkins