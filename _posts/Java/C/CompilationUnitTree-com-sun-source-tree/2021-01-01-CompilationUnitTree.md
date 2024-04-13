---
title: CompilationUnitTree
permalink: /Java/CompilationUnitTree-com-sun-source-tree/
date: 2021-01-11
key: Java.C.CompilationUnitTree-com-sun-source-tree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompilationUnitTree-com-sun-source-tree.description }}

## Sintaxis
~~~java
public interface CompilationUnitTree extends Tree
~~~

## Métodos
* [getImports()](/Java/CompilationUnitTree-com-sun-source-tree/getImports)
* [getLineMap()](/Java/CompilationUnitTree-com-sun-source-tree/getLineMap)
* [getPackage()](/Java/CompilationUnitTree-com-sun-source-tree/getPackage)
* [getPackageAnnotations()](/Java/CompilationUnitTree-com-sun-source-tree/getPackageAnnotations)
* [getPackageName()](/Java/CompilationUnitTree-com-sun-source-tree/getPackageName)
* [getSourceFile()](/Java/CompilationUnitTree-com-sun-source-tree/getSourceFile)
* [getTypeDecls()](/Java/CompilationUnitTree-com-sun-source-tree/getTypeDecls)

## Ejemplo
~~~java
{{ site.data.Java.C.CompilationUnitTree-com-sun-source-tree.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CompilationUnitTree-com-sun-source-tree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
