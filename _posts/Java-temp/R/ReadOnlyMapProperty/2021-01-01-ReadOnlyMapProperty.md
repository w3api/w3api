---
title: ReadOnlyMapProperty
permalink: /Java/ReadOnlyMapProperty/
date: 2021-01-11
key: Java.R.ReadOnlyMapProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReadOnlyMapProperty.description }}

## Sintaxis
~~~java
public abstract class ReadOnlyMapProperty<K,V> extends MapExpression<K,V> implements ReadOnlyProperty<ObservableMap<K,V>>
~~~

## Constructores
* [ReadOnlyMapProperty()](/Java/ReadOnlyMapProperty/ReadOnlyMapProperty/)

## Métodos
* [bindContent()](/Java/ReadOnlyMapProperty/bindContent)
* [bindContentBidirectional()](/Java/ReadOnlyMapProperty/bindContentBidirectional)
* [hashCode()](/Java/ReadOnlyMapProperty/hashCode)
* [toString()](/Java/ReadOnlyMapProperty/toString)
* [unbindContent()](/Java/ReadOnlyMapProperty/unbindContent)
* [unbindContentBidirectional()](/Java/ReadOnlyMapProperty/unbindContentBidirectional)

## Ejemplo
~~~java
{{ site.data.Java.R.ReadOnlyMapProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReadOnlyMapProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
