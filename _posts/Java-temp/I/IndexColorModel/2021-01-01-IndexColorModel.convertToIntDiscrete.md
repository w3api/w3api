---
title: IndexColorModel.convertToIntDiscrete()
permalink: /Java/IndexColorModel/convertToIntDiscrete/
date: 2021-01-11
key: Java.I.IndexColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexColorModel.metodos valor="convertToIntDiscrete" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage convertToIntDiscrete(Raster raster, boolean forceARGB)
~~~

## Parámetros
* **boolean forceARGB**,  {% include w3api/param_description.html metodo=_dato parametro="boolean forceARGB" %}
* **Raster raster**,  {% include w3api/param_description.html metodo=_dato parametro="Raster raster" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IndexColorModel](/Java/IndexColorModel/)

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
