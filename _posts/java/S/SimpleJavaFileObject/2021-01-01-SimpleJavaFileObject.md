---
title: SimpleJavaFileObject
permalink: Java/SimpleJavaFileObject
date: 2021-01-11
key: JavaJava.S.SimpleJavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SimpleJavaFileObject.description }}

## Sintaxis
~~~java
public class SimpleJavaFileObject extends Object implements JavaFileObject
~~~

## Constructores
* [SimpleJavaFileObject()](/Java/SimpleJavaFileObject/SimpleJavaFileObject/)

## Campos
* [kind](/Java/SimpleJavaFileObject/kind)
* [uri](/Java/SimpleJavaFileObject/uri)

## Métodos
* [delete()](/Java/SimpleJavaFileObject/delete)
* [getAccessLevel()](/Java/SimpleJavaFileObject/getAccessLevel)
* [getCharContent()](/Java/SimpleJavaFileObject/getCharContent)
* [getKind()](/Java/SimpleJavaFileObject/getKind)
* [getLastModified()](/Java/SimpleJavaFileObject/getLastModified)
* [getNestingKind()](/Java/SimpleJavaFileObject/getNestingKind)
* [isNameCompatible()](/Java/SimpleJavaFileObject/isNameCompatible)
* [openInputStream()](/Java/SimpleJavaFileObject/openInputStream)
* [openOutputStream()](/Java/SimpleJavaFileObject/openOutputStream)
* [openReader()](/Java/SimpleJavaFileObject/openReader)
* [openWriter()](/Java/SimpleJavaFileObject/openWriter)

## Ejemplo
~~~java
{{ site.data.Java.S.SimpleJavaFileObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleJavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
