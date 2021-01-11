---
title: AffineTransformOp.filter()
permalink: Java/AffineTransformOp/filter
date: 2021-01-10
key: JavaJava.A.AffineTransformOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransformOp.metodos valor="filter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final BufferedImage filter(BufferedImage src, BufferedImage dst)
public final WritableRaster filter(Raster src, WritableRaster dst)
~~~

## Parámetros
* **WritableRaster dst**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster dst" %}
* **BufferedImage src**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage src" %}
* **Raster src**,  {% include w3api/param_description.html metodo=_dato parametro="Raster src" %}
* **BufferedImage dst**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage dst" %}

## Excepciones
[ImagingOpException](/Java/ImagingOpException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AffineTransformOp](/Java/AffineTransformOp/)

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
