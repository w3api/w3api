---
title: StackTraceElement
permalink: /Java/StackTraceElement/
date: 2021-01-11
key: Java.S.StackTraceElement
category: Java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StackTraceElement.description }}

## Sintaxis
~~~java
public final class StackTraceElement extends Object implements Serializable
~~~

## Constructores
* [StackTraceElement()](/Java/StackTraceElement/StackTraceElement/)

## Métodos
* [equals()](/Java/StackTraceElement/equals)
* [getClassLoaderName()](/Java/StackTraceElement/getClassLoaderName)
* [getClassName()](/Java/StackTraceElement/getClassName)
* [getFileName()](/Java/StackTraceElement/getFileName)
* [getLineNumber()](/Java/StackTraceElement/getLineNumber)
* [getMethodName()](/Java/StackTraceElement/getMethodName)
* [getModuleName()](/Java/StackTraceElement/getModuleName)
* [getModuleVersion()](/Java/StackTraceElement/getModuleVersion)
* [hashCode()](/Java/StackTraceElement/hashCode)
* [isNativeMethod()](/Java/StackTraceElement/isNativeMethod)
* [toString()](/Java/StackTraceElement/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.StackTraceElement.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackTraceElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
