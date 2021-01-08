---
title: TypeElement
permalink: Java/TypeElement
date: 2021-01-04
key: JavaJava.T.TypeElement
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeElement.description }}

## Sintaxis
~~~java
public interface TypeElement extends Element, Parameterizable, QualifiedNameable
~~~

## Métodos
* [getEnclosedElements()](/Java/TypeElement/getEnclosedElements)
* [getEnclosingElement()](/Java/TypeElement/getEnclosingElement)
* [getInterfaces()](/Java/TypeElement/getInterfaces)
* [getNestingKind()](/Java/TypeElement/getNestingKind)
* [getQualifiedName()](/Java/TypeElement/getQualifiedName)
* [getSimpleName()](/Java/TypeElement/getSimpleName)
* [getSuperclass()](/Java/TypeElement/getSuperclass)
* [getTypeParameters()](/Java/TypeElement/getTypeParameters)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeElement.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
