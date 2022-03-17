# Project 4 Documentation
  1. Within the `/etc/hosts` file, each web server was added by entering their private IPs followed with their hostnames.
  2. In order to SSH into each web server, I SFTP'd the private key that I use to SSH into the proxy server so that I can bring it over to the said server to perform the SSH on thr web servers.
  3. To set up the HAProxy Load Balancer, I accessed the `haproxy.conf` file located in `/etc/haproxy/` directory and added the frontend and backend sections.
	- Nothing complicated has been added onto the frontend other than a few basic lines that was seen in a provided `.conf` file. For the backend, I added the two web servers where they will be checking port 80.
	- I restarted the service by entering `reboot`.
  4. I set up each web server by locating each of their `index.html` files located in the `/var/www/html/` directory and simply replaced its syntax to the ones provided in the directions.
	- The HTML files were located in this location because a file called `000-default.conf` file located in the `/etc/apache2/sites-available/` directory calls to this file when it runs to serve content.
	- I restarted the service by entering `reboot`.
  5. Down below are two screenshots to show a successful connection to web servers 1 and 2, respectively.

