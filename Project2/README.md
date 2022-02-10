## Part 1
[!Alt text] (https://user-images.githubusercontent.com/76796854/153281383-8147b9f4-4c17-4505-9b26-573df8ab878e.png)
  - Creation of the VPC.

[!Alt text] (https://user-images.githubusercontent.com/76796854/153281333-43a3fb51-b09a-4b1a-ba74-3bf0063f4b6d.png)
  - Creation of the subnet.

[!Alt text] (https://user-images.githubusercontent.com/76796854/153281657-96ab28ff-05d6-4427-a927-9fb67872e638.png)
  - Creation of the internet gateway.

[!Alt text] (https://user-images.githubusercontent.com/76796854/153282111-d2500e03-1513-4662-83b0-5955c00517a3.png)
  - Creation of the route table.

[!Alt text] (https://user-images.githubusercontent.com/76796854/153283432-08572fa0-3d99-4ed8-bc24-e60d5b552816.png)
  - Creation of the security group, with the inclusion of the three networks within the inbound rules.


## Part 2
  1. The instance was created with the "Amazon Linux 2" AMI, the default user for this instance type is "ec2-user".

  2. VPC attached during instanch launch. Selected by going to Network and then selecting the VPC created for this project.

  3. I selected to allow for an auto-assign public ip, it will hopefully be generated within the parameters and it can be found easily.

  4. Volume was added to the instance via the next step in the instance configuration. Done by adding a new volume and allocating size where it is appropriate.

  5. A tag was added in the next step, typed "Name" under Key and then typed "ZATREH-instance" under Value.

  6. The instance was associated to the security group by selecting "Select an existing security group" and then the "ZATREH-sg" group.

  7. An elastic IP was reserved by going to Elastic IPs under Network & Security and then selecting "Allocate Elastic IP Address". EIP was then associated to the instance by selecting Actions and then Associate Elastic IP Address.

[!Alt text] (https://user-images.githubusercontent.com/76796854/153288850-aedc3dff-1c01-451e-85bf-153dcf692f05.png)
  8. Instance created, along with all of the VPC details included.

  9. After SSHing into the instance, the hostname was changed to "zatreh-AMI" by typing the following command: "sudo hostname zatreh-AMI".

[!Alt text] (https://user-images.githubusercontent.com/76796854/153492076-61495daf-4ac9-4e71-90e5-6f2933ea4e01.png)
  10. Proof of SSH connection to the instance, included with the hostname change.

