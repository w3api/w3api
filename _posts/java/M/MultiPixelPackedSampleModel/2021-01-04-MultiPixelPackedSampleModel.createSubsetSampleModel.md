---
title: MultiPixelPackedSampleModel.createSubsetSampleModel()
permalink: Java/MultiPixelPackedSampleModel/createSubsetSampleModel
date: 2021-01-04
key: JavaJava.M.MultiPixelPackedSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiPixelPackedSampleModel.metodos valor="createSubsetSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SampleModel createSubsetSampleModel(int[] bands)
~~~

## Parámetros
* **int[] bands**,  {% include w3api/param_description.html metodo=_data parametro="int[] bands" %}

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
