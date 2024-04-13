---
title: Spliterators.spliteratorUnknownSize()
permalink: /Java/Spliterators/spliteratorUnknownSize/
date: 2021-01-11
key: Java.S.Spliterators
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterators.metodos valor="spliteratorUnknownSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Spliterator<T> spliteratorUnknownSize(Iterator<? extends T> iterator, int characteristics)
public static Spliterator.OfDouble spliteratorUnknownSize(PrimitiveIterator.OfDouble iterator, int characteristics)
public static Spliterator.OfInt spliteratorUnknownSize(PrimitiveIterator.OfInt iterator, int characteristics)
public static Spliterator.OfLong spliteratorUnknownSize(PrimitiveIterator.OfLong iterator, int characteristics)
~~~

## Parámetros
* **int characteristics**,  {% include w3api/param_description.html metodo=_dato parametro="int characteristics" %}
* **PrimitiveIterator.OfLong iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfLong iterator" %}
* **PrimitiveIterator.OfInt iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfInt iterator" %}
* **Iterator&lt;? extends T&gt; iterator**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<? extends T> iterator" %}
* **PrimitiveIterator.OfDouble iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfDouble iterator" %}

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
