---
title: AnnotationTree
permalink: Java/AnnotationTree
date: 2021-01-11
key: JavaJava.A.AnnotationTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AnnotationTree.description }}

## Sintaxis
~~~java
public interface AnnotationTree extends ExpressionTree
~~~

## Métodos
* [getAnnotationType()](/Java/AnnotationTree/getAnnotationType)
* [getArguments()](/Java/AnnotationTree/getArguments)

## Ejemplo
~~~java
{{ site.data.Java.A.AnnotationTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AnnotationTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
