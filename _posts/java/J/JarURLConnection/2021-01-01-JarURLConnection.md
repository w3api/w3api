---
title: JarURLConnection
permalink: /Java/JarURLConnection/
date: 2021-01-11
key: Java.J.JarURLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JarURLConnection.description }}

## Sintaxis
~~~java
public abstract class JarURLConnection extends URLConnection
~~~

## Constructores
* [JarURLConnection()](/Java/JarURLConnection/JarURLConnection/)

## Campos
* [jarFileURLConnection](/Java/JarURLConnection/jarFileURLConnection)

## Métodos
* [getAttributes()](/Java/JarURLConnection/getAttributes)
* [getCertificates()](/Java/JarURLConnection/getCertificates)
* [getEntryName()](/Java/JarURLConnection/getEntryName)
* [getJarEntry()](/Java/JarURLConnection/getJarEntry)
* [getJarFile()](/Java/JarURLConnection/getJarFile)
* [getJarFileURL()](/Java/JarURLConnection/getJarFileURL)
* [getMainAttributes()](/Java/JarURLConnection/getMainAttributes)
* [getManifest()](/Java/JarURLConnection/getManifest)

## Ejemplo
~~~java
{{ site.data.Java.J.JarURLConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
