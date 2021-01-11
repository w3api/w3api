---
title: DirectColorModel.getDataElement()
permalink: Java/DirectColorModel/getDataElement
date: 2021-01-11
key: JavaJava.D.DirectColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="getDataElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getDataElement(int[] components, int offset)
~~~

## Parámetros
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

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
