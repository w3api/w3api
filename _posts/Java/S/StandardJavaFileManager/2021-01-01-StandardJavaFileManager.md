---
title: StandardJavaFileManager
permalink: /Java/StandardJavaFileManager/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardJavaFileManager.description }}

## Sintaxis
~~~java
public interface StandardJavaFileManager extends JavaFileManager
~~~

## Métodos
* [asPath()](/Java/StandardJavaFileManager/asPath)
* [getJavaFileObjects()](/Java/StandardJavaFileManager/getJavaFileObjects)
* [getJavaFileObjectsFromFiles()](/Java/StandardJavaFileManager/getJavaFileObjectsFromFiles)
* [getJavaFileObjectsFromPaths()](/Java/StandardJavaFileManager/getJavaFileObjectsFromPaths)
* [getJavaFileObjectsFromStrings()](/Java/StandardJavaFileManager/getJavaFileObjectsFromStrings)
* [getLocation()](/Java/StandardJavaFileManager/getLocation)
* [getLocationAsPaths()](/Java/StandardJavaFileManager/getLocationAsPaths)
* [isSameFile()](/Java/StandardJavaFileManager/isSameFile)
* [setLocation()](/Java/StandardJavaFileManager/setLocation)
* [setLocationForModule()](/Java/StandardJavaFileManager/setLocationForModule)
* [setLocationFromPaths()](/Java/StandardJavaFileManager/setLocationFromPaths)
* [setPathFactory()](/Java/StandardJavaFileManager/setPathFactory)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardJavaFileManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
