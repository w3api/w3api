---
title: PackageTree
permalink: Java/PackageTree
date: 2021-01-11
key: JavaJava.P.PackageTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PackageTree.description }}

## Sintaxis
~~~java
public interface PackageTree extends Tree
~~~

## Métodos
* [getAnnotations()](/Java/PackageTree/getAnnotations)
* [getPackageName()](/Java/PackageTree/getPackageName)

## Ejemplo
~~~java
{{ site.data.Java.P.PackageTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PackageTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
