---
title: TypeVariable
permalink: Java/TypeVariable-java-lang-reflect
date: 2021-01-04
key: JavaJava.T.TypeVariable-java-lang-reflect
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeVariable-java-lang-reflect.description }}

## Sintaxis
~~~java
public interface TypeVariable<D extends GenericDeclaration> extends Type, AnnotatedElement
~~~

## Métodos
* [getAnnotatedBounds()](/Java/TypeVariable-java-lang-reflect/getAnnotatedBounds)
* [getBounds()](/Java/TypeVariable-java-lang-reflect/getBounds)
* [getGenericDeclaration()](/Java/TypeVariable-java-lang-reflect/getGenericDeclaration)
* [getName()](/Java/TypeVariable-java-lang-reflect/getName)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeVariable-java-lang-reflect.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeVariable-java-lang-reflect.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
