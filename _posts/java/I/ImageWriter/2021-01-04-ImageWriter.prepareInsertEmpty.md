---
title: ImageWriter.prepareInsertEmpty()
permalink: Java/ImageWriter/prepareInsertEmpty
date: 2021-01-04
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
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata imageMetadata" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriteParam param" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_data parametro="ImageTypeSpecifier imageType" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **List&lt;? extends BufferedImage&gt; thumbnails**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends BufferedImage> thumbnails" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
