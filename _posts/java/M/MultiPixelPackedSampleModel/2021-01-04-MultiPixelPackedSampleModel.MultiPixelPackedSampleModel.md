---
title: MultiPixelPackedSampleModel.MultiPixelPackedSampleModel()
permalink: Java/MultiPixelPackedSampleModel/MultiPixelPackedSampleModel
date: 2021-01-04
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
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **int numberOfBits**,  {% include w3api/param_description.html metodo=_data parametro="int numberOfBits" %}
* **int dataBitOffset**,  {% include w3api/param_description.html metodo=_data parametro="int dataBitOffset" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

## Excepciones
[RasterFormatException](/Java/RasterFormatException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
