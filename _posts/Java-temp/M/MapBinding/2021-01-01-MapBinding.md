---
title: MapBinding
permalink: /Java/MapBinding/
date: 2021-01-11
key: Java.M.MapBinding
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MapBinding.description }}

## Sintaxis
~~~java
public abstract class MapBinding<K,V> extends MapExpression<K,V> implements Binding<ObservableMap<K,V>>
~~~

## Constructores
* [MapBinding()](/Java/MapBinding/MapBinding/)

## Métodos
* [bind()](/Java/MapBinding/bind)
* [computeValue()](/Java/MapBinding/computeValue)
* [dispose()](/Java/MapBinding/dispose)
* [get()](/Java/MapBinding/get)
* [getDependencies()](/Java/MapBinding/getDependencies)
* [onInvalidating()](/Java/MapBinding/onInvalidating)
* [toString()](/Java/MapBinding/toString)
* [unbind()](/Java/MapBinding/unbind)

## Ejemplo
~~~java
{{ site.data.Java.M.MapBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MapBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
