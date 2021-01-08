---
title: ForwardingJavaFileManager
permalink: Java/ForwardingJavaFileManager
date: 2021-01-04
key: JavaJava.F.ForwardingJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForwardingJavaFileManager.description }}

## Sintaxis
~~~java
public class ForwardingJavaFileManager<M extends JavaFileManager> extends Object implements JavaFileManager
~~~

## Constructores
* [ForwardingJavaFileManager()](/Java/ForwardingJavaFileManager/ForwardingJavaFileManager/)

## Campos
* [fileManager](/Java/ForwardingJavaFileManager/fileManager)

## Métodos
* [contains()](/Java/ForwardingJavaFileManager/contains)
* [getClassLoader()](/Java/ForwardingJavaFileManager/getClassLoader)
* [getFileForInput()](/Java/ForwardingJavaFileManager/getFileForInput)
* [getFileForOutput()](/Java/ForwardingJavaFileManager/getFileForOutput)
* [getJavaFileForInput()](/Java/ForwardingJavaFileManager/getJavaFileForInput)
* [getJavaFileForOutput()](/Java/ForwardingJavaFileManager/getJavaFileForOutput)
* [getLocationForModule()](/Java/ForwardingJavaFileManager/getLocationForModule)
* [getServiceLoader()](/Java/ForwardingJavaFileManager/getServiceLoader)
* [handleOption()](/Java/ForwardingJavaFileManager/handleOption)
* [inferBinaryName()](/Java/ForwardingJavaFileManager/inferBinaryName)
* [inferModuleName()](/Java/ForwardingJavaFileManager/inferModuleName)
* [isSameFile()](/Java/ForwardingJavaFileManager/isSameFile)
* [list()](/Java/ForwardingJavaFileManager/list)
* [listLocationsForModules()](/Java/ForwardingJavaFileManager/listLocationsForModules)

## Ejemplo
~~~java
{{ site.data.Java.F.ForwardingJavaFileManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForwardingJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
