---
title: ObjectBinding
permalink: /Java/ObjectBinding/
date: 2021-01-11
key: Java.O.ObjectBinding
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectBinding.description }}

## Sintaxis
~~~java
public abstract class ObjectBinding<T> extends ObjectExpression<T> implements Binding<T>
~~~

## Constructores
* [ObjectBinding()](/Java/ObjectBinding/ObjectBinding/)

## Métodos
* [bind()](/Java/ObjectBinding/bind)
* [computeValue()](/Java/ObjectBinding/computeValue)
* [dispose()](/Java/ObjectBinding/dispose)
* [get()](/Java/ObjectBinding/get)
* [getDependencies()](/Java/ObjectBinding/getDependencies)
* [onInvalidating()](/Java/ObjectBinding/onInvalidating)
* [toString()](/Java/ObjectBinding/toString)
* [unbind()](/Java/ObjectBinding/unbind)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
