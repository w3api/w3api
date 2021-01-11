---
title: Spliterators.iterator()
permalink: Java/Spliterators/iterator
date: 2021-01-11
key: JavaJava.S.Spliterators
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterators.metodos valor="iterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static PrimitiveIterator.OfDouble iterator(Spliterator.OfDouble spliterator)
public static PrimitiveIterator.OfInt iterator(Spliterator.OfInt spliterator)
public static PrimitiveIterator.OfLong iterator(Spliterator.OfLong spliterator)
static <T> Iterator<T> iterator(Spliterator<? extends T> spliterator)
~~~

## Parámetros
* **Spliterator.OfInt spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfInt spliterator" %}
* **Spliterator&lt;? extends T&gt; spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator<? extends T> spliterator" %}
* **Spliterator.OfLong spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfLong spliterator" %}
* **Spliterator.OfDouble spliterator**,  {% include w3api/param_description.html metodo=_dato parametro="Spliterator.OfDouble spliterator" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Spliterators](/Java/Spliterators/)

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
