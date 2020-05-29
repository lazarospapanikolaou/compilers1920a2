import re

##Kανονικές εκφράσεις για την επίλυση των ζητούμενων 1,2,3,4,5,6,7



#Κανονικές εκφράσεις για το ζητούμενο 1 (Εξαγωγή και εκτύπωση του τίτλου (οτιδήποτε βρίσκεται μεταξύ <title> και </title>)
rexptitle = re.compile('<title>(.+?)</title>')
      print(m.group(1))      #Αποδεσμεύει το <title></title> το (+) καθώς επιτρέπει και το (?) να δεσμέυσει 


  
  
#Κανονικές εκφράσεις για το ζητούμενο 2 (Απαλοιφή των σχολίων (οτιδήποτε βρίσκεται μεταξύ <!-- και -->)
rexpcomments = re.compile('<!--.*?-->',re.DOTALL) #Προσθήκη και του newline με το re.DOTALL
    text = rexpcomments.sub(' ',text)
    print(text)
    
    
    
    
#Κανονικές εκφράσεις για το ζητούμενο 3 (Απαλοιφή των <script> και <style> tags με όλο τους το περιεχόμενο, μέχρι δηλαδή να
#συναντήσετε το αντίστοιχο </script> ή </style> (και τα τελευταία)
rexpscrsty = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)
    text = rexpscrsty.sub(' ',text)
    print(text)
    

    
    
#Κανονικές εκφράσεις για το ζητούμενο 4 (Εξαγωγή και εκτύπωση του συνδέσμου (ιδιότητα href) από <a> tags και του κειμένου τους
#(ό,τι βρίσκεται δηλαδή μεταξύ των <a> και </a>).
rexphref = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)
    text = fp.read()
    m = rexphref.search(text)
    for m in rexphref.finditer(text): 
        print('{} {}'.format(m.group(1),m.group(2)))  #Για την εξαγωγή των data που βρισκονται και μεσα στα href αλλα και μεσα στο <a>  


        
        
#Κανονικές εκφράσεις για το ζητούμενο 5 (Απαλοιφή όλων των tags από το κείμενο)
  #A. Tags με διπλο κλείσιμο.
rexpdoubletags = re.compile(r'<.+?>|</.+?>',re.DOTALL)
    text = rexpdoubletags.sub(' ',text) 
    print(text)
    
  #B. Tags με μονο κλεισιμο.
rexponetag = re.compile(r'<.+?/>',re.DOTALL)
     text = rexponetag.sub(' ',text)   
     print(text) 
    
    
    
#Κανονικές εκφράσεις για το ζητούμενο 6 (Μετατροπή των ειδικών HTML entities που υπάρχουν στο κείμενο σύμφωνα με τον παρακάτω
#πίνακα)
rexphtmlentities = re.compile(r'&(amp|gt|lt|nbsp);')
    m = rexphtmlentities.search(text)
    text = rexphtmlentities.sub(cb,text)
print(text)
        
def cb(m):
  if(m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&nbsp;'):
    return ' '
  
  
  
  #Κανονικές εκφράσεις για το ζητούμενο 7 (Μετατροπή ακολουθιών συνεχόμενων χαρακτήρων whitespace σε ένα ακριβώς κενό (εδώ όμως διατηρούμε τα σημεία στίξης!).
  rexpwhitespace = re.compile(r'\s+')
      text = fp.read()
    
  text = rexpwhitespace.sub(' ',text)  
  print(text)
  
  
  
  
  
  
#####Συνολικά ο κώδικας καλογραμμένος

import re

# arxika grafw tis kanonikes ekfraseis gia kathe zitoumeno

#gia to zitoumeno 1 
rexptitle = re.compile('<title>(.+?)</title>')


#gia to zitoumeno 2
rexpcomments = re.compile('<!--.*?-->',re.DOTALL)


#gia to zitoumeno 3
rexpscrsty = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)


#gia to zitoumeno 4
rexphref = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)


#gia to zitoumeno 5
#A. tags me diplo kleisimo
rexpdoubletags = re.compile(r'<.+?>|</.+?>',re.DOTALL)


#B. tags me mono kleisimo
rexponetag = re.compile(r'<.+?/>',re.DOTALL)


#gia to zitoumeno 6
rexphtmlentities = re.compile(r'&(amp|gt|lt|nbsp);')

#pinakas antikatastasis gia to zitoumeno 6
def cb(m):
  if(m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&nbsp;'):
    return ' '


#gia to zitoumeno 7
rexpwhitespace = re.compile(r'\s+')



#se auto to bima anoigoume to arxeio poy maw dinetai apo ekfvnhsh
#kai kaloume synarthsh gia na to diabasei kai na to kanei execute
with open('testpage.txt','r',encoding='utf-8') as fp:
   text = fp.read()
   m = rexptitle.search(text)
   
  #se auto to bhma ektypwnoume entoles diadoxika gia kathe zitoumeno
  #ektipvnoume gia to zitoumeno 1
   print(m.group(1))

   #ektipvnoume gia to zitoumeno 2
   text = rexpcomments.sub(' ',text)


   #ektipvnoume gia to zitoumeno 3
   text = rexpscrsty.sub(' ',text)

   
   #ektipvnoume gia to zitoumeno 4
   for m in rexphref.finditer(text): 
        print('{} {}'.format(m.group(1),m.group(2)))


   #A.ektipvnoume gia to zitoumeno 5a
   text = rexpdoubletags.sub(' ',text)


   #B.ektipvnoume gia to zitoumeno 5b
   text = rexponetag.sub(' ',text)


   #ektipvnoume gia to zitoumeno 6
   text = rexphtmlentities.sub(cb,text)
   m = rexphtmlentities.search(text)

   #ektipvnoume gia to zitoumeno 7
   text = rexpwhitespace.sub(' ',text) 


   # kanoume execute ta apotelesmata
   print(text)     

    
    
        
        
        
        
        
        
        
