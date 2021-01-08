---
title: WritableRaster.setRect()
permalink: Java/WritableRaster/setRect
date: 2021-01-04
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="setRect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRect(int dx, int dy, Raster srcRaster)
public void setRect(Raster srcRaster)
~~~

## Parámetros
* **int dy**,  {% include w3api/param_description.html metodo=_data parametro="int dy" %}
* **Raster srcRaster**,  {% include w3api/param_description.html metodo=_data parametro="Raster srcRaster" %}
* **int dx**,  {% include w3api/param_description.html metodo=_data parametro="int dx" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
