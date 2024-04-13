---
title: CodeSource
permalink: /Java/CodeSource/
date: 2021-01-11
key: Java.C.CodeSource
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CodeSource.description }}

## Sintaxis
~~~java
public class CodeSource extends Object implements Serializable
~~~

## Constructores
* [CodeSource()](/Java/CodeSource/CodeSource/)

## Métodos
* [equals()](/Java/CodeSource/equals)
* [getCertificates()](/Java/CodeSource/getCertificates)
* [getCodeSigners()](/Java/CodeSource/getCodeSigners)
* [getLocation()](/Java/CodeSource/getLocation)
* [hashCode()](/Java/CodeSource/hashCode)
* [implies()](/Java/CodeSource/implies)
* [toString()](/Java/CodeSource/toString)

## Ejemplo
~~~java
{{ site.data.Java.C.CodeSource.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CodeSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
