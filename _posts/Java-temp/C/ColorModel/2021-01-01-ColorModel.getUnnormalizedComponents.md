---
title: ColorModel.getUnnormalizedComponents()
permalink: /Java/ColorModel/getUnnormalizedComponents/
date: 2021-01-11
key: Java.C.ColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getUnnormalizedComponents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] getUnnormalizedComponents(float[] normComponents, int normOffset, int[] components, int offset)
~~~

## Parámetros
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_dato parametro="float[] normComponents" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int normOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int normOffset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

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
