FROM python:3.7

# Set working directory
WORKDIR /web_service

# Add everything inside the `web_service` local directory
# into the working directory
ADD . /web_service/

# Install all requirements 
RUN pip install -r requirements.txt

# Run server of the web service app
RUN chmod +x /web_service/runserver.sh
CMD ["sh", "runserver.sh"]
