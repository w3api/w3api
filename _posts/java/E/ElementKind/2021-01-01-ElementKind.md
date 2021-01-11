---
title: ElementKind
permalink: Java/ElementKind
date: 2021-01-11
key: JavaJava.E.ElementKind
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ElementKind.description }}

## Sintaxis
~~~java
public enum ElementKind extends Enum<ElementKind>
~~~

## Enumerados
* [ANNOTATION_TYPE](/Java/ElementKind/ANNOTATION_TYPE)
* [CLASS](/Java/ElementKind/CLASS)
* [CONSTRUCTOR](/Java/ElementKind/CONSTRUCTOR)
* [ENUM](/Java/ElementKind/ENUM)
* [ENUM_CONSTANT](/Java/ElementKind/ENUM_CONSTANT)
* [EXCEPTION_PARAMETER](/Java/ElementKind/EXCEPTION_PARAMETER)
* [FIELD](/Java/ElementKind/FIELD)
* [INSTANCE_INIT](/Java/ElementKind/INSTANCE_INIT)
* [INTERFACE](/Java/ElementKind/INTERFACE)
* [LOCAL_VARIABLE](/Java/ElementKind/LOCAL_VARIABLE)
* [METHOD](/Java/ElementKind/METHOD)
* [MODULE](/Java/ElementKind/MODULE)
* [OTHER](/Java/ElementKind/OTHER)
* [PACKAGE](/Java/ElementKind/PACKAGE)
* [PARAMETER](/Java/ElementKind/PARAMETER)
* [RESOURCE_VARIABLE](/Java/ElementKind/RESOURCE_VARIABLE)
* [STATIC_INIT](/Java/ElementKind/STATIC_INIT)
* [TYPE_PARAMETER](/Java/ElementKind/TYPE_PARAMETER)

## Métodos
* [isClass()](/Java/ElementKind/isClass)
* [isField()](/Java/ElementKind/isField)
* [isInterface()](/Java/ElementKind/isInterface)
* [valueOf()](/Java/ElementKind/valueOf)
* [values()](/Java/ElementKind/values)

## Ejemplo
~~~java
{{ site.data.Java.E.ElementKind.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ElementKind.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
