---
title: WritableRaster.WritableRaster()
permalink: Java/WritableRaster/WritableRaster
date: 2021-01-04
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.constructores valor="WritableRaster" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected WritableRaster(SampleModel sampleModel, DataBuffer dataBuffer, Point origin)
protected WritableRaster(SampleModel sampleModel, DataBuffer dataBuffer, Rectangle aRegion, Point sampleModelTranslate, WritableRaster parent)
protected WritableRaster(SampleModel sampleModel, Point origin)
~~~

## Parámetros
* **SampleModel sampleModel**,  {% include w3api/param_description.html metodo=_data parametro="SampleModel sampleModel" %}
* **DataBuffer dataBuffer**,  {% include w3api/param_description.html metodo=_data parametro="DataBuffer dataBuffer" %}
* **WritableRaster parent**,  {% include w3api/param_description.html metodo=_data parametro="WritableRaster parent" %}
* **Point origin**,  {% include w3api/param_description.html metodo=_data parametro="Point origin" %}
* **Point sampleModelTranslate**,  {% include w3api/param_description.html metodo=_data parametro="Point sampleModelTranslate" %}
* **Rectangle aRegion**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle aRegion" %}

## Excepciones
[RasterFormatException](/Java/RasterFormatException/)

## Clase Padre
[WritableRaster](/Java/WritableRaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WritableRaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
