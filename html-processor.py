import re

with open('testpage.txt','r',encoding='utf-8') as fp, open('apotelesma.txt','w',newline='',encoding='utf-8') as myfile:
    def save_to_file(*text):
        for lines in text:
            myfile.write('\n'.join(str(line) for line in lines))
            myfile.write('\n')

    text=fp.read()

    #1.ευρεση και εκτύπωση του τίτλου
    ptitle='<title>(.+?)</title>'
    result=re.compile(ptitle)
    title=re.findall(result,text)
    print (title)
    myfile.write(str(title))
    myfile.write('\n')
    
    #2.Απαλοιφή των σχολίων
    pcomment='<!--(.*?)-->'
    result=re.compile(pcomment,re.DOTALL)
    comment=re.findall(result,text)
    newtext=result.sub(' ',text)

    
    #3.Απαλοιφή  script & style
    pscript='<script(.*?)</script>|style="(.*?)"'
    result=re.compile(pscript,re.DOTALL)
    script=re.findall(result,newtext)
    newtext=result.sub(' ',newtext)
    
    #4.href
    phref='<a[^>]* href="https://([^"]*)">([^<]*)</a>' #>([^"]*)</a>'
    result=re.compile(phref)
    href=re.findall(result,newtext)   
    print(*href, sep='\n')
    save_to_file(href)
    
    #5.διαγραφη tag
    def remove_html_tags(newtext):
        p = re.compile(r'<.*?>',re.DOTALL)
        return p.sub('', newtext)

    newtext=remove_html_tags(newtext)
    
    #6.html
    def htmlentities(m):
     if m.group(0) =='&amp;': return '&'
     if m.group(0) =='&gt;': return '>'
     if m.group(0) =='&lt;': return '<'
     if m.group(0) =='&nbsp;': return ' '
    result=re.compile(r'&(.*?);')
    newtext=result.sub(htmlentities,newtext)
    #7.space
    rexp = re.compile(r'\s+')   # αναγνώριση χαρακτήρων whitespace
    newtext = rexp.sub(' ',newtext)
    
    #8.print
    print(newtext)
    myfile.write(newtext)

    
        
    
    
