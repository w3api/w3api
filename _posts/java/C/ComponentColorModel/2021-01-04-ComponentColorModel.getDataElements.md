---
title: ComponentColorModel.getDataElements()
permalink: Java/ComponentColorModel/getDataElements
date: 2021-01-04
key: JavaJava.C.ComponentColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.metodos valor="getDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getDataElements(float[] normComponents, int normOffset, Object obj)
public Object getDataElements(int[] components, int offset, Object obj)
public Object getDataElements(int rgb, Object pixel)
~~~

## Parámetros
* **Object pixel**,  {% include w3api/param_description.html metodo=_data parametro="Object pixel" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_data parametro="float[] normComponents" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_data parametro="int[] components" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int rgb**,  {% include w3api/param_description.html metodo=_data parametro="int rgb" %}
* **int normOffset**,  {% include w3api/param_description.html metodo=_data parametro="int normOffset" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ComponentColorModel](/Java/ComponentColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComponentColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
