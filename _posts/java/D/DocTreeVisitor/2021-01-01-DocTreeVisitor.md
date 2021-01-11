---
title: DocTreeVisitor
permalink: Java/DocTreeVisitor
date: 2021-01-11
key: JavaJava.D.DocTreeVisitor
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocTreeVisitor.description }}

## Sintaxis
~~~java
public interface DocTreeVisitor<R,P>
~~~

## Métodos
* [visitAttribute()](/Java/DocTreeVisitor/visitAttribute)
* [visitAuthor()](/Java/DocTreeVisitor/visitAuthor)
* [visitComment()](/Java/DocTreeVisitor/visitComment)
* [visitDeprecated()](/Java/DocTreeVisitor/visitDeprecated)
* [visitDocComment()](/Java/DocTreeVisitor/visitDocComment)
* [visitDocRoot()](/Java/DocTreeVisitor/visitDocRoot)
* [visitDocType()](/Java/DocTreeVisitor/visitDocType)
* [visitEndElement()](/Java/DocTreeVisitor/visitEndElement)
* [visitEntity()](/Java/DocTreeVisitor/visitEntity)
* [visitErroneous()](/Java/DocTreeVisitor/visitErroneous)
* [visitHidden()](/Java/DocTreeVisitor/visitHidden)
* [visitIdentifier()](/Java/DocTreeVisitor/visitIdentifier)
* [visitIndex()](/Java/DocTreeVisitor/visitIndex)
* [visitInheritDoc()](/Java/DocTreeVisitor/visitInheritDoc)
* [visitLink()](/Java/DocTreeVisitor/visitLink)
* [visitLiteral()](/Java/DocTreeVisitor/visitLiteral)
* [visitOther()](/Java/DocTreeVisitor/visitOther)
* [visitParam()](/Java/DocTreeVisitor/visitParam)
* [visitProvides()](/Java/DocTreeVisitor/visitProvides)
* [visitReference()](/Java/DocTreeVisitor/visitReference)
* [visitReturn()](/Java/DocTreeVisitor/visitReturn)
* [visitSee()](/Java/DocTreeVisitor/visitSee)
* [visitSerial()](/Java/DocTreeVisitor/visitSerial)
* [visitSerialData()](/Java/DocTreeVisitor/visitSerialData)
* [visitSerialField()](/Java/DocTreeVisitor/visitSerialField)
* [visitSince()](/Java/DocTreeVisitor/visitSince)
* [visitStartElement()](/Java/DocTreeVisitor/visitStartElement)
* [visitSummary()](/Java/DocTreeVisitor/visitSummary)
* [visitText()](/Java/DocTreeVisitor/visitText)
* [visitThrows()](/Java/DocTreeVisitor/visitThrows)
* [visitUnknownBlockTag()](/Java/DocTreeVisitor/visitUnknownBlockTag)
* [visitUnknownInlineTag()](/Java/DocTreeVisitor/visitUnknownInlineTag)
* [visitUses()](/Java/DocTreeVisitor/visitUses)
* [visitValue()](/Java/DocTreeVisitor/visitValue)
* [visitVersion()](/Java/DocTreeVisitor/visitVersion)

## Ejemplo
~~~java
{{ site.data.Java.D.DocTreeVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
