---
title: SecureDirectoryStream
permalink: /Java/SecureDirectoryStream/
date: 2021-01-11
key: Java.S.SecureDirectoryStream
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SecureDirectoryStream.description }}

## Sintaxis
~~~java
public interface SecureDirectoryStream<T> extends DirectoryStream<T>
~~~

## Métodos
* [deleteDirectory()](/Java/SecureDirectoryStream/deleteDirectory)
* [deleteFile()](/Java/SecureDirectoryStream/deleteFile)
* [getFileAttributeView()](/Java/SecureDirectoryStream/getFileAttributeView)
* [move()](/Java/SecureDirectoryStream/move)
* [newByteChannel()](/Java/SecureDirectoryStream/newByteChannel)
* [newDirectoryStream()](/Java/SecureDirectoryStream/newDirectoryStream)

## Ejemplo
~~~java
{{ site.data.Java.S.SecureDirectoryStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureDirectoryStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
