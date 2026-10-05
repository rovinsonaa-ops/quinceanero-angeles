with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('build.py', 'w', encoding='utf-8') as f:
    f.write('import os\n\noutput_path = r"C:\\Users\\Rovinson\\.gemini\\antigravity\\scratch\\quinceanero-angeles\\index.html"\n\nhtml_code = """' + html + '"""\n\nwith open(output_path, "w", encoding="utf-8") as out_f:\n    out_f.write(html_code)\n\nprint("Build compiled successfully!")\n')

print("Sync completed!")
