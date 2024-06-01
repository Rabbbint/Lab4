FROM python:3.11

RUN apt-get update
RUN apt-get install -y git
RUN apt-get update && apt-get install -y \
    xvfb \
    libgl1-mesa-glx \
    libgtk2.0-dev \
    libgtk-3-dev \
    libnotify-dev \
    libgconf-2-4 \
    libatk1.0-dev \
    libcairo2-dev \
    libcups2-dev \
    libfontconfig1-dev \
    libgdk-pixbuf2.0-dev \
    libgirepository1.0-dev \
    libgtk2.0-dev \
    libpango1.0-dev \
    libsoup2.4-dev \
    librsvg2-dev \
    libwebkit2gtk-4.0-dev \
    libxtst-dev \
    libxss1 \
    gconf-service \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget

RUN git clone https://github.com/Rabbbint/Lab4.git

WORKDIR /Laba4

RUN pip install -r requirements.txt

CMD ["python", "Project.py"]