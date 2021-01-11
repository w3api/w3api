---
title: ComponentColorModel.coerceData()
permalink: Java/ComponentColorModel/coerceData
date: 2021-01-11
key: JavaJava.C.ComponentColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.metodos valor="coerceData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ColorModel coerceData(WritableRaster raster, boolean isAlphaPremultiplied)
~~~

## Parámetros
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **WritableRaster raster**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster raster" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ComponentColorModel](/Java/ComponentColorModel/)

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
