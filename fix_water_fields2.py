path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = """      water_pit: [
        {id:'depth',label:'Гүн (метр)',type:'number',def:'3.0',min:'1',step:'0.5'},
        {id:'diameter',label:'Диаметр (метр)',type:'number',def:'1.5',min:'0.8',step:'0.1'},
        {id:'cover_material',label:'Бүрхүүлийн материал',type:'select',opts:['бетон','тоосго']},
      ],"""

new = """      water_pit: [
        {id:'eng_count',label:'Тоо ширхэг',type:'number',def:'1',min:'1',step:'1'},
        {id:'depth',label:'Гүн (метр)',type:'number',def:'3.0',min:'1',step:'0.5'},
        {id:'diameter',label:'Диаметр (метр)',type:'number',def:'1.5',min:'0.8',step:'0.1'},
        {id:'cover_material',label:'Бүрхүүлийн материал',type:'select',opts:['бетон','тоосго','бетон цагираг (КС)']},
      ],"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Засагдлаа")
else:
    print("❌ Олдсонгүй")