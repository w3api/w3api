---
title: ColorModel.getAlpha()
permalink: Java/ColorModel/getAlpha
date: 2021-01-11
key: JavaJava.C.ColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getAlpha" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getAlpha(int pixel)
public int getAlpha(Object inData)
~~~

## Parámetros
* **Object inData**,  {% include w3api/param_description.html metodo=_dato parametro="Object inData" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_dato parametro="int pixel" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

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
