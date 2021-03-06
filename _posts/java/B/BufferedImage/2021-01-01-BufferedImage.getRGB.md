---
title: BufferedImage.getRGB()
permalink: /Java/BufferedImage/getRGB/
date: 2021-01-11
key: Java.B.BufferedImage
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="getRGB" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getRGB(int x, int y)
public int[] getRGB(int startX, int startY, int w, int h, int[] rgbArray, int offset, int scansize)
~~~

## Parámetros
* **int startX**,  {% include w3api/param_description.html metodo=_dato parametro="int startX" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int[] rgbArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] rgbArray" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_dato parametro="int scansize" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int startY**,  {% include w3api/param_description.html metodo=_dato parametro="int startY" %}

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
