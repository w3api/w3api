---
title: ImageTypeSpecifier.getBitsPerBand()
permalink: /Java/ImageTypeSpecifier/getBitsPerBand/
date: 2021-01-11
key: Java.I.ImageTypeSpecifier
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="getBitsPerBand" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getBitsPerBand(int band)
~~~

## Parámetros
* **int band**,  {% include w3api/param_description.html metodo=_dato parametro="int band" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTypeSpecifier](/Java/ImageTypeSpecifier/)

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
