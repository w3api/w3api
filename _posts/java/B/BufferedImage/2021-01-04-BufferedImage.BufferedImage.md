---
title: BufferedImage.BufferedImage()
permalink: Java/BufferedImage/BufferedImage
date: 2021-01-04
key: JavaJava.B.BufferedImage
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
* **IndexColorModel cm**,  {% include w3api/param_description.html metodo=_data parametro="IndexColorModel cm" %}
* **WritableRaster raster**,  {% include w3api/param_description.html metodo=_data parametro="WritableRaster raster" %}
* **?&gt; properties**,  {% include w3api/param_description.html metodo=_data parametro="?> properties" %}
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel cm" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<?" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **int imageType**,  {% include w3api/param_description.html metodo=_data parametro="int imageType" %}
* **boolean isRasterPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isRasterPremultiplied" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}

## Excepciones
[RasterFormatException](/Java/RasterFormatException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
