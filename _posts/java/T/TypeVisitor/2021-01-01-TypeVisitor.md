---
title: TypeVisitor
permalink: Java/TypeVisitor
date: 2021-01-11
key: JavaJava.T.TypeVisitor
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeVisitor.description }}

## Sintaxis
~~~java
public interface TypeVisitor<R,P>
~~~

## Métodos
* [visit()](/Java/TypeVisitor/visit)
* [visitArray()](/Java/TypeVisitor/visitArray)
* [visitDeclared()](/Java/TypeVisitor/visitDeclared)
* [visitError()](/Java/TypeVisitor/visitError)
* [visitExecutable()](/Java/TypeVisitor/visitExecutable)
* [visitIntersection()](/Java/TypeVisitor/visitIntersection)
* [visitNoType()](/Java/TypeVisitor/visitNoType)
* [visitNull()](/Java/TypeVisitor/visitNull)
* [visitPrimitive()](/Java/TypeVisitor/visitPrimitive)
* [visitTypeVariable()](/Java/TypeVisitor/visitTypeVariable)
* [visitUnion()](/Java/TypeVisitor/visitUnion)
* [visitUnknown()](/Java/TypeVisitor/visitUnknown)
* [visitWildcard()](/Java/TypeVisitor/visitWildcard)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
