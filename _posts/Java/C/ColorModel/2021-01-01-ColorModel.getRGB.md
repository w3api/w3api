---
title: ColorModel.getRGB()
permalink: /Java/ColorModel/getRGB/
date: 2021-01-11
key: Java.C.ColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getRGB" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getRGB(int pixel)
public int getRGB(Object inData)
~~~

## Parámetros
* **Object inData**,  {% include w3api/param_description.html metodo=_dato parametro="Object inData" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_dato parametro="int pixel" %}

## Clase Padre
[ColorModel](/Java/ColorModel/)

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
