---
title: ReadOnlySetProperty
permalink: Java/ReadOnlySetProperty
date: 2021-01-11
key: Java.R.ReadOnlySetProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReadOnlySetProperty.description }}

## Sintaxis
~~~java
public abstract class ReadOnlySetProperty<E> extends SetExpression<E> implements ReadOnlyProperty<ObservableSet<E>>
~~~

## Constructores
* [ReadOnlySetProperty()](/Java/ReadOnlySetProperty/ReadOnlySetProperty/)

## Métodos
* [bindContent()](/Java/ReadOnlySetProperty/bindContent)
* [bindContentBidirectional()](/Java/ReadOnlySetProperty/bindContentBidirectional)
* [hashCode()](/Java/ReadOnlySetProperty/hashCode)
* [toString()](/Java/ReadOnlySetProperty/toString)
* [unbindContent()](/Java/ReadOnlySetProperty/unbindContent)
* [unbindContentBidirectional()](/Java/ReadOnlySetProperty/unbindContentBidirectional)

## Ejemplo
~~~java
{{ site.data.Java.R.ReadOnlySetProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReadOnlySetProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
