---
title: ObservableList
permalink: /Java/ObservableList/
date: 2021-01-11
key: JavaJava.O.ObservableList
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'interface java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObservableList.description }}

## Sintaxis
~~~java
public interface ObservableList<E> extends List<E>, Observable
~~~

## Métodos
* [addAll()](/Java/ObservableList/addAll)
* [addListener()](/Java/ObservableList/addListener)
* [filtered()](/Java/ObservableList/filtered)
* [remove()](/Java/ObservableList/remove)
* [removeAll()](/Java/ObservableList/removeAll)
* [removeListener()](/Java/ObservableList/removeListener)
* [retainAll()](/Java/ObservableList/retainAll)
* [setAll()](/Java/ObservableList/setAll)
* [sorted()](/Java/ObservableList/sorted)

## Ejemplo
~~~java
{{ site.data.Java.O.ObservableList.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
