# Project 4 Documentation
  - Within the `/etc/hosts` file, each web server was added by entering their private IPs followed with their hostnames.
  - In order to SSH into each web server, I SFTP'd the private key that I use to SSH into the proxy server so that I can bring it over to the said server to perform the SSH on the web servers.
  - To set up the HAProxy Load Balancer, I accessed the `haproxy.conf` file located in `/etc/haproxy/` directory and added the frontend and backend sections.
    - Nothing complicated has been added onto the frontend other than a few basic lines that was seen in a provided `.conf` file. For the backend, I added the two web servers where they will be checking port 80.
    - I restarted the service by entering `reboot`.
  - I set up each web server by locating each of their `index.html` files located in the `/var/www/html/` directory and simply replaced its syntax to the ones provided in the directions.
    - The HTML files were located in this location because a file called `000-default.conf` file located in the `/etc/apache2/sites-available/` directory calls to this file when it runs to serve content.
    - I restarted the service by entering `reboot`.
  - Down below are two screenshots to show a successful connection to web servers 1 and 2, respectively.
![Image](https://user-images.githubusercontent.com/76796854/158911347-fec57b5d-7c55-4290-857d-8bfc08a14f39.png)
![Image](https://user-images.githubusercontent.com/76796854/158911388-f9f61e2c-9e6a-4b69-819b-bbda44efaa9b.png)
