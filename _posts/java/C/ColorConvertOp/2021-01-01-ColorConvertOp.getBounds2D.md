---
title: ColorConvertOp.getBounds2D()
permalink: /Java/ColorConvertOp/getBounds2D/
date: 2021-01-11
key: Java.C.ColorConvertOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorConvertOp.metodos valor="getBounds2D" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Rectangle2D getBounds2D(BufferedImage src)
public final Rectangle2D getBounds2D(Raster src)
~~~

## Parámetros
* **Raster src**,  {% include w3api/param_description.html metodo=_dato parametro="Raster src" %}
* **BufferedImage src**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage src" %}

## Clase Padre
[ColorConvertOp](/Java/ColorConvertOp/)

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
