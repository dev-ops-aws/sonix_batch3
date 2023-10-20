Project-1: S3 Website Hosting of Project Profile
--------------------------------------------------

Services Used


Amazon S3: For storing and hosting the static website files.


Amazon CloudFront: Content Delivery Network (CDN) for fast content delivery.


Amazon Certificate Manager (ACM): To obtain and manage SSL/TLS certificates for secure website access.


Amazon CloudWatch: Monitoring and logging service for tracking website performance.


AWS Developer Tools - GitHub: For version control and collaboration.


AWS CloudFormation: For infrastructure as code to automate resource provisioning.


Domain Mapping: Custom domain mapping (e.g., www.yourdomain.com).


-----------------------------------------------------

Phase 1: Static Website Hosting using CloudFront
-----------------------------------------------------

Objective: To host a static website using AWS services and improve website performance through content delivery via CloudFront.

Steps:

Create an S3 Bucket for Website Hosting:
-----------------------------------------------------

s3bucketpolicy.template
-----------------------------------------------------
Replace the following values with your specific information:

Bucket Name: Replace 'prasanthkumar.000' with the name of your S3 bucket. This should be done wherever it appears in the template.

Bucket ARN: In the Resource section under PolicyDocument, you can replace 'prasanthkumar.000' with your S3 bucket name using the Fn::Sub function. Ensure you replace this value with your bucket name.

s3bucket (1).template
----------------------------------------------------
Replace prasanthkumar.000 with your desired S3 bucket name under the BucketName property.

Modify index.html and error.html with your preferred index and error document names under the WebsiteConfiguration section.

Edit the values of BlockPublicAcls, BlockPublicPolicy, IgnorePublicAcls, and RestrictPublicBuckets under the PublicAccessBlockConfiguration section as needed to configure your desired public access settings for the S3 bucket.

cloudwatch.yml
---------------------------------------------------
Replace the following values with your specific information:

Alarm Name: Modify the `AlarmName` property to specify a unique name for your CloudWatch Alarm.
     
Threshold: Adjust the `Threshold` property to set the error rate threshold at which the alarm should trigger.
     
Distribution ID: Change the `Value` under the `Dimensions` section to the CloudFront distribution you want to monitor.
     
SNS Topic ARN: Update the `AlarmActions` and `OKActions` with the ARN of your SNS topic for notifications.

cloudfront (3).template
---------------------------------------------------
 Replace the following values with your specific information:
 
S3 Bucket Domain Name: Modify the `DomainName` property under `Origins` to specify the domain name of your S3 bucket. 

S3 Origin ID: You can change the `Id` under `Origins` to give your S3 origin a unique identifier.

Viewer Protocol Policy: If you want to change the viewer protocol policy, modify the `ViewerProtocolPolicy` property under `DefaultCacheBehavior`.

Enabled: Set the `Enabled` property to `true` to enable the CloudFront distribution.

---------------------------------------------------

Create an Amazon S3 bucket to store static website files.
Configure the bucket for static website hosting.

Upload Website Files:
Upload your website's static files (HTML, CSS, JavaScript, images, etc.) to the S3 bucket.

Configure Amazon CloudFront:
Set up an Amazon CloudFront distribution to serve your website content.
Configure the CloudFront distribution to use your S3 bucket as the origin.

Secure Your Website with HTTPS:
Use ACM to obtain an SSL/TLS certificate for secure website access.
Configure the CloudFront distribution to use the certificate, enabling HTTPS.
Domain Mapping:

Map your custom domain (e.g., www.yourdomain.com) to your CloudFront distribution. Consider using AWS Route 53 for DNS management.

Monitoring and Logging:
Set up Amazon CloudWatch to monitor website performance and troubleshoot issues.

-------------------------------------------------------

Phase 2: Implementing CI/CD - GitHub to S3
-------------------------------------------------------

Objective: To set up Continuous Integration and Continuous Deployment (CI/CD) for your static website using GitHub as the source repository, AWS CodePipeline for automation, and automatic reflection in both GitHub and S3. Additionally, set up CloudWatch to monitor 404 error rates.

Steps:

Source Code Repository:

Host your website's source code in a version control system. You'll use GitHub in this project.
Continuous Integration (CI):


Configure CI to automatically build your website whenever changes are pushed to the repository.
Use AWS CodeBuild to create build environments and automate the build process.
Deployment (CD):


Implement a CD process to automatically deploy the built website to your S3 bucket.
CI/CD Pipeline:


Create a CI/CD pipeline that integrates your GitHub repository with AWS services.
Automate the CI and CD processes based on code changes.

-------------------------------------------------------

Testing:
-------------------------------------------------------

Implement testing as part of your CI/CD process to ensure your website works correctly after each deployment.

Monitoring and Logging:
-------------------------------------------------------

Configure CloudWatch to monitor the CI/CD pipeline, as well as your website, specifically tracking 404 error rates.

Automation and Notifications:
Maintain detailed documentation, including architecture diagrams, configurations, and procedures.

Testing and Validation:
Before going live, thoroughly test the CI/CD process to ensure it correctly builds, deploys, and updates your website.

Continuous Improvement:
Regularly review and improve your CI/CD pipeline and website hosting setup to optimize performance and maintain reliability.
