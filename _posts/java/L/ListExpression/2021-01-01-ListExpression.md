---
title: ListExpression
permalink: Java/ListExpression
date: 2021-01-11
key: JavaJava.L.ListExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.ListExpression.description }}

## Sintaxis
~~~java
public abstract class ListExpression<E> extends Object implements ObservableListValue<E>
~~~

## Constructores
* [ListExpression()](/Java/ListExpression/ListExpression/)

## Métodos
* [asString()](/Java/ListExpression/asString)
* [emptyProperty()](/Java/ListExpression/emptyProperty)
* [getSize()](/Java/ListExpression/getSize)
* [isEqualTo()](/Java/ListExpression/isEqualTo)
* [isNotEqualTo()](/Java/ListExpression/isNotEqualTo)
* [isNotNull()](/Java/ListExpression/isNotNull)
* [isNull()](/Java/ListExpression/isNull)
* [listExpression()](/Java/ListExpression/listExpression)
* [sizeProperty()](/Java/ListExpression/sizeProperty)
* [valueAt()](/Java/ListExpression/valueAt)

## Ejemplo
~~~java
{{ site.data.Java.L.ListExpression.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
