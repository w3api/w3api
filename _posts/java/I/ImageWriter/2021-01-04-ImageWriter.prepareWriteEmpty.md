---
title: ImageWriter.prepareWriteEmpty()
permalink: Java/ImageWriter/prepareWriteEmpty
date: 2021-01-04
key: JavaJava.I.ImageWriter
category: java
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
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata imageMetadata" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriteParam param" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_data parametro="ImageTypeSpecifier imageType" %}
* **IIOMetadata streamMetadata**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata streamMetadata" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **List&lt;? extends BufferedImage&gt; thumbnails**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends BufferedImage> thumbnails" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
