---
title: ColorConvertOp.createCompatibleDestRaster()
permalink: /Java/ColorConvertOp/createCompatibleDestRaster/
date: 2021-01-11
key: Java.C.ColorConvertOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorConvertOp.metodos valor="createCompatibleDestRaster" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WritableRaster createCompatibleDestRaster(Raster src)
~~~

## Parámetros
* **Raster src**,  {% include w3api/param_description.html metodo=_dato parametro="Raster src" %}

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
