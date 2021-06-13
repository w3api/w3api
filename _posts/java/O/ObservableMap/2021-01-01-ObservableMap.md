---
title: ObservableMap
permalink: /Java/ObservableMap/
date: 2021-01-11
key: JavaJava.O.ObservableMap
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'interface java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObservableMap.description }}

## Sintaxis
~~~java
public interface ObservableMap<K,V> extends Map<K,V>, Observable
~~~

## Métodos
* [addListener()](/Java/ObservableMap/addListener)
* [removeListener()](/Java/ObservableMap/removeListener)

## Ejemplo
~~~java
{{ site.data.Java.O.ObservableMap.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
