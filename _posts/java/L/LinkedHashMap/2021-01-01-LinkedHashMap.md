---
title: LinkedHashMap
permalink: Java/LinkedHashMap
date: 2021-01-11
key: Java.L.LinkedHashMap
category: java
tags: ['java se', 'java.util', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkedHashMap.description }}

## Sintaxis
~~~java
public class LinkedHashMap<K,V> extends HashMap<K,V> implements Map<K,V>
~~~

## Constructores
* [LinkedHashMap()](/Java/LinkedHashMap/LinkedHashMap/)

## Métodos
* [containsValue()](/Java/LinkedHashMap/containsValue)
* [entrySet()](/Java/LinkedHashMap/entrySet)
* [get()](/Java/LinkedHashMap/get)
* [keySet()](/Java/LinkedHashMap/keySet)
* [removeEldestEntry()](/Java/LinkedHashMap/removeEldestEntry)
* [values()](/Java/LinkedHashMap/values)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkedHashMap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
