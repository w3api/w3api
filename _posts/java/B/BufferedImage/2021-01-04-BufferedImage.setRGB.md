---
title: BufferedImage.setRGB()
permalink: Java/BufferedImage/setRGB
date: 2021-01-04
key: JavaJava.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="setRGB" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRGB(int x, int y, int rgb)
public void setRGB(int startX, int startY, int w, int h, int[] rgbArray, int offset, int scansize)
~~~

## Parámetros
* **int scansize**,  {% include w3api/param_description.html metodo=_data parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int[] rgbArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] rgbArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int startX**,  {% include w3api/param_description.html metodo=_data parametro="int startX" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int rgb**,  {% include w3api/param_description.html metodo=_data parametro="int rgb" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int startY**,  {% include w3api/param_description.html metodo=_data parametro="int startY" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
