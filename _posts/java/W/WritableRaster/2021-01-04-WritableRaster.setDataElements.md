---
title: WritableRaster.setDataElements()
permalink: Java/WritableRaster/setDataElements
date: 2021-01-04
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="setDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDataElements(int x, int y, int w, int h, Object inData)
public void setDataElements(int x, int y, Raster inRaster)
public void setDataElements(int x, int y, Object inData)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Raster inRaster**,  {% include w3api/param_description.html metodo=_data parametro="Raster inRaster" %}
* **Object inData**,  {% include w3api/param_description.html metodo=_data parametro="Object inData" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[WritableRaster](/Java/WritableRaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WritableRaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
