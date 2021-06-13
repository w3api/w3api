---
title: RGBImageFilter.filterRGBPixels()
permalink: Java/RGBImageFilter/filterRGBPixels
date: 2021-01-11
key: Java.R.RGBImageFilter
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RGBImageFilter.metodos valor="filterRGBPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void filterRGBPixels(int x, int y, int w, int h, int[] pixels, int off, int scansize)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_dato parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] pixels**,  {% include w3api/param_description.html metodo=_dato parametro="int[] pixels" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Clase Padre
[RGBImageFilter](/Java/RGBImageFilter/)

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
