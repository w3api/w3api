---
title: StackWalker.StackFrame
permalink: Java/StackWalker/StackFrame
date: 2021-01-04
key: JavaJava.S.StackWalker.StackFrame
category: java
tags: ['java se', 'java.lang', 'java.base', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StackWalker.StackFrame.description }}

## Sintaxis
~~~java
public static interface StackWalker.StackFrame
~~~

## Métodos
* [getByteCodeIndex()](/Java/StackWalker/StackFrame/getByteCodeIndex)
* [getClassName()](/Java/StackWalker/StackFrame/getClassName)
* [getDeclaringClass()](/Java/StackWalker/StackFrame/getDeclaringClass)
* [getDescriptor()](/Java/StackWalker/StackFrame/getDescriptor)
* [getFileName()](/Java/StackWalker/StackFrame/getFileName)
* [getLineNumber()](/Java/StackWalker/StackFrame/getLineNumber)
* [getMethodName()](/Java/StackWalker/StackFrame/getMethodName)
* [getMethodType()](/Java/StackWalker/StackFrame/getMethodType)
* [isNativeMethod()](/Java/StackWalker/StackFrame/isNativeMethod)
* [toStackTraceElement()](/Java/StackWalker/StackFrame/toStackTraceElement)

## Ejemplo
~~~java
{{ site.data.Java.S.StackWalker.StackFrame.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackWalker.StackFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
