---
title: FileStore
permalink: /Java/FileStore/
date: 2021-01-11
key: Java.F.FileStore
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FileStore.description }}

## Sintaxis
~~~java
public abstract class FileStore extends Object
~~~

## Constructores
* [FileStore()](/Java/FileStore/FileStore/)

## Métodos
* [getAttribute()](/Java/FileStore/getAttribute)
* [getBlockSize()](/Java/FileStore/getBlockSize)
* [getFileStoreAttributeView()](/Java/FileStore/getFileStoreAttributeView)
* [getTotalSpace()](/Java/FileStore/getTotalSpace)
* [getUnallocatedSpace()](/Java/FileStore/getUnallocatedSpace)
* [getUsableSpace()](/Java/FileStore/getUsableSpace)
* [isReadOnly()](/Java/FileStore/isReadOnly)
* [name()](/Java/FileStore/name)
* [supportsFileAttributeView()](/Java/FileStore/supportsFileAttributeView)
* [type()](/Java/FileStore/type)

## Ejemplo
~~~java
{{ site.data.Java.F.FileStore.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileStore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
