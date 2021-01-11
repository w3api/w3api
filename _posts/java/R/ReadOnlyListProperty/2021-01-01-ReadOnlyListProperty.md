---
title: ReadOnlyListProperty
permalink: Java/ReadOnlyListProperty
date: 2021-01-11
key: JavaJava.R.ReadOnlyListProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReadOnlyListProperty.description }}

## Sintaxis
~~~java
public abstract class ReadOnlyListProperty<E> extends ListExpression<E> implements ReadOnlyProperty<ObservableList<E>>
~~~

## Constructores
* [ReadOnlyListProperty()](/Java/ReadOnlyListProperty/ReadOnlyListProperty/)

## Métodos
* [bindContent()](/Java/ReadOnlyListProperty/bindContent)
* [bindContentBidirectional()](/Java/ReadOnlyListProperty/bindContentBidirectional)
* [toString()](/Java/ReadOnlyListProperty/toString)
* [unbindContent()](/Java/ReadOnlyListProperty/unbindContent)
* [unbindContentBidirectional()](/Java/ReadOnlyListProperty/unbindContentBidirectional)

## Ejemplo
~~~java
{{ site.data.Java.R.ReadOnlyListProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReadOnlyListProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
