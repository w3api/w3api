---
title: AtomicLongArray.AtomicLongArray()
permalink: Java/AtomicLongArray/AtomicLongArray
date: 2021-01-11
key: JavaJava.A.AtomicLongArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongArray.constructores valor="AtomicLongArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AtomicLongArray(int length)
public AtomicLongArray(long[] array)
~~~

## Parámetros
* **long[] array**,  {% include w3api/param_description.html metodo=_dato parametro="long[] array" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AtomicLongArray](/Java/AtomicLongArray/)

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
