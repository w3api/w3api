---
title: IndexColorModel.getDataElements()
permalink: /Java/IndexColorModel/getDataElements/
date: 2021-01-11
key: Java.I.IndexColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexColorModel.metodos valor="getDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getDataElements(int[] components, int offset, Object pixel)
public Object getDataElements(int rgb, Object pixel)
~~~

## Parámetros
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **int rgb**,  {% include w3api/param_description.html metodo=_dato parametro="int rgb" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **Object pixel**,  {% include w3api/param_description.html metodo=_dato parametro="Object pixel" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[IndexColorModel](/Java/IndexColorModel/)

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
