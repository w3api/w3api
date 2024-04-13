---
title: ClassLoader
permalink: /Java/ClassLoader/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassLoader.description }}

## Sintaxis
~~~java
public abstract class ClassLoader extends Object
~~~

## Constructores
* [ClassLoader()](/Java/ClassLoader/ClassLoader/)

## Métodos
* [clearAssertionStatus()](/Java/ClassLoader/clearAssertionStatus)
* [defineClass()](/Java/ClassLoader/defineClass)
* [definePackage()](/Java/ClassLoader/definePackage)
* [findClass()](/Java/ClassLoader/findClass)
* [findLibrary()](/Java/ClassLoader/findLibrary)
* [findLoadedClass()](/Java/ClassLoader/findLoadedClass)
* [findResource()](/Java/ClassLoader/findResource)
* [findResources()](/Java/ClassLoader/findResources)
* [findSystemClass()](/Java/ClassLoader/findSystemClass)
* [getClassLoadingLock()](/Java/ClassLoader/getClassLoadingLock)
* [getDefinedPackage()](/Java/ClassLoader/getDefinedPackage)
* [getDefinedPackages()](/Java/ClassLoader/getDefinedPackages)
* [getName()](/Java/ClassLoader/getName)
* [getPackage()](/Java/ClassLoader/getPackage)
* [getPackages()](/Java/ClassLoader/getPackages)
* [getParent()](/Java/ClassLoader/getParent)
* [getPlatformClassLoader()](/Java/ClassLoader/getPlatformClassLoader)
* [getResource()](/Java/ClassLoader/getResource)
* [getResourceAsStream()](/Java/ClassLoader/getResourceAsStream)
* [getResources()](/Java/ClassLoader/getResources)
* [getSystemClassLoader()](/Java/ClassLoader/getSystemClassLoader)
* [getSystemResource()](/Java/ClassLoader/getSystemResource)
* [getSystemResourceAsStream()](/Java/ClassLoader/getSystemResourceAsStream)
* [getSystemResources()](/Java/ClassLoader/getSystemResources)
* [getUnnamedModule()](/Java/ClassLoader/getUnnamedModule)
* [isRegisteredAsParallelCapable()](/Java/ClassLoader/isRegisteredAsParallelCapable)
* [loadClass()](/Java/ClassLoader/loadClass)
* [registerAsParallelCapable()](/Java/ClassLoader/registerAsParallelCapable)
* [resolveClass()](/Java/ClassLoader/resolveClass)
* [resources()](/Java/ClassLoader/resources)
* [setClassAssertionStatus()](/Java/ClassLoader/setClassAssertionStatus)
* [setDefaultAssertionStatus()](/Java/ClassLoader/setDefaultAssertionStatus)
* [setPackageAssertionStatus()](/Java/ClassLoader/setPackageAssertionStatus)
* [setSigners()](/Java/ClassLoader/setSigners)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassLoader.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
