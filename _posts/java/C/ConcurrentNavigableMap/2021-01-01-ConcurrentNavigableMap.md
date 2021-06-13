---
title: ConcurrentNavigableMap
permalink: /Java/ConcurrentNavigableMap/
date: 2021-01-11
key: Java.C.ConcurrentNavigableMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConcurrentNavigableMap.description }}

## Sintaxis
~~~java
public interface ConcurrentNavigableMap<K,V> extends ConcurrentMap<K,V>, NavigableMap<K,V>
~~~

## Métodos
* [descendingKeySet()](/Java/ConcurrentNavigableMap/descendingKeySet)
* [descendingMap()](/Java/ConcurrentNavigableMap/descendingMap)
* [headMap()](/Java/ConcurrentNavigableMap/headMap)
* [keySet()](/Java/ConcurrentNavigableMap/keySet)
* [navigableKeySet()](/Java/ConcurrentNavigableMap/navigableKeySet)
* [subMap()](/Java/ConcurrentNavigableMap/subMap)
* [tailMap()](/Java/ConcurrentNavigableMap/tailMap)

## Ejemplo
~~~java
{{ site.data.Java.C.ConcurrentNavigableMap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentNavigableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
