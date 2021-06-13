---
title: MultiPixelPackedSampleModel.getDataElements()
permalink: Java/MultiPixelPackedSampleModel/getDataElements
date: 2021-01-11
key: JavaJava.M.MultiPixelPackedSampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiPixelPackedSampleModel.metodos valor="getDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getDataElements(int x, int y, Object obj, DataBuffer data)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

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
