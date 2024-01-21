# devops-task
## My solution to the problem
- In this case i would like to take an AWS Cloud service to serve all the requirements.
- As the Ecommerce application has some background jobs to run we will use Amazon SQS service for that.
- As the application relies on some external system for product list the main thing will be reducing API hit or dependencies. In some cases a Redis Cache Server can be helpfull for the system, if applicable.
- As the E-commerce traffic can be varied from time to time we can use Loac Balancer along with Scalable EC2 Instances in most extrem cases.
- Whenever the desired pod inside of the kubernetes cluster get full then horizontal pod scalling might be helpfull to take all increased traffics.
- We can use RDS auto scallable cluster so that when its needed it would be scalabble according to the traffic needs.
