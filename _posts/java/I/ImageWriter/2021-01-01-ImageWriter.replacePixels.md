---
title: ImageWriter.replacePixels()
permalink: /Java/ImageWriter/replacePixels/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="replacePixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replacePixels(Raster raster, ImageWriteParam param) throws IOException
public void replacePixels(RenderedImage image, ImageWriteParam param) throws IOException
~~~

## Parámetros
* **RenderedImage image**,  {% include w3api/param_description.html metodo=_dato parametro="RenderedImage image" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **Raster raster**,  {% include w3api/param_description.html metodo=_dato parametro="Raster raster" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
