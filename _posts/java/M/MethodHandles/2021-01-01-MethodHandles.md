---
title: MethodHandles
permalink: /Java/MethodHandles/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodHandles.description }}

## Sintaxis
~~~java
public class MethodHandles extends Object
~~~

## Métodos
* [arrayConstructor()](/Java/MethodHandles/arrayConstructor)
* [arrayElementGetter()](/Java/MethodHandles/arrayElementGetter)
* [arrayElementSetter()](/Java/MethodHandles/arrayElementSetter)
* [arrayElementVarHandle()](/Java/MethodHandles/arrayElementVarHandle)
* [arrayLength()](/Java/MethodHandles/arrayLength)
* [byteArrayViewVarHandle()](/Java/MethodHandles/byteArrayViewVarHandle)
* [byteBufferViewVarHandle()](/Java/MethodHandles/byteBufferViewVarHandle)
* [catchException()](/Java/MethodHandles/catchException)
* [collectArguments()](/Java/MethodHandles/collectArguments)
* [constant()](/Java/MethodHandles/constant)
* [countedLoop()](/Java/MethodHandles/countedLoop)
* [doWhileLoop()](/Java/MethodHandles/doWhileLoop)
* [dropArguments()](/Java/MethodHandles/dropArguments)
* [dropArgumentsToMatch()](/Java/MethodHandles/dropArgumentsToMatch)
* [empty()](/Java/MethodHandles/empty)
* [exactInvoker()](/Java/MethodHandles/exactInvoker)
* [explicitCastArguments()](/Java/MethodHandles/explicitCastArguments)
* [filterArguments()](/Java/MethodHandles/filterArguments)
* [filterReturnValue()](/Java/MethodHandles/filterReturnValue)
* [foldArguments()](/Java/MethodHandles/foldArguments)
* [guardWithTest()](/Java/MethodHandles/guardWithTest)
* [identity()](/Java/MethodHandles/identity)
* [insertArguments()](/Java/MethodHandles/insertArguments)
* [invoker()](/Java/MethodHandles/invoker)
* [iteratedLoop()](/Java/MethodHandles/iteratedLoop)
* [lookup()](/Java/MethodHandles/lookup)
* [loop()](/Java/MethodHandles/loop)
* [permuteArguments()](/Java/MethodHandles/permuteArguments)
* [privateLookupIn()](/Java/MethodHandles/privateLookupIn)
* [publicLookup()](/Java/MethodHandles/publicLookup)
* [reflectAs()](/Java/MethodHandles/reflectAs)
* [spreadInvoker()](/Java/MethodHandles/spreadInvoker)
* [throwException()](/Java/MethodHandles/throwException)
* [tryFinally()](/Java/MethodHandles/tryFinally)
* [varHandleExactInvoker()](/Java/MethodHandles/varHandleExactInvoker)
* [varHandleInvoker()](/Java/MethodHandles/varHandleInvoker)
* [whileLoop()](/Java/MethodHandles/whileLoop)
* [zero()](/Java/MethodHandles/zero)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodHandles.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
