---
title: ComponentColorModel.coerceData()
permalink: Java/ComponentColorModel/coerceData
date: 2021-01-04
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
* **WritableRaster raster**,  {% include w3api/param_description.html metodo=_data parametro="WritableRaster raster" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}

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
{%- for _ldc in site.data.Java.C.ComponentColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
