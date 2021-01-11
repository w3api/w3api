---
title: ConcurrentMap
permalink: Java/ConcurrentMap
date: 2021-01-11
key: JavaJava.C.ConcurrentMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConcurrentMap.description }}

## Sintaxis
~~~java
public interface ConcurrentMap<K,V> extends Map<K,V>
~~~

## Métodos
* [compute()](/Java/ConcurrentMap/compute)
* [computeIfAbsent()](/Java/ConcurrentMap/computeIfAbsent)
* [computeIfPresent()](/Java/ConcurrentMap/computeIfPresent)
* [forEach()](/Java/ConcurrentMap/forEach)
* [getOrDefault()](/Java/ConcurrentMap/getOrDefault)
* [merge()](/Java/ConcurrentMap/merge)
* [putIfAbsent()](/Java/ConcurrentMap/putIfAbsent)
* [remove()](/Java/ConcurrentMap/remove)
* [replace()](/Java/ConcurrentMap/replace)
* [replaceAll()](/Java/ConcurrentMap/replaceAll)

## Ejemplo
~~~java
{{ site.data.Java.C.ConcurrentMap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
