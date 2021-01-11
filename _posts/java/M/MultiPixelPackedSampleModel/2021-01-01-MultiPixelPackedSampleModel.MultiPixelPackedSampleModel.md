---
title: MultiPixelPackedSampleModel.MultiPixelPackedSampleModel()
permalink: Java/MultiPixelPackedSampleModel/MultiPixelPackedSampleModel
date: 2021-01-11
key: JavaJava.M.MultiPixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiPixelPackedSampleModel.constructores valor="MultiPixelPackedSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MultiPixelPackedSampleModel(int dataType, int w, int h, int numberOfBits)
public MultiPixelPackedSampleModel(int dataType, int w, int h, int numberOfBits, int scanlineStride, int dataBitOffset)
~~~

## Parámetros
* **int numberOfBits**,  {% include w3api/param_description.html metodo=_dato parametro="int numberOfBits" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **int dataBitOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int dataBitOffset" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RasterFormatException](/Java/RasterFormatException/)

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
