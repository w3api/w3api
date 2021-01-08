---
title: ObservableValue
permalink: Java/ObservableValue
date: 2021-01-04
key: JavaJava.O.ObservableValue
category: java
tags: ['java se', 'javafx.beans.value', 'javafx.base', 'interface java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObservableValue.description }}

## Sintaxis
~~~java
public interface ObservableValue<T> extends Observable
~~~

## Métodos
* [addListener()](/Java/ObservableValue/addListener)
* [getValue()](/Java/ObservableValue/getValue)
* [removeListener()](/Java/ObservableValue/removeListener)

## Ejemplo
~~~java
{{ site.data.Java.O.ObservableValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObservableValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
