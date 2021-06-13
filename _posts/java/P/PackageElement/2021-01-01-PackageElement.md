---
title: PackageElement
permalink: /Java/PackageElement/
date: 2021-01-11
key: Java.P.PackageElement
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PackageElement.description }}

## Sintaxis
~~~java
public interface PackageElement extends Element, QualifiedNameable
~~~

## Métodos
* [getEnclosedElements()](/Java/PackageElement/getEnclosedElements)
* [getEnclosingElement()](/Java/PackageElement/getEnclosingElement)
* [getQualifiedName()](/Java/PackageElement/getQualifiedName)
* [getSimpleName()](/Java/PackageElement/getSimpleName)
* [isUnnamed()](/Java/PackageElement/isUnnamed)

## Ejemplo
~~~java
{{ site.data.Java.P.PackageElement.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PackageElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
