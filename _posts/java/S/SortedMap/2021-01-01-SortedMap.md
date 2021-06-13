---
title: SortedMap
permalink: /Java/SortedMap/
date: 2021-01-11
key: Java.S.SortedMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SortedMap.description }}

## Sintaxis
~~~java
public interface SortedMap<K,V> extends Map<K,V>
~~~

## Métodos
* [comparator()](/Java/SortedMap/comparator)
* [entrySet()](/Java/SortedMap/entrySet)
* [firstKey()](/Java/SortedMap/firstKey)
* [headMap()](/Java/SortedMap/headMap)
* [keySet()](/Java/SortedMap/keySet)
* [lastKey()](/Java/SortedMap/lastKey)
* [subMap()](/Java/SortedMap/subMap)
* [tailMap()](/Java/SortedMap/tailMap)
* [values()](/Java/SortedMap/values)

## Ejemplo
~~~java
{{ site.data.Java.S.SortedMap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SortedMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
