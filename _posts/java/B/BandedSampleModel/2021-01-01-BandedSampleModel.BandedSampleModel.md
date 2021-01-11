---
title: BandedSampleModel.BandedSampleModel()
permalink: Java/BandedSampleModel/BandedSampleModel
date: 2021-01-11
key: JavaJava.B.BandedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BandedSampleModel.constructores valor="BandedSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BandedSampleModel(int dataType, int w, int h, int numBands)
public BandedSampleModel(int dataType, int w, int h, int scanlineStride, int[] bankIndices, int[] bandOffsets)
~~~

## Parámetros
* **int[] bankIndices**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bankIndices" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **int numBands**,  {% include w3api/param_description.html metodo=_dato parametro="int numBands" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **int[] bandOffsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bandOffsets" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BandedSampleModel](/Java/BandedSampleModel/)

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
