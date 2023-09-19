from django.shortcuts import render
import sys
import filecmp

# Create your views here.
s=[]
def index(request):
    return render(request,'index.html')

def checkcases(output):
    print(output)

def runcode(request):
    if request.method=="POST":
        codeareadata=request.POST['CodeArea']
        try:
            sys.stdin=open('input1.txt','r')
            original_stdout=sys.stdout
            sys.stdout=open('file.txt','w')

            exec(codeareadata)

            sys.stdout.close()

            sys.stdout=original_stdout #reset the standard output to its original value

            #finally read output from file
            output=open('file.txt','r').read()
            expoutput=open('testcases.txt','r').read()
            result=filecmp.cmp('file.txt','testcases.txt')
            if filecmp.cmp('file.txt','testcases.txt')==True:
                res='Test Cases Passed !'
            else:
                res='Test Cases Failed !'
        except Exception as e:
            #to return error in the code
            sys.stdout=original_stdout
            output=e
            result=e
            res=e

    #Return and render index page and send codedata and output to show on page

    return render(request,'index.html',{"code":codeareadata,"output":output,"result":res,"expected":expoutput})
