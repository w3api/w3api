---
title: PackageDoc
permalink: Java/PackageDoc
date: 2021-01-11
key: JavaJava.P.PackageDoc
category: java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PackageDoc.description }}

## Sintaxis
~~~java
@Deprecated public interface PackageDoc extends Doc
~~~

## Métodos
* [allClasses()](/Java/PackageDoc/allClasses)
* [annotations()](/Java/PackageDoc/annotations)
* [annotationTypes()](/Java/PackageDoc/annotationTypes)
* [enums()](/Java/PackageDoc/enums)
* [errors()](/Java/PackageDoc/errors)
* [exceptions()](/Java/PackageDoc/exceptions)
* [findClass()](/Java/PackageDoc/findClass)
* [interfaces()](/Java/PackageDoc/interfaces)
* [ordinaryClasses()](/Java/PackageDoc/ordinaryClasses)

## Ejemplo
~~~java
{{ site.data.Java.P.PackageDoc.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PackageDoc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
