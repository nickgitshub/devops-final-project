
import sys
firstarg=sys.argv[1]


def generateECR(ECRRepoName):
    print "sed 's|ECR-REPO|"+ECRRepoName+"|g' webapp.yaml > webapp-modified.yaml"

generateECR(firstarg)