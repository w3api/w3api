---
title: ColorModel.getComponents()
permalink: Java/ColorModel/getComponents
date: 2021-01-04
key: JavaJava.C.ColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getComponents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] getComponents(int pixel, int[] components, int offset)
public int[] getComponents(Object pixel, int[] components, int offset)
~~~

## Parámetros
* **Object pixel**,  {% include w3api/param_description.html metodo=_data parametro="Object pixel" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_data parametro="int pixel" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_data parametro="int[] components" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
