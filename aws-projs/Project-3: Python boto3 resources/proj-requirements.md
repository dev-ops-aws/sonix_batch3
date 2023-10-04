## Title - Summary and Scheduling of AWS Resources (EC2, RDS)
### Services used - EC2, Boto3, RDS, SNS notifications, Gmail integration, Event bridge

### Phase-1: 
Trigger email to your gmail-id from Lambda 
Summarise all the resources running in your aws account at 6PM everyday (both running and stopped instances)
### Phase-2
Stop EC2 instances at 8PM everyday (if they are running) for all resources that have tag updated as auto-stop = true
Stop RDS instances at 8PM everyday (if they are running) for all resources that have tag updated as auto-stop = true