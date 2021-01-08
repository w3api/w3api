---
title: ComponentColorModel.getDataElement()
permalink: Java/ComponentColorModel/getDataElement
date: 2021-01-04
key: JavaJava.C.ComponentColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.metodos valor="getDataElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getDataElement(float[] normComponents, int normOffset)
public int getDataElement(int[] components, int offset)
~~~

## Parámetros
* **int normOffset**,  {% include w3api/param_description.html metodo=_data parametro="int normOffset" %}
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_data parametro="float[] normComponents" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_data parametro="int[] components" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
