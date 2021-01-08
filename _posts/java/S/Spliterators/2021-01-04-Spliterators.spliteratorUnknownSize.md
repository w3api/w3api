---
title: Spliterators.spliteratorUnknownSize()
permalink: Java/Spliterators/spliteratorUnknownSize
date: 2021-01-04
key: JavaJava.S.Spliterators
category: java
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
* **Iterator&lt;? extends T&gt; iterator**,  {% include w3api/param_description.html metodo=_data parametro="Iterator<? extends T> iterator" %}
* **PrimitiveIterator.OfLong iterator**,  {% include w3api/param_description.html metodo=_data parametro="PrimitiveIterator.OfLong iterator" %}
* **PrimitiveIterator.OfInt iterator**,  {% include w3api/param_description.html metodo=_data parametro="PrimitiveIterator.OfInt iterator" %}
* **int characteristics**,  {% include w3api/param_description.html metodo=_data parametro="int characteristics" %}
* **PrimitiveIterator.OfDouble iterator**,  {% include w3api/param_description.html metodo=_data parametro="PrimitiveIterator.OfDouble iterator" %}

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
{%- for _ldc in site.data.Java.S.Spliterators.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
