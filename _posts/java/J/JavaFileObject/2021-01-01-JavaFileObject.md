---
title: JavaFileObject
permalink: Java/JavaFileObject
date: 2021-01-11
key: JavaJava.J.JavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JavaFileObject.description }}

## Sintaxis
~~~java
public interface JavaFileObject extends FileObject
~~~

## Métodos
* [getAccessLevel()](/Java/JavaFileObject/getAccessLevel)
* [getKind()](/Java/JavaFileObject/getKind)
* [getNestingKind()](/Java/JavaFileObject/getNestingKind)
* [isNameCompatible()](/Java/JavaFileObject/isNameCompatible)

## Ejemplo
~~~java
{{ site.data.Java.J.JavaFileObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
