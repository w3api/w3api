---
title: DirectColorModel.getComponents()
permalink: /Java/DirectColorModel/getComponents/
date: 2021-01-11
key: Java.D.DirectColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="getComponents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int[] getComponents(int pixel, int[] components, int offset)
public final int[] getComponents(Object pixel, int[] components, int offset)
~~~

## Parámetros
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_dato parametro="int pixel" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **Object pixel**,  {% include w3api/param_description.html metodo=_dato parametro="Object pixel" %}

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
