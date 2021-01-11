---
title: MultiPixelPackedSampleModel.setSample()
permalink: Java/MultiPixelPackedSampleModel/setSample
date: 2021-01-11
key: JavaJava.M.MultiPixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiPixelPackedSampleModel.metodos valor="setSample" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSample(int x, int y, int b, int s, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int s**,  {% include w3api/param_description.html metodo=_dato parametro="int s" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[MultiPixelPackedSampleModel](/Java/MultiPixelPackedSampleModel/)

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
