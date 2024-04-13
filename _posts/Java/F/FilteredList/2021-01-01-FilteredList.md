---
title: FilteredList
permalink: /Java/FilteredList/
date: 2021-01-11
key: Java.F.FilteredList
category: Java
tags: ['java se', 'javafx.collections.transformation', 'javafx.base', 'clase java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FilteredList.description }}

## Sintaxis
~~~java
public final class FilteredList<E> extends TransformationList<E,E>
~~~

## Constructores
* [FilteredList()](/Java/FilteredList/FilteredList/)

## Métodos
* [get()](/Java/FilteredList/get)
* [getPredicate()](/Java/FilteredList/getPredicate)
* [predicateProperty()](/Java/FilteredList/predicateProperty)
* [setPredicate()](/Java/FilteredList/setPredicate)
* [size()](/Java/FilteredList/size)

## Ejemplo
~~~java
{{ site.data.Java.F.FilteredList.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FilteredList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
