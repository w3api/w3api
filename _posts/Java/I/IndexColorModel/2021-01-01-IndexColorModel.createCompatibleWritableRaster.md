---
title: IndexColorModel.createCompatibleWritableRaster()
permalink: /Java/IndexColorModel/createCompatibleWritableRaster/
date: 2021-01-11
key: Java.I.IndexColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexColorModel.metodos valor="createCompatibleWritableRaster" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WritableRaster createCompatibleWritableRaster(int w, int h)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
