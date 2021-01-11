---
title: URLClassLoader
permalink: Java/URLClassLoader
date: 2021-01-11
key: JavaJava.U.URLClassLoader
category: java
tags: ['java se', 'java.net', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.URLClassLoader.description }}

## Sintaxis
~~~java
public class URLClassLoader extends SecureClassLoader implements Closeable
~~~

## Constructores
* [URLClassLoader()](/Java/URLClassLoader/URLClassLoader/)

## Métodos
* [addURL()](/Java/URLClassLoader/addURL)
* [close()](/Java/URLClassLoader/close)
* [definePackage()](/Java/URLClassLoader/definePackage)
* [findClass()](/Java/URLClassLoader/findClass)
* [findResource()](/Java/URLClassLoader/findResource)
* [findResources()](/Java/URLClassLoader/findResources)
* [getPermissions()](/Java/URLClassLoader/getPermissions)
* [getResourceAsStream()](/Java/URLClassLoader/getResourceAsStream)
* [getURLs()](/Java/URLClassLoader/getURLs)
* [newInstance()](/Java/URLClassLoader/newInstance)

## Ejemplo
~~~java
{{ site.data.Java.U.URLClassLoader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.URLClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
