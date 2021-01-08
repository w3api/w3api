---
title: ArrayDeque.remove()
permalink: Java/ArrayDeque/remove
date: 2021-01-04
key: JavaJava.A.ArrayDeque
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayDeque.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E remove()
public boolean remove(Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_data parametro="Object o" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/)

## Clase Padre
[ArrayDeque](/Java/ArrayDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ArrayDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
