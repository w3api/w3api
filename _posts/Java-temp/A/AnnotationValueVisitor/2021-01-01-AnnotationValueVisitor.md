---
title: AnnotationValueVisitor
permalink: /Java/AnnotationValueVisitor/
date: 2021-01-11
key: Java.A.AnnotationValueVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AnnotationValueVisitor.description }}

## Sintaxis
~~~java
public interface AnnotationValueVisitor<R,P>
~~~

## Métodos
* [visit()](/Java/AnnotationValueVisitor/visit)
* [visitAnnotation()](/Java/AnnotationValueVisitor/visitAnnotation)
* [visitArray()](/Java/AnnotationValueVisitor/visitArray)
* [visitBoolean()](/Java/AnnotationValueVisitor/visitBoolean)
* [visitByte()](/Java/AnnotationValueVisitor/visitByte)
* [visitChar()](/Java/AnnotationValueVisitor/visitChar)
* [visitDouble()](/Java/AnnotationValueVisitor/visitDouble)
* [visitEnumConstant()](/Java/AnnotationValueVisitor/visitEnumConstant)
* [visitFloat()](/Java/AnnotationValueVisitor/visitFloat)
* [visitInt()](/Java/AnnotationValueVisitor/visitInt)
* [visitLong()](/Java/AnnotationValueVisitor/visitLong)
* [visitShort()](/Java/AnnotationValueVisitor/visitShort)
* [visitString()](/Java/AnnotationValueVisitor/visitString)
* [visitType()](/Java/AnnotationValueVisitor/visitType)
* [visitUnknown()](/Java/AnnotationValueVisitor/visitUnknown)

## Ejemplo
~~~java
{{ site.data.Java.A.AnnotationValueVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AnnotationValueVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
