---
title: DirectColorModel.getDataElements()
permalink: Java/DirectColorModel/getDataElements
date: 2021-01-11
key: JavaJava.D.DirectColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="getDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getDataElements(int[] components, int offset, Object obj)
public Object getDataElements(int rgb, Object pixel)
~~~

## Parámetros
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **Object pixel**,  {% include w3api/param_description.html metodo=_dato parametro="Object pixel" %}
* **int rgb**,  {% include w3api/param_description.html metodo=_dato parametro="int rgb" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DirectColorModel](/Java/DirectColorModel/)

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
