---
title: ColorConvertOp.filter()
permalink: /Java/ColorConvertOp/filter/
date: 2021-01-11
key: Java.C.ColorConvertOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorConvertOp.metodos valor="filter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final BufferedImage filter(BufferedImage src, BufferedImage dest)
public final WritableRaster filter(Raster src, WritableRaster dest)
~~~

## Parámetros
* **Raster src**,  {% include w3api/param_description.html metodo=_dato parametro="Raster src" %}
* **BufferedImage src**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage src" %}
* **WritableRaster dest**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster dest" %}
* **BufferedImage dest**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage dest" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ColorConvertOp](/Java/ColorConvertOp/)

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
