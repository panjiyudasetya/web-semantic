FROM node:18

# Set working directory
WORKDIR /simple_web_app

# Add everything inside the `simple_web_app` local directory
# into the working directory
ADD . /simple_web_app/

# Install the `simple_web_app` dependencies with yarn
RUN yarn install

# Run the `simple_web_app` app
CMD ["yarn", "serve"]
