---
title: DirectColorModel.coerceData()
permalink: Java/DirectColorModel/coerceData
date: 2021-01-04
key: JavaJava.D.DirectColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="coerceData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final ColorModel coerceData(WritableRaster raster, boolean isAlphaPremultiplied)
~~~

## Parámetros
* **WritableRaster raster**,  {% include w3api/param_description.html metodo=_data parametro="WritableRaster raster" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DirectColorModel](/Java/DirectColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
