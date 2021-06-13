---
title: DirectColorModel.getBlue()
permalink: /Java/DirectColorModel/getBlue/
date: 2021-01-11
key: Java.D.DirectColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="getBlue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int getBlue(int pixel)
public int getBlue(Object inData)
~~~

## Parámetros
* **Object inData**,  {% include w3api/param_description.html metodo=_dato parametro="Object inData" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_dato parametro="int pixel" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DirectColorModel](/Java/DirectColorModel/)

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
