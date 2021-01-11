---
title: ImageWriter.prepareInsertEmpty()
permalink: Java/ImageWriter/prepareInsertEmpty
date: 2021-01-11
key: JavaJava.I.ImageWriter
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="prepareInsertEmpty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void prepareInsertEmpty(int imageIndex, ImageTypeSpecifier imageType, int width, int height, IIOMetadata imageMetadata, List<? extends BufferedImage> thumbnails, ImageWriteParam param) throws IOException
~~~

## Parámetros
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_dato parametro="ImageTypeSpecifier imageType" %}
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata imageMetadata" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **List&lt;? extends BufferedImage&gt; thumbnails**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends BufferedImage> thumbnails" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

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
