# Abuse Checker

This repository contains a Python script for checking abuse contacts for IP addresses and URLs using WHOIS data. The script allows you to specify a single IP address, an array of IP addresses, a single URL, or an array of URLs to check for abuse contacts.

## Usage

1. Clone the repository:


git clone https://github.com/ggunay/abuse-checker.git
   cd abuse-checker
Build the Docker image:

2. Set EXCHANGE_SERVER, SENDER_EMAIL and EMAIL_TEMPLATE in config.env

Note: The email template should include the <IP_OR_URL> placeholder since the script replaces it with the actual IP or full URL before sending the email.

3. docker build -t abuse_checker .

4. Run the Docker container with the desired target:

docker run --env-file config.env abuse_checker <IP/URL>

Replace <IP/URL> with the IP address or URL you want to check for abuse contact.


The script will perform a WHOIS lookup for domains to find abuse contact emails and will use the IP address directly as the abuse contact email.

## Requirements

Docker: Install Docker on your machine to build and run the container.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute or report issues if you encounter any problems while using the script.