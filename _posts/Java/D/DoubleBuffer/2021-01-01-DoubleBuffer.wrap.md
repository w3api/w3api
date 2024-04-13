---
title: DoubleBuffer.wrap()
permalink: /Java/DoubleBuffer/wrap/
date: 2021-01-11
key: Java.D.DoubleBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleBuffer.metodos valor="wrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DoubleBuffer wrap(double[] array)
public static DoubleBuffer wrap(double[] array, int offset, int length)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **double[] array**,  {% include w3api/param_description.html metodo=_dato parametro="double[] array" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[DoubleBuffer](/Java/DoubleBuffer/)

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
