---
title: WritableRaster.setSample()
permalink: Java/WritableRaster/setSample
date: 2021-01-11
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
* **double s**,  {% include w3api/param_description.html metodo=_dato parametro="double s" %}
* **int s**,  {% include w3api/param_description.html metodo=_dato parametro="int s" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float s**,  {% include w3api/param_description.html metodo=_dato parametro="float s" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
