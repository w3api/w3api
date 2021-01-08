---
title: MultiPixelPackedSampleModel.getSample()
permalink: Java/MultiPixelPackedSampleModel/getSample
date: 2021-01-04
key: JavaJava.M.MultiPixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiPixelPackedSampleModel.metodos valor="getSample" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getSample(int x, int y, int b, DataBuffer data)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_data parametro="DataBuffer data" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.M.MultiPixelPackedSampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
