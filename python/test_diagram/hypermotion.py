from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3

with Diagram("HyperBDR Deploymenet", show=False):
    with Cluster("Source"):
        source_group = [
            EC2("Linux"),
            EC2("Windows"),
            EC2("VMWare")
        ]

    with Cluster("HyperBDR Services"):
        lb = ELB("Load Balance")
        hyperbdr_ec2 = EC2("HyperBDR")
        db_ec2 = EC2("MariaDB")

        lb - hyperbdr_ec2 - db_ec2

    with Cluster("Cloud"):
        s3 = S3("Object Storage")

    source_group >> lb >> s3
