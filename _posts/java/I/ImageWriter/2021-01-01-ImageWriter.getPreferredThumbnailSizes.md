---
title: ImageWriter.getPreferredThumbnailSizes()
permalink: /Java/ImageWriter/getPreferredThumbnailSizes/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="getPreferredThumbnailSizes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Dimension[] getPreferredThumbnailSizes(ImageTypeSpecifier imageType, ImageWriteParam param, IIOMetadata streamMetadata, IIOMetadata imageMetadata)
~~~

## Parámetros
* **IIOMetadata streamMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata streamMetadata" %}
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_dato parametro="ImageTypeSpecifier imageType" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata imageMetadata" %}

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
