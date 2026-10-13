# Cómo publicar en coderLAT

1. Haz **fork** de este repositorio.
2. Copia `templates/articulo/` a `pages/02.blog/<slug-de-tu-articulo>/` (slug en minúsculas, sin tildes, con guiones).
3. Renombra el archivo a `item.es.md` y completa el encabezado (frontmatter) y el texto en Markdown. Imágenes: en la misma carpeta, referenciadas por nombre.
4. Abre un **Pull Request** hacia `main`. La validación automática te dirá si falta algo.
5. Revisamos, pedimos ajustes si hace falta y, al aprobar, se publica en el sitio.

## Encabezado obligatorio

```yaml
---
title: 'Título claro y específico'
date: '31-12-2026 10:00'      # dd-mm-aaaa hh:mm
author: tu-usuario-github
taxonomy:
    tool: [n8n]               # herramienta principal, en minúsculas
    resource: [tutorial]      # skill, plantilla, tutorial, glosario, automatizacion, ...
    country: [mexico]         # país de origen, sin tildes, en minúsculas
---
```

Las etiquetas van en minúsculas y sin tildes para que los filtros del sitio no se dupliquen (`n8n` y `N8N` serían filtros distintos).

## Criterios editoriales

- Resuelve un problema real, con pasos que otra persona pueda reproducir.
- Es contenido propio o con permiso; cita fuentes y licencias.
- No incluyas credenciales, datos personales ni información de clientes.
- Sin publicidad ni autopromoción encubierta.

## Sin git

Abre un Issue con la plantilla **Proponer solución**; lo convertimos en artículo y te damos el crédito como autor.
