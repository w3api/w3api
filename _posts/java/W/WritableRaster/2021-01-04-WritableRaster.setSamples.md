---
title: WritableRaster.setSamples()
permalink: Java/WritableRaster/setSamples
date: 2021-01-04
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="setSamples" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSamples(int x, int y, int w, int h, int b, double[] dArray)
public void setSamples(int x, int y, int w, int h, int b, float[] fArray)
public void setSamples(int x, int y, int w, int h, int b, int[] iArray)
~~~

## Parámetros
* **int[] iArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] iArray" %}
* **float[] fArray**,  {% include w3api/param_description.html metodo=_data parametro="float[] fArray" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **double[] dArray**,  {% include w3api/param_description.html metodo=_data parametro="double[] dArray" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}
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
