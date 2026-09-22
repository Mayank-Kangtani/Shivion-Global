import os
import glob

html_files = glob.glob(r'C:\Users\sanya\.gemini\antigravity\scratch\Shivion_Global\*.html')

dropdown_html = '''                    <li class="dropdown">
                        <a href="products.html">Our Products ▾</a>
                        <ul class="dropdown-menu">
                            <li><a href="products.html#fruits">Fruits</a></li>
                            <li><a href="products.html#spices">Spices</a></li>
                            <li><a href="products.html">Fresh Vegetables</a></li>
                            <li><a href="products.html">Peanuts</a></li>
                            <li><a href="products.html">Cereals</a></li>
                            <li><a href="products.html">Herbs</a></li>
                        </ul>
                    </li>'''

dropdown_html_active = dropdown_html.replace('<a href="products.html">Our Products', '<a href="products.html" class="active">Our Products')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('<li><a href="products.html">Our Products</a></li>', dropdown_html)
    content = content.replace('<li><a href="products.html" class="active">Our Products</a></li>', dropdown_html_active)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files with dropdown menu.")
