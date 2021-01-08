---
title: ElementVisitor
permalink: Java/ElementVisitor
date: 2021-01-04
key: JavaJava.E.ElementVisitor
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ElementVisitor.description }}

## Sintaxis
~~~java
public interface ElementVisitor<R,P>
~~~

## Métodos
* [visit()](/Java/ElementVisitor/visit)
* [visitExecutable()](/Java/ElementVisitor/visitExecutable)
* [visitModule()](/Java/ElementVisitor/visitModule)
* [visitPackage()](/Java/ElementVisitor/visitPackage)
* [visitType()](/Java/ElementVisitor/visitType)
* [visitTypeParameter()](/Java/ElementVisitor/visitTypeParameter)
* [visitUnknown()](/Java/ElementVisitor/visitUnknown)
* [visitVariable()](/Java/ElementVisitor/visitVariable)

## Ejemplo
~~~java
{{ site.data.Java.E.ElementVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ElementVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
