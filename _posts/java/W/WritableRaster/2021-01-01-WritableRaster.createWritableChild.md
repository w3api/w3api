---
title: WritableRaster.createWritableChild()
permalink: /Java/WritableRaster/createWritableChild/
date: 2021-01-11
key: Java.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="createWritableChild" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WritableRaster createWritableChild(int parentX, int parentY, int w, int h, int childMinX, int childMinY, int[] bandList)
~~~

## Parámetros
* **int parentY**,  {% include w3api/param_description.html metodo=_dato parametro="int parentY" %}
* **int[] bandList**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bandList" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int parentX**,  {% include w3api/param_description.html metodo=_dato parametro="int parentX" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int childMinY**,  {% include w3api/param_description.html metodo=_dato parametro="int childMinY" %}
* **int childMinX**,  {% include w3api/param_description.html metodo=_dato parametro="int childMinX" %}

## Excepciones
[RasterFormatException](/Java/RasterFormatException/)

## Clase Padre
[WritableRaster](/Java/WritableRaster/)

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
