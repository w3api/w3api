---
title: JavaFileManager
permalink: /Java/JavaFileManager/
date: 2021-01-11
key: Java.J.JavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JavaFileManager.description }}

## Sintaxis
~~~java
public interface JavaFileManager extends Closeable, Flushable, OptionChecker
~~~

## Métodos
* [close()](/Java/JavaFileManager/close)
* [contains()](/Java/JavaFileManager/contains)
* [flush()](/Java/JavaFileManager/flush)
* [getClassLoader()](/Java/JavaFileManager/getClassLoader)
* [getFileForInput()](/Java/JavaFileManager/getFileForInput)
* [getFileForOutput()](/Java/JavaFileManager/getFileForOutput)
* [getJavaFileForInput()](/Java/JavaFileManager/getJavaFileForInput)
* [getJavaFileForOutput()](/Java/JavaFileManager/getJavaFileForOutput)
* [getLocationForModule()](/Java/JavaFileManager/getLocationForModule)
* [getServiceLoader()](/Java/JavaFileManager/getServiceLoader)
* [handleOption()](/Java/JavaFileManager/handleOption)
* [hasLocation()](/Java/JavaFileManager/hasLocation)
* [inferBinaryName()](/Java/JavaFileManager/inferBinaryName)
* [inferModuleName()](/Java/JavaFileManager/inferModuleName)
* [isSameFile()](/Java/JavaFileManager/isSameFile)
* [list()](/Java/JavaFileManager/list)
* [listLocationsForModules()](/Java/JavaFileManager/listLocationsForModules)

## Ejemplo
~~~java
{{ site.data.Java.J.JavaFileManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
