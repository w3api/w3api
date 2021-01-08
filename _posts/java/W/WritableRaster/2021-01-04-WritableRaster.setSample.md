---
title: WritableRaster.setSample()
permalink: Java/WritableRaster/setSample
date: 2021-01-04
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="setSample" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSample(int x, int y, int b, double s)
public void setSample(int x, int y, int b, float s)
public void setSample(int x, int y, int b, int s)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int s**,  {% include w3api/param_description.html metodo=_data parametro="int s" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}
* **float s**,  {% include w3api/param_description.html metodo=_data parametro="float s" %}
* **double s**,  {% include w3api/param_description.html metodo=_data parametro="double s" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

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
