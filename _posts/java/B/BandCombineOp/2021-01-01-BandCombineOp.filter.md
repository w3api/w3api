---
title: BandCombineOp.filter()
permalink: /Java/BandCombineOp/filter/
date: 2021-01-11
key: Java.B.BandCombineOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BandCombineOp.metodos valor="filter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WritableRaster filter(Raster src, WritableRaster dst)
~~~

## Parámetros
* **Raster src**,  {% include w3api/param_description.html metodo=_dato parametro="Raster src" %}
* **WritableRaster dst**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster dst" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BandCombineOp](/Java/BandCombineOp/)

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
