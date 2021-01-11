---
title: Spliterators.spliterator()
permalink: Java/Spliterators/spliterator
date: 2021-01-11
key: JavaJava.S.Spliterators
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterators.metodos valor="spliterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Spliterator.OfDouble spliterator(double[] array, int additionalCharacteristics)
public static Spliterator.OfDouble spliterator(double[] array, int fromIndex, int toIndex, int additionalCharacteristics)
public static Spliterator.OfInt spliterator(int[] array, int additionalCharacteristics)
public static Spliterator.OfInt spliterator(int[] array, int fromIndex, int toIndex, int additionalCharacteristics)
public static Spliterator.OfLong spliterator(long[] array, int additionalCharacteristics)
public static Spliterator.OfLong spliterator(long[] array, int fromIndex, int toIndex, int additionalCharacteristics)
static <T> Spliterator<T> spliterator(Object[] array, int additionalCharacteristics)
static <T> Spliterator<T> spliterator(Object[] array, int fromIndex, int toIndex, int additionalCharacteristics)
static <T> Spliterator<T> spliterator(Collection<? extends T> c, int characteristics)
static <T> Spliterator<T> spliterator(Iterator<? extends T> iterator, long size, int characteristics)
public static Spliterator.OfDouble spliterator(PrimitiveIterator.OfDouble iterator, long size, int characteristics)
public static Spliterator.OfInt spliterator(PrimitiveIterator.OfInt iterator, long size, int characteristics)
public static Spliterator.OfLong spliterator(PrimitiveIterator.OfLong iterator, long size, int characteristics)
~~~

## Parámetros
* **int characteristics**,  {% include w3api/param_description.html metodo=_dato parametro="int characteristics" %}
* **int[] array**,  {% include w3api/param_description.html metodo=_dato parametro="int[] array" %}
* **PrimitiveIterator.OfLong iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfLong iterator" %}
* **int additionalCharacteristics**,  {% include w3api/param_description.html metodo=_dato parametro="int additionalCharacteristics" %}
* **Iterator&lt;? extends T&gt; iterator**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<? extends T> iterator" %}
* **PrimitiveIterator.OfInt iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfInt iterator" %}
* **double[] array**,  {% include w3api/param_description.html metodo=_dato parametro="double[] array" %}
* **int toIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int toIndex" %}
* **Collection&lt;? extends T&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends T> c" %}
* **long size**,  {% include w3api/param_description.html metodo=_dato parametro="long size" %}
* **int fromIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int fromIndex" %}
* **long[] array**,  {% include w3api/param_description.html metodo=_dato parametro="long[] array" %}
* **Object[] array**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] array" %}
* **PrimitiveIterator.OfDouble iterator**,  {% include w3api/param_description.html metodo=_dato parametro="PrimitiveIterator.OfDouble iterator" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

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
