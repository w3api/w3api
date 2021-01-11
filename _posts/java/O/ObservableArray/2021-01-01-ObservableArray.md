---
title: ObservableArray
permalink: Java/ObservableArray
date: 2021-01-11
key: JavaJava.O.ObservableArray
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'interface java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObservableArray.description }}

## Sintaxis
~~~java
public interface ObservableArray<T extends ObservableArray<T>> extends Observable
~~~

## Métodos
* [addListener()](/Java/ObservableArray/addListener)
* [clear()](/Java/ObservableArray/clear)
* [ensureCapacity()](/Java/ObservableArray/ensureCapacity)
* [removeListener()](/Java/ObservableArray/removeListener)
* [resize()](/Java/ObservableArray/resize)
* [size()](/Java/ObservableArray/size)
* [trimToSize()](/Java/ObservableArray/trimToSize)

## Ejemplo
~~~java
{{ site.data.Java.O.ObservableArray.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
