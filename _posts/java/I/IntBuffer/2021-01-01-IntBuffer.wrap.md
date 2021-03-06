---
title: IntBuffer.wrap()
permalink: /Java/IntBuffer/wrap/
date: 2021-01-11
key: Java.I.IntBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntBuffer.metodos valor="wrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static IntBuffer wrap(int[] array)
public static IntBuffer wrap(int[] array, int offset, int length)
~~~

## Parámetros
* **int[] array**,  {% include w3api/param_description.html metodo=_dato parametro="int[] array" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[IntBuffer](/Java/IntBuffer/)

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
