---
title: MapExpression
permalink: Java/MapExpression
date: 2021-01-04
key: JavaJava.M.MapExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MapExpression.description }}

## Sintaxis
~~~java
public abstract class MapExpression<K,V> extends Object implements ObservableMapValue<K,V>
~~~

## Constructores
* [MapExpression()](/Java/MapExpression/MapExpression/)

## Métodos
* [asString()](/Java/MapExpression/asString)
* [emptyProperty()](/Java/MapExpression/emptyProperty)
* [getSize()](/Java/MapExpression/getSize)
* [isEqualTo()](/Java/MapExpression/isEqualTo)
* [isNotEqualTo()](/Java/MapExpression/isNotEqualTo)
* [isNotNull()](/Java/MapExpression/isNotNull)
* [isNull()](/Java/MapExpression/isNull)
* [mapExpression()](/Java/MapExpression/mapExpression)
* [sizeProperty()](/Java/MapExpression/sizeProperty)
* [valueAt()](/Java/MapExpression/valueAt)

## Ejemplo
~~~java
{{ site.data.Java.M.MapExpression.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MapExpression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
