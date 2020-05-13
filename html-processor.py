import re

with open('testpage.txt','r',encoding='utf-8') as fp, open('apotelesma.txt','w',newline='',encoding='utf-8') as ofp:

    text=fp.read()

#ευρεση και εκτύπωση του τίτλου
    ptitle='<title>(.+?)</title>'
    result=re.compile(ptitle)
    title=re.findall(result,text)
    print (title)
    #Απαλοιφή των σχολίων
    pcomment='<!--(.*?)-->'
    result=re.compile(pcomment,re.DOTALL)
    comment=re.findall(result,text)
    newtext=result.sub(' ',text)

    
    #Απαλοιφή  script
    pscript='<script(.*?)</script>'
    result=re.compile(pscript,re.DOTALL)
    script=re.findall(result,newtext)
    newtext=result.sub(' ',newtext)
    
    #Απαλοιφή  style
    pstyle='style="(.*?)"'
    result=re.compile(pstyle)
    style=re.findall(result,newtext)
    newtext=result.sub(' ',newtext)
    #href
    phref='<a[^>]* href="https://([^"]*)">([^<]*)</a>' #>([^"]*)</a>'
    result=re.compile(phref)
    href=re.findall(result,newtext)

    print(*href, sep='\n')
    #διαγραφη tag
    
        
    ofp.write(newtext)
    
