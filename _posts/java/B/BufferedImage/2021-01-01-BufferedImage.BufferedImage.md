---
title: BufferedImage.BufferedImage()
permalink: /Java/BufferedImage/BufferedImage/
date: 2021-01-11
key: Java.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.constructores valor="BufferedImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage(int width, int height, int imageType)
public BufferedImage(int width, int height, int imageType, IndexColorModel cm)
public BufferedImage(ColorModel cm, WritableRaster raster, boolean isRasterPremultiplied, Hashtable<?,?> properties)
~~~

## Parámetros
* **?&gt; properties**,  {% include w3api/param_description.html metodo=_dato parametro="?> properties" %}
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel cm" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **WritableRaster raster**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster raster" %}
* **boolean isRasterPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isRasterPremultiplied" %}
* **IndexColorModel cm**,  {% include w3api/param_description.html metodo=_dato parametro="IndexColorModel cm" %}
* **int imageType**,  {% include w3api/param_description.html metodo=_dato parametro="int imageType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RasterFormatException](/Java/RasterFormatException/)

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

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
