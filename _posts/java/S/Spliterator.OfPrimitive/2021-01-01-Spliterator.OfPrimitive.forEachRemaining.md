---
title: Spliterator.OfPrimitive.forEachRemaining()
permalink: /Java/Spliterator/OfPrimitive/forEachRemaining/
date: 2021-01-11
key: Java.S.Spliterator.OfPrimitive
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfPrimitive.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(T_CONS action)
~~~

## Parámetros
* **T_CONS action**,  {% include w3api/param_description.html metodo=_dato parametro="T_CONS action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Spliterator.OfPrimitive](/Java/Spliterator/OfPrimitive/)

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
