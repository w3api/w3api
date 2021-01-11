---
title: SinglePixelPackedSampleModel.getPixel()
permalink: Java/SinglePixelPackedSampleModel/getPixel
date: 2021-01-11
key: JavaJava.S.SinglePixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SinglePixelPackedSampleModel.metodos valor="getPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] getPixel(int x, int y, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] iArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] iArray" %}

## Clase Padre
[SinglePixelPackedSampleModel](/Java/SinglePixelPackedSampleModel/)

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
