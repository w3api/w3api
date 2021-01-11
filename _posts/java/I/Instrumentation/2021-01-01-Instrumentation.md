---
title: Instrumentation
permalink: Java/Instrumentation
date: 2021-01-11
key: JavaJava.I.Instrumentation
category: java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.Instrumentation.description }}

## Sintaxis
~~~java
public interface Instrumentation
~~~

## Métodos
* [addTransformer()](/Java/Instrumentation/addTransformer)
* [appendToBootstrapClassLoaderSearch()](/Java/Instrumentation/appendToBootstrapClassLoaderSearch)
* [appendToSystemClassLoaderSearch()](/Java/Instrumentation/appendToSystemClassLoaderSearch)
* [getAllLoadedClasses()](/Java/Instrumentation/getAllLoadedClasses)
* [getInitiatedClasses()](/Java/Instrumentation/getInitiatedClasses)
* [getObjectSize()](/Java/Instrumentation/getObjectSize)
* [isModifiableClass()](/Java/Instrumentation/isModifiableClass)
* [isModifiableModule()](/Java/Instrumentation/isModifiableModule)
* [isNativeMethodPrefixSupported()](/Java/Instrumentation/isNativeMethodPrefixSupported)
* [isRedefineClassesSupported()](/Java/Instrumentation/isRedefineClassesSupported)
* [isRetransformClassesSupported()](/Java/Instrumentation/isRetransformClassesSupported)
* [redefineClasses()](/Java/Instrumentation/redefineClasses)
* [redefineModule()](/Java/Instrumentation/redefineModule)
* [removeTransformer()](/Java/Instrumentation/removeTransformer)
* [retransformClasses()](/Java/Instrumentation/retransformClasses)
* [setNativeMethodPrefix()](/Java/Instrumentation/setNativeMethodPrefix)

## Ejemplo
~~~java
{{ site.data.Java.I.Instrumentation.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Instrumentation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
