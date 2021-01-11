---
title: LongBuffer.wrap()
permalink: Java/LongBuffer/wrap
date: 2021-01-11
key: JavaJava.L.LongBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongBuffer.metodos valor="wrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LongBuffer wrap(long[] array)
public static LongBuffer wrap(long[] array, int offset, int length)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **long[] array**,  {% include w3api/param_description.html metodo=_dato parametro="long[] array" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[LongBuffer](/Java/LongBuffer/)

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
