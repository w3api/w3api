---
title: ArrayDeque.toArray()
permalink: /Java/ArrayDeque/toArray/
date: 2021-01-11
key: Java.A.ArrayDeque
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayDeque.metodos valor="toArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object[] toArray()
<T> T[] toArray(T[] a)
~~~

## Parámetros
* **T[] a**,  {% include w3api/param_description.html metodo=_dato parametro="T[] a" %}

## Clase Padre
[ArrayDeque](/Java/ArrayDeque/)

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
