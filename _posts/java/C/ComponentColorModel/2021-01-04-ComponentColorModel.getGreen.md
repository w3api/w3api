---
title: ComponentColorModel.getGreen()
permalink: Java/ComponentColorModel/getGreen
date: 2021-01-04
key: JavaJava.C.ComponentColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.metodos valor="getGreen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getGreen(int pixel)
public int getGreen(Object inData)
~~~

## Parámetros
* **Object inData**,  {% include w3api/param_description.html metodo=_data parametro="Object inData" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_data parametro="int pixel" %}

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
