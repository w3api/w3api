---
title: FileSystem
permalink: /Java/FileSystem/
date: 2021-01-11
key: Java.F.FileSystem
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FileSystem.description }}

## Sintaxis
~~~java
public abstract class FileSystem extends Object implements Closeable
~~~

## Constructores
* [FileSystem()](/Java/FileSystem/FileSystem/)

## Métodos
* [close()](/Java/FileSystem/close)
* [getFileStores()](/Java/FileSystem/getFileStores)
* [getPath()](/Java/FileSystem/getPath)
* [getPathMatcher()](/Java/FileSystem/getPathMatcher)
* [getRootDirectories()](/Java/FileSystem/getRootDirectories)
* [getSeparator()](/Java/FileSystem/getSeparator)
* [getUserPrincipalLookupService()](/Java/FileSystem/getUserPrincipalLookupService)
* [isOpen()](/Java/FileSystem/isOpen)
* [isReadOnly()](/Java/FileSystem/isReadOnly)
* [newWatchService()](/Java/FileSystem/newWatchService)
* [provider()](/Java/FileSystem/provider)
* [supportedFileAttributeViews()](/Java/FileSystem/supportedFileAttributeViews)

## Ejemplo
~~~java
{{ site.data.Java.F.FileSystem.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
