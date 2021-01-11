---
title: StringBinding
permalink: Java/StringBinding
date: 2021-01-11
key: JavaJava.S.StringBinding
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StringBinding.description }}

## Sintaxis
~~~java
public abstract class StringBinding extends StringExpression implements Binding<String>
~~~

## Constructores
* [StringBinding()](/Java/StringBinding/StringBinding/)

## Métodos
* [bind()](/Java/StringBinding/bind)
* [computeValue()](/Java/StringBinding/computeValue)
* [dispose()](/Java/StringBinding/dispose)
* [get()](/Java/StringBinding/get)
* [getDependencies()](/Java/StringBinding/getDependencies)
* [onInvalidating()](/Java/StringBinding/onInvalidating)
* [toString()](/Java/StringBinding/toString)
* [unbind()](/Java/StringBinding/unbind)

## Ejemplo
~~~java
{{ site.data.Java.S.StringBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
