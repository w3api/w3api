---
title: ImageConsumer.setPixels()
permalink: /Java/ImageConsumer/setPixels/
date: 2021-01-11
key: Java.I.ImageConsumer
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageConsumer.metodos valor="setPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPixels(int x, int y, int w, int h, ColorModel model, byte[] pixels, int off, int scansize)
void setPixels(int x, int y, int w, int h, ColorModel model, int[] pixels, int off, int scansize)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_dato parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **byte[] pixels**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] pixels" %}
* **int[] pixels**,  {% include w3api/param_description.html metodo=_dato parametro="int[] pixels" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **ColorModel model**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel model" %}

## Clase Padre
[ImageConsumer](/Java/ImageConsumer/)

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
