---
title: ModuleElement.DirectiveVisitor
permalink: /Java/ModuleElement/DirectiveVisitor/
date: 2021-01-11
key: Java.M.ModuleElement.DirectiveVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModuleElement.DirectiveVisitor.description }}

## Sintaxis
~~~java
public static interface ModuleElement.DirectiveVisitor<R,P>
~~~

## Métodos
* [visit()](/Java/ModuleElement/DirectiveVisitor/visit)
* [visitExports()](/Java/ModuleElement/DirectiveVisitor/visitExports)
* [visitOpens()](/Java/ModuleElement/DirectiveVisitor/visitOpens)
* [visitProvides()](/Java/ModuleElement/DirectiveVisitor/visitProvides)
* [visitRequires()](/Java/ModuleElement/DirectiveVisitor/visitRequires)
* [visitUnknown()](/Java/ModuleElement/DirectiveVisitor/visitUnknown)
* [visitUses()](/Java/ModuleElement/DirectiveVisitor/visitUses)

## Ejemplo
~~~java
{{ site.data.Java.M.ModuleElement.DirectiveVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleElement.DirectiveVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
