---
title: BooleanBinding
permalink: Java/BooleanBinding
date: 2021-01-11
key: JavaJava.B.BooleanBinding
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BooleanBinding.description }}

## Sintaxis
~~~java
public abstract class BooleanBinding extends BooleanExpression implements Binding<Boolean>
~~~

## Constructores
* [BooleanBinding()](/Java/BooleanBinding/BooleanBinding/)

## Métodos
* [bind()](/Java/BooleanBinding/bind)
* [computeValue()](/Java/BooleanBinding/computeValue)
* [dispose()](/Java/BooleanBinding/dispose)
* [get()](/Java/BooleanBinding/get)
* [getDependencies()](/Java/BooleanBinding/getDependencies)
* [onInvalidating()](/Java/BooleanBinding/onInvalidating)
* [toString()](/Java/BooleanBinding/toString)
* [unbind()](/Java/BooleanBinding/unbind)

## Ejemplo
~~~java
{{ site.data.Java.B.BooleanBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BooleanBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
