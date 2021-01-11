---
title: Collection.toArray()
permalink: Java/Collection/toArray
date: 2021-01-11
key: JavaJava.C.Collection
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collection.metodos valor="toArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object[] toArray()
<T> T[] toArray(T[] a)
~~~

## Parámetros
* **T[] a**,  {% include w3api/param_description.html metodo=_dato parametro="T[] a" %}

## Clase Padre
[Collection](/Java/Collection/)

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
