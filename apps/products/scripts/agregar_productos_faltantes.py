import csv
from apps.products.models import Product

csv_file_path = r'D:\Users\v52anap\Documents\Potencial de compra.csv'
litros_col = 'Litros Potenciales'
productos_faltantes = set()

# Extraer productos no encontrados del archivo de potenciales
with open(csv_file_path, newline='', encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        producto_nombre = row['Producto'].strip()
        producto_nombre_normalizado = producto_nombre.upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('Ñ','N').replace('  ',' ').replace(' /','/').replace('/ ','/').replace(' SAE',' SAE').replace('API ','API ').replace('PLUS','PLUS').replace('GL-5','GL-5').replace('CF','CF').replace('CI-4','CI-4').replace('TBN','TBN').replace('DOT','DOT').replace('JASO','JASO').replace('MA/MA-2','MA/MA-2').replace('SP/SN','SP/SN').replace('SN/SL','SN/SL').replace('SP','SP').replace('SN','SN').replace('SL','SL').replace(' ',' ')
        # Verificar si existe en la base de datos
        existe = Product.objects.filter(name__iexact=producto_nombre_normalizado).exists()
        if not existe:
            productos_faltantes.add(producto_nombre_normalizado)

# Agregar productos faltantes
for nombre in productos_faltantes:
    if not Product.objects.filter(name__iexact=nombre).exists():
        Product.objects.create(name=nombre)
        print(f"Producto agregado: {nombre}")
