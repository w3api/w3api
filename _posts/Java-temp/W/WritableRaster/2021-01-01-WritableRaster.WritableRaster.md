---
title: WritableRaster.WritableRaster()
permalink: /Java/WritableRaster/WritableRaster/
date: 2021-01-11
key: Java.W.WritableRaster
category: Java
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
* **Point origin**,  {% include w3api/param_description.html metodo=_dato parametro="Point origin" %}
* **SampleModel sampleModel**,  {% include w3api/param_description.html metodo=_dato parametro="SampleModel sampleModel" %}
* **Point sampleModelTranslate**,  {% include w3api/param_description.html metodo=_dato parametro="Point sampleModelTranslate" %}
* **Rectangle aRegion**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle aRegion" %}
* **WritableRaster parent**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRaster parent" %}
* **DataBuffer dataBuffer**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer dataBuffer" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
