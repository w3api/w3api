---
title: ImageReader.readTileRaster()
permalink: /Java/ImageReader/readTileRaster/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="readTileRaster" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Raster readTileRaster(int imageIndex, int tileX, int tileY) throws IOException
~~~

## Parámetros
* **int tileY**,  {% include w3api/param_description.html metodo=_dato parametro="int tileY" %}
* **int tileX**,  {% include w3api/param_description.html metodo=_dato parametro="int tileX" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ImageReader](/Java/ImageReader/)

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
