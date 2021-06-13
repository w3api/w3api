---
title: BufferedImage.isTileWritable()
permalink: /Java/BufferedImage/isTileWritable/
date: 2021-01-11
key: Java.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="isTileWritable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isTileWritable(int tileX, int tileY)
~~~

## Parámetros
* **int tileY**,  {% include w3api/param_description.html metodo=_dato parametro="int tileY" %}
* **int tileX**,  {% include w3api/param_description.html metodo=_dato parametro="int tileX" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

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
