---
title: ModuleElement
permalink: Java/ModuleElement
date: 2021-01-04
key: JavaJava.M.ModuleElement
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModuleElement.description }}

## Sintaxis
~~~java
public interface ModuleElement extends Element, QualifiedNameable
~~~

## Métodos
* [getDirectives()](/Java/ModuleElement/getDirectives)
* [getEnclosedElements()](/Java/ModuleElement/getEnclosedElements)
* [getEnclosingElement()](/Java/ModuleElement/getEnclosingElement)
* [getQualifiedName()](/Java/ModuleElement/getQualifiedName)
* [getSimpleName()](/Java/ModuleElement/getSimpleName)
* [isOpen()](/Java/ModuleElement/isOpen)
* [isUnnamed()](/Java/ModuleElement/isUnnamed)

## Ejemplo
~~~java
{{ site.data.Java.M.ModuleElement.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
