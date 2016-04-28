# pys test bot  

## Summary  

Test bot on [www.pys.com](http://www.pys.com)  

When fully functional, user will be able to purchase products from pys after executing python command `app.py` alongside a few agruments. 

Requires `mechanize` and `bs4`. If you install packages globally, change line 1 of `app.py` to your local python env (usually `#!/usr/bin/python`)

## Features  

**4/28/16** - product scraping is up and running. To run, type `python app.py` in the terminal. When running properly, output should look like this:  

```
Adidas Men Tubular Doom (gray / charcoal solid grey / metallic silver)  
Adidas...  
...  
Puma x Dee And Ricky Women Basket - CR (yellow / white)  
Puma...  
...  
The Hundreds Johnson Low Top Suede (burgundy)  
The Hundreds...  
...
```  

Next feature will be adding items to cart.