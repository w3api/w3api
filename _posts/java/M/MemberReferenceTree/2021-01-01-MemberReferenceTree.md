---
title: MemberReferenceTree
permalink: Java/MemberReferenceTree
date: 2021-01-11
key: JavaJava.M.MemberReferenceTree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemberReferenceTree.description }}

## Sintaxis
~~~java
public interface MemberReferenceTree extends ExpressionTree
~~~

## Métodos
* [getMode()](/Java/MemberReferenceTree/getMode)
* [getName()](/Java/MemberReferenceTree/getName)
* [getQualifierExpression()](/Java/MemberReferenceTree/getQualifierExpression)
* [getTypeArguments()](/Java/MemberReferenceTree/getTypeArguments)

## Ejemplo
~~~java
{{ site.data.Java.M.MemberReferenceTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemberReferenceTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
