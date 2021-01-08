---
title: PixelInterleavedSampleModel.PixelInterleavedSampleModel()
permalink: Java/PixelInterleavedSampleModel/PixelInterleavedSampleModel
date: 2021-01-04
key: JavaJava.P.PixelInterleavedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelInterleavedSampleModel.constructores valor="PixelInterleavedSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PixelInterleavedSampleModel(int dataType, int w, int h, int pixelStride, int scanlineStride, int[] bandOffsets)
~~~

## Parámetros
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **int pixelStride**,  {% include w3api/param_description.html metodo=_data parametro="int pixelStride" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int[] bandOffsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] bandOffsets" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PixelInterleavedSampleModel](/Java/PixelInterleavedSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PixelInterleavedSampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
