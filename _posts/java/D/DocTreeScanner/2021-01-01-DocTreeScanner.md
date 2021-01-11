---
title: DocTreeScanner
permalink: Java/DocTreeScanner
date: 2021-01-11
key: JavaJava.D.DocTreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocTreeScanner.description }}

## Sintaxis
~~~java
public class DocTreeScanner<R,P> extends Object implements DocTreeVisitor<R,P>
~~~

## Constructores
* [DocTreeScanner()](/Java/DocTreeScanner/DocTreeScanner/)

## Métodos
* [reduce()](/Java/DocTreeScanner/reduce)
* [scan()](/Java/DocTreeScanner/scan)
* [visitAttribute()](/Java/DocTreeScanner/visitAttribute)
* [visitAuthor()](/Java/DocTreeScanner/visitAuthor)
* [visitComment()](/Java/DocTreeScanner/visitComment)
* [visitDeprecated()](/Java/DocTreeScanner/visitDeprecated)
* [visitDocComment()](/Java/DocTreeScanner/visitDocComment)
* [visitDocRoot()](/Java/DocTreeScanner/visitDocRoot)
* [visitDocType()](/Java/DocTreeScanner/visitDocType)
* [visitEndElement()](/Java/DocTreeScanner/visitEndElement)
* [visitEntity()](/Java/DocTreeScanner/visitEntity)
* [visitErroneous()](/Java/DocTreeScanner/visitErroneous)
* [visitHidden()](/Java/DocTreeScanner/visitHidden)
* [visitIdentifier()](/Java/DocTreeScanner/visitIdentifier)
* [visitIndex()](/Java/DocTreeScanner/visitIndex)
* [visitInheritDoc()](/Java/DocTreeScanner/visitInheritDoc)
* [visitLink()](/Java/DocTreeScanner/visitLink)
* [visitLiteral()](/Java/DocTreeScanner/visitLiteral)
* [visitOther()](/Java/DocTreeScanner/visitOther)
* [visitParam()](/Java/DocTreeScanner/visitParam)
* [visitProvides()](/Java/DocTreeScanner/visitProvides)
* [visitReference()](/Java/DocTreeScanner/visitReference)
* [visitReturn()](/Java/DocTreeScanner/visitReturn)
* [visitSee()](/Java/DocTreeScanner/visitSee)
* [visitSerial()](/Java/DocTreeScanner/visitSerial)
* [visitSerialData()](/Java/DocTreeScanner/visitSerialData)
* [visitSerialField()](/Java/DocTreeScanner/visitSerialField)
* [visitSince()](/Java/DocTreeScanner/visitSince)
* [visitStartElement()](/Java/DocTreeScanner/visitStartElement)
* [visitSummary()](/Java/DocTreeScanner/visitSummary)
* [visitText()](/Java/DocTreeScanner/visitText)
* [visitThrows()](/Java/DocTreeScanner/visitThrows)
* [visitUnknownBlockTag()](/Java/DocTreeScanner/visitUnknownBlockTag)
* [visitUnknownInlineTag()](/Java/DocTreeScanner/visitUnknownInlineTag)
* [visitUses()](/Java/DocTreeScanner/visitUses)
* [visitValue()](/Java/DocTreeScanner/visitValue)
* [visitVersion()](/Java/DocTreeScanner/visitVersion)

## Ejemplo
~~~java
{{ site.data.Java.D.DocTreeScanner.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreeScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
