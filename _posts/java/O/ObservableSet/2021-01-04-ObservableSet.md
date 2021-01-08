---
title: ObservableSet
permalink: Java/ObservableSet
date: 2021-01-04
key: JavaJava.O.ObservableSet
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'interface java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObservableSet.description }}

## Sintaxis
~~~java
public interface ObservableSet<E> extends Set<E>, Observable
~~~

## Métodos
* [addListener()](/Java/ObservableSet/addListener)
* [removeListener()](/Java/ObservableSet/removeListener)

## Ejemplo
~~~java
{{ site.data.Java.O.ObservableSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
