## Part 1
![Image](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/VPC%20Creation.png)
  - Creation of the VPC.

[!Image](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Subnet%20Creation.png)
  - Creation of the subnet.

[!Image](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Gateway%20Creation.png)
  - Creation of the internet gateway.

[!Image](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Route%20Table%20Creation.png)
  - Creation of the route table.

[!Image](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Security%20Group%20Creation.png)
  - Creation of the security group, with the inclusion of the three networks within the inbound rules.


## Part 2
  1. The instance was created with the "Amazon Linux 2" AMI, the default user for this instance type is "ec2-user".

  2. VPC attached during instanch launch. Selected by going to Network and then selecting the VPC created for this project.

  3. I selected to allow for an auto-assign public ip, it will hopefully be generated within the parameters and it can be found easily.

  4. Volume was added to the instance via the next step in the instance configuration. Done by adding a new volume and allocating size where it is appropriate.

  5. A tag was added in the next step, typed "Name" under Key and then typed "ZATREH-instance" under Value.

  6. The instance was associated to the security group by selecting "Select an existing security group" and then the "ZATREH-sg" group.

  7. An elastic IP was reserved by going to Elastic IPs under Network & Security and then selecting "Allocate Elastic IP Address". EIP was then associated to the instance by selecting Actions and then Associate Elastic IP Address.

[!Alt text](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Instance%20Creation.png)
  8. Instance created, along with all of the VPC details included.

  9. After SSHing into the instance, the hostname was changed to "zatreh-AMI" by typing the following command: "sudo hostname zatreh-AMI".

[!Alt text](https://github.com/WSU-kduncan/ceg3120-AZ-Sketches/blob/main/Project2/Proof%20of%20SSH%20Creation.png)
  10. Proof of SSH connection to the instance, included with the hostname change.

