---
title: LinkedList.toArray()
permalink: Java/LinkedList/toArray
date: 2021-01-11
key: JavaJava.L.LinkedList
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedList.metodos valor="toArray" %}

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
[LinkedList](/Java/LinkedList/)

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