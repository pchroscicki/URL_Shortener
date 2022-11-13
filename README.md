# URL_Shortener

Aim:    
URL_Shortener is a web-based application, which accepts provided url from anonymous user and returns a unique and shorter alternative url in a format: [domain]/[alias].

Description:    
    1) Provided url has to contain: "https://" or "http:// prefix.      
    2) The url alias is displayed after filling and sending the form.   
    3) Application deletes aliases which are not visited for more than 48h automatically.       
    4) Application has user-friendly admin interface to display database with all objects details.     

Methodology for unique alias generation:        
The url alias is generates as 10-element-long string composed of:       
    - 2-7 upper or lower case letters   
    - at least 3 digits         
 The last element is always a digit, which indicates a total number of letters within this alias.   
 If the generated alias is unique, it is saved and displayed to the user.   

Technology stack:       
    • Python3   
    • Django    
    • PosgreSQL         
    • Docker    
    • Pytest    
