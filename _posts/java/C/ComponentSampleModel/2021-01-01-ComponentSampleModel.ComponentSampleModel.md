---
title: ComponentSampleModel.ComponentSampleModel()
permalink: /Java/ComponentSampleModel/ComponentSampleModel/
date: 2021-01-11
key: Java.C.ComponentSampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentSampleModel.constructores valor="ComponentSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComponentSampleModel(int dataType, int w, int h, int pixelStride, int scanlineStride, int[] bandOffsets)
public ComponentSampleModel(int dataType, int w, int h, int pixelStride, int scanlineStride, int[] bankIndices, int[] bandOffsets)
~~~

## Parámetros
* **int[] bankIndices**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bankIndices" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **int pixelStride**,  {% include w3api/param_description.html metodo=_dato parametro="int pixelStride" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **int[] bandOffsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bandOffsets" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ComponentSampleModel](/Java/ComponentSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
