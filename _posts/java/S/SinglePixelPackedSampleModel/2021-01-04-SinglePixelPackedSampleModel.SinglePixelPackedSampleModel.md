---
title: SinglePixelPackedSampleModel.SinglePixelPackedSampleModel()
permalink: Java/SinglePixelPackedSampleModel/SinglePixelPackedSampleModel
date: 2021-01-04
key: JavaJava.S.SinglePixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SinglePixelPackedSampleModel.constructores valor="SinglePixelPackedSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SinglePixelPackedSampleModel(int dataType, int w, int h, int[] bitMasks)
public SinglePixelPackedSampleModel(int dataType, int w, int h, int scanlineStride, int[] bitMasks)
~~~

## Parámetros
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **int[] bitMasks**,  {% include w3api/param_description.html metodo=_data parametro="int[] bitMasks" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SinglePixelPackedSampleModel](/Java/SinglePixelPackedSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SinglePixelPackedSampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
