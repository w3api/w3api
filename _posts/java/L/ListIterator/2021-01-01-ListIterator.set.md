---
title: ListIterator.set()
permalink: Java/ListIterator/set
date: 2021-01-11
key: JavaJava.L.ListIterator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.ListIterator.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void set(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ListIterator](/Java/ListIterator/)

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
