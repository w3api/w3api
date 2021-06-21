---
title: ImageWriter.prepareWriteEmpty()
permalink: /Java/ImageWriter/prepareWriteEmpty/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="prepareWriteEmpty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void prepareWriteEmpty(IIOMetadata streamMetadata, ImageTypeSpecifier imageType, int width, int height, IIOMetadata imageMetadata, List<? extends BufferedImage> thumbnails, ImageWriteParam param) throws IOException
~~~

## Parámetros
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_dato parametro="ImageTypeSpecifier imageType" %}
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata imageMetadata" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **IIOMetadata streamMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata streamMetadata" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **List&lt;? extends BufferedImage&gt; thumbnails**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends BufferedImage> thumbnails" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
