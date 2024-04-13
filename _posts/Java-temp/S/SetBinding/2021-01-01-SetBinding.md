---
title: SetBinding
permalink: /Java/SetBinding/
date: 2021-01-11
key: Java.S.SetBinding
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SetBinding.description }}

## Sintaxis
~~~java
public abstract class SetBinding<E> extends SetExpression<E> implements Binding<ObservableSet<E>>
~~~

## Constructores
* [SetBinding()](/Java/SetBinding/SetBinding/)

## Métodos
* [bind()](/Java/SetBinding/bind)
* [computeValue()](/Java/SetBinding/computeValue)
* [dispose()](/Java/SetBinding/dispose)
* [get()](/Java/SetBinding/get)
* [getDependencies()](/Java/SetBinding/getDependencies)
* [onInvalidating()](/Java/SetBinding/onInvalidating)
* [toString()](/Java/SetBinding/toString)
* [unbind()](/Java/SetBinding/unbind)

## Ejemplo
~~~java
{{ site.data.Java.S.SetBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SetBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
