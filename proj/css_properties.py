import re

regex = re.compile('[-\w+ ]*: *[#\"-]*[\w\"]+[-\w\"%#/\\\, .]*')

def css_properties(st):
    
    props = regex.findall(st)
    li = []
    for i in props:
        #print(i)
        k,v = i.split(':')
        k = k.strip()
        v = v.strip()
        li.append((k,v))
    return li


print(css_properties("""
#LasVegas .billboard { text-decoration: blink; }

.ninja, #Snowden { visibility: hidden; }


.oliveoil
{
  -bla-z-index: #1;
  content: "";
}
.water
{
  k-z-index: 0/0 a;
}

#poop {
  float  : 1px solid #c0c0c0  #c0c0c0%;
  color  : #343434 ;

  width  : 0.61875rem  ;
  height : auto\\9 ;
}

.God { position: absolute; display: none; }
#blackhole { padding: -9999em; }

.word {  font-family:    "Comic Sans", "Times New Roman", sans-serif  ;  }
"""))
