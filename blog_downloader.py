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

def sanitize_filename(filename):
    """Limpia el nombre del archivo para que sea válido en el sistema de archivos"""
    # Reemplaza caracteres no válidos
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    # Limita la longitud
    if len(filename) > 200:
        filename = filename[:200]
    return filename

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

def download_blog_post(url, output_folder=None):
    """
    Descarga una entrada de blog y la convierte a Markdown
    
    Args:
        url: URL de la entrada del blog
        output_folder: Carpeta donde guardar los archivos (opcional)
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
        
        # Crear carpeta de salida
        if output_folder is None:
            output_folder = sanitize_filename(title)
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
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
        h.escape_snob = True
        
        # Convertir el contenido
        markdown_content = h.handle(str(post_body))
        
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
    if len(sys.argv) < 2:
        print("Uso: python3 blog_downloader.py <URL> [carpeta_salida]")
        print("\nEjemplo:")
        print("  python3 blog_downloader.py 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'")
        print("  python3 blog_downloader.py 'https://tu-blog.com/entrada' 'mi-carpeta'")
        sys.exit(1)
    
    url = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = download_blog_post(url, output_folder)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
