content = open("apps/registry/templates/registry/ad_create.html", "r", encoding="utf-8").read()

# Wrap-ын grid-г засах — sidebar-г баруун талд, form-г бүтэн
old = '    .wrap{max-width:860px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 240px;gap:16px;}'
new = '    .wrap{max-width:960px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 220px;gap:16px;}'

content = content.replace(old, new, 1)

# Mobile responsive нэмэх
old2 = '    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.sb{display:none;}.main-cats{grid-template-columns:1fr 1fr;}}'
new2 = '''    @media(max-width:900px){
      .wrap{grid-template-columns:1fr;padding:0 12px;}
      .sb{display:none;}
      .main-cats{grid-template-columns:1fr 1fr;}
      .field-row{grid-template-columns:1fr;}
      .form-body{padding:14px;}
    }
    @media(max-width:480px){
      .main-cats{grid-template-columns:1fr 1fr;}
      .subcat-hd{font-size:12px;}
    }'''

content = content.replace(old2, new2, 1)

open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8").write(content)
print("OK")