#!/usr/bin/env python3
"""
Script para descargar entradas de blog de Blogger a Markdown
Descarga el contenido y las imágenes, organizándolas en carpetas
"""

import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse
import html2text
import sys
from datetime import datetime
from dateutil import parser as date_parser

def sanitize_filename(filename):
    """Limpia el nombre del archivo para que sea válido en el sistema de archivos"""
    # Reemplaza caracteres no válidos
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    # Limita la longitud
    if len(filename) > 200:
        filename = filename[:200]
    return filename

def extract_publication_date(soup, url):
    """
    Extrae la fecha de publicación del post desde el HTML o URL
    
    Args:
        soup: BeautifulSoup object del HTML
        url: URL del post
    
    Returns:
        datetime object o None si no se puede extraer
    """
    # Método 1: Buscar en meta tags
    meta_date = None
    
    # Blogger format
    meta_tags = [
        ('meta', {'property': 'article:published_time'}),
        ('meta', {'property': 'og:published_time'}),
        ('meta', {'name': 'date'}),
        ('meta', {'itemprop': 'datePublished'}),
    ]
    
    for tag_name, attrs in meta_tags:
        meta_tag = soup.find(tag_name, attrs)
        if meta_tag and meta_tag.get('content'):
            try:
                meta_date = date_parser.parse(meta_tag.get('content'))
                print(f"  ✓ Fecha encontrada en meta tag: {meta_date.strftime('%Y-%m-%d')}")
                return meta_date
            except:
                pass
    
    # Método 2: Buscar en el contenido del post (Blogger específico)
    # Blogger suele tener la fecha en un span con class 'date-header' o similar
    date_selectors = [
        ('span', 'date-header'),
        ('span', 'post-date'),
        ('time', 'published'),
        ('span', 'published'),
        ('abbr', 'published'),
        ('time', 'entry-date'),
    ]
    
    for tag, class_name in date_selectors:
        date_elem = soup.find(tag, class_=class_name)
        if date_elem:
            date_text = date_elem.get_text().strip()
            try:
                parsed_date = date_parser.parse(date_text, fuzzy=True)
                print(f"  ✓ Fecha encontrada en contenido: {parsed_date.strftime('%Y-%m-%d')}")
                return parsed_date
            except:
                pass
    
    # Método 3: Extraer desde la URL (formato Blogger: /YYYY/MM/titulo.html)
    url_patterns = [
        r'/(\d{4})/(\d{2})/',  # /2023/11/
        r'(\d{4})-(\d{2})-(\d{2})',  # 2023-11-07
        r'/(\d{4})/(\d{2})/(\d{2})/',  # /2023/11/07/
    ]
    
    for pattern in url_patterns:
        match = re.search(pattern, url)
        if match:
            try:
                if len(match.groups()) == 2:
                    year, month = match.groups()
                    date_from_url = datetime(int(year), int(month), 1)
                else:
                    year, month, day = match.groups()
                    date_from_url = datetime(int(year), int(month), int(day))
                
                print(f"  ✓ Fecha extraída de URL: {date_from_url.strftime('%Y-%m-%d')}")
                return date_from_url
            except:
                pass
    
    print("  ⚠ No se encontró fecha, usando fecha actual")
    return None

def generate_slug(title):
    """
    Genera un slug URL-friendly a partir del título
    
    Args:
        title: Título del post
    
    Returns:
        String slug en minúsculas con guiones
    """
    # Convertir a minúsculas
    slug = title.lower()
    
    # Reemplazar caracteres acentuados comunes
    char_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ñ': 'n', 'ç': 'c',
    }
    
    for char, replacement in char_map.items():
        slug = slug.replace(char, replacement)
    
    # Reemplazar caracteres no alfanuméricos con guiones
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    
    # Reemplazar espacios y múltiples guiones con un solo guión
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    
    # Eliminar guiones al inicio y final
    slug = slug.strip('-')
    
    # Limitar longitud
    if len(slug) > 100:
        slug = slug[:100].rstrip('-')
    
    return slug

def format_date_folder_name(date_obj, slug, date_format='YYYYMMDD'):
    """
    Formatea el nombre de la carpeta con fecha y slug
    
    Args:
        date_obj: datetime object
        slug: String slug del título
        date_format: Formato de fecha ('YYYYMMDD', 'YYYY-MM-DD', etc.)
    
    Returns:
        String con nombre de carpeta formateado
    """
    if not date_obj:
        return slug
    
    if date_format == 'YYYYMMDD':
        date_prefix = date_obj.strftime('%Y%m%d')
    elif date_format == 'YYYY-MM-DD':
        date_prefix = date_obj.strftime('%Y-%m-%d')
    else:
        date_prefix = date_obj.strftime('%Y%m%d')
    
    return f"{date_prefix}-{slug}"

def download_image(img_url, images_folder, index):
    """Descarga una imagen y retorna el nombre del archivo local"""
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
        
        # Obtener extensión del archivo
        parsed_url = urlparse(img_url)
        path = parsed_url.path
        ext = os.path.splitext(path)[1]
        
        # Si no hay extensión, intentar obtenerla del Content-Type
        if not ext:
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            elif 'webp' in content_type:
                ext = '.webp'
            else:
                ext = '.jpg'  # Por defecto
        
        # Crear nombre de archivo
        filename = f"image_{index:03d}{ext}"
        filepath = os.path.join(images_folder, filename)
        
        # Guardar imagen
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"  ✓ Imagen descargada: {filename}")
        return filename
    
    except Exception as e:
        print(f"  ✗ Error descargando imagen {img_url}: {str(e)}")
        return None

def download_blog_post(url, output_folder=None, add_date_prefix=False, date_format='YYYYMMDD'):
    """
    Descarga una entrada de blog y la convierte a Markdown
    
    Args:
        url: URL de la entrada del blog
        output_folder: Carpeta donde guardar los archivos (opcional)
        add_date_prefix: Si es True, agrega prefijo de fecha al nombre de la carpeta
        date_format: Formato de fecha ('YYYYMMDD', 'YYYY-MM-DD')
    """
    print(f"\n📥 Descargando entrada desde: {url}")
    
    try:
        # Descargar la página
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraer el título
        title_tag = soup.find('h3', class_='post-title')
        if not title_tag:
            title_tag = soup.find('h1', class_='post-title')
        if not title_tag:
            title_tag = soup.find('title')
        
        title = title_tag.get_text().strip() if title_tag else "Sin título"
        print(f"📄 Título: {title}")
        
        # Extraer fecha de publicación si está habilitado
        post_date = None
        if add_date_prefix:
            print("📅 Extrayendo fecha de publicación...")
            post_date = extract_publication_date(soup, url)
        
        # Crear carpeta de salida (todas las conversiones van bajo conversions/)
        if output_folder is None:
            # Generar slug desde el título
            slug = generate_slug(title)

            # Si está habilitado el prefijo de fecha, usar formato con fecha
            if add_date_prefix and post_date:
                folder_name = format_date_folder_name(post_date, slug, date_format)
            else:
                folder_name = slug

            output_folder = os.path.join("conversions", folder_name)
        else:
            # Si se especifica una carpeta explícita, también anclarla a conversions/
            output_folder = os.path.join("conversions", os.path.basename(output_folder))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder, exist_ok=True)
        
        images_folder = os.path.join(output_folder, "images")
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        
        # Extraer el contenido del post
        post_body = soup.find('div', class_='post-body')
        if not post_body:
            post_body = soup.find('article')
        if not post_body:
            post_body = soup.find('div', class_='entry-content')
        
        if not post_body:
            print("❌ No se pudo encontrar el contenido del post")
            return False
        
        # Descargar imágenes y actualizar referencias
        images = post_body.find_all('img')
        print(f"\n🖼️  Encontradas {len(images)} imágenes")
        
        image_map = {}
        for idx, img in enumerate(images, 1):
            img_url = img.get('src')
            if not img_url:
                continue
            
            # Convertir URL relativa a absoluta
            img_url = urljoin(url, img_url)
            
            # Descargar imagen
            local_filename = download_image(img_url, images_folder, idx)
            
            if local_filename:
                image_map[img_url] = f"images/{local_filename}"
                # Actualizar el src en el HTML
                img['src'] = f"images/{local_filename}"
        
        # Convertir a Markdown
        print("\n📝 Convirtiendo a Markdown...")
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # No limitar el ancho
        h.unicode_snob = True
        h.escape_snob = False  # Evita escapar \(, \) en textos con paréntesis

        # Convertir el contenido
        markdown_content = h.handle(str(post_body))

        # Post-procesado: convertir imágenes enlazadas [![alt](local)](url) → ![local](url)
        # y asegurar que la ruta local de la imagen se mantenga
        def _fix_image_links(text):
            pattern = r'\[!\[([^\]]*)\]\(([^)]+)\)\]\([^)]+\)'
            def _repl(m):
                return f"![{m.group(1)}]({m.group(2)})"
            return re.sub(pattern, _repl, text)
        markdown_content = _fix_image_links(markdown_content)

        # Construir el documento final
        final_markdown = f"# {title}\n\n"
        final_markdown += f"**Fuente:** {url}\n\n"
        final_markdown += "---\n\n"
        final_markdown += markdown_content
        
        # Guardar el archivo Markdown
        markdown_filename = os.path.join(output_folder, "README.md")
        with open(markdown_filename, 'w', encoding='utf-8') as f:
            f.write(final_markdown)
        
        print(f"\n✅ Descarga completada!")
        print(f"📁 Archivos guardados en: {output_folder}/")
        print(f"   - README.md")
        print(f"   - images/ ({len(image_map)} imágenes)")
        
        return True
    
    except requests.RequestException as e:
        print(f"❌ Error al descargar la página: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Función principal del script"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Descarga entradas de blog y las convierte a Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Ejemplos:
  python3 blog_downloader.py 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'
  python3 blog_downloader.py 'https://tu-blog.com/entrada' --add-date
  python3 blog_downloader.py 'https://tu-blog.com/entrada' --add-date --date-format YYYY-MM-DD
  python3 blog_downloader.py 'https://tu-blog.com/entrada' 'mi-carpeta'
        '''
    )
    
    parser.add_argument('url', help='URL de la entrada del blog')
    parser.add_argument('output_folder', nargs='?', help='Carpeta de salida (opcional)')
    parser.add_argument('--add-date', action='store_true', 
                        help='Agrega prefijo de fecha al nombre de la carpeta (formato: YYYYMMDD-titulo)')
    parser.add_argument('--date-format', choices=['YYYYMMDD', 'YYYY-MM-DD'], default='YYYYMMDD',
                        help='Formato de fecha para el prefijo (default: YYYYMMDD)')
    
    args = parser.parse_args()
    
    success = download_blog_post(
        args.url, 
        args.output_folder,
        add_date_prefix=args.add_date,
        date_format=args.date_format
    )
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
