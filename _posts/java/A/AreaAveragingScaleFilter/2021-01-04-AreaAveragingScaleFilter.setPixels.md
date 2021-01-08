---
title: AreaAveragingScaleFilter.setPixels()
permalink: Java/AreaAveragingScaleFilter/setPixels
date: 2021-01-04
key: JavaJava.A.AreaAveragingScaleFilter
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AreaAveragingScaleFilter.metodos valor="setPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPixels(int x, int y, int w, int h, ColorModel model, byte[] pixels, int off, int scansize)
public void setPixels(int x, int y, int w, int h, ColorModel model, int[] pixels, int off, int scansize)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **byte[] pixels**,  {% include w3api/param_description.html metodo=_data parametro="byte[] pixels" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_data parametro="int scansize" %}
* **int[] pixels**,  {% include w3api/param_description.html metodo=_data parametro="int[] pixels" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **ColorModel model**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel model" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[AreaAveragingScaleFilter](/Java/AreaAveragingScaleFilter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AreaAveragingScaleFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
