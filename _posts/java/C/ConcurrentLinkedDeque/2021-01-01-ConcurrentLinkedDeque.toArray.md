---
title: ConcurrentLinkedDeque.toArray()
permalink: /Java/ConcurrentLinkedDeque/toArray/
date: 2021-01-11
key: Java.C.ConcurrentLinkedDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedDeque.metodos valor="toArray" %}

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
[ConcurrentLinkedDeque](/Java/ConcurrentLinkedDeque/)

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
