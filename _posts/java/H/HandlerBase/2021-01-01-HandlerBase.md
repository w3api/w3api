---
title: HandlerBase
permalink: /Java/HandlerBase/
date: 2021-01-11
key: Java.H.HandlerBase
category: Java
tags: ['java se', 'org.xml.sax', 'java.xml', 'clase java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HandlerBase.description }}

## Sintaxis
~~~java
@Deprecated(since="1.5") public class HandlerBase extends Object implements EntityResolver, DTDHandler, DocumentHandler, ErrorHandler
~~~

## Constructores
* [HandlerBase()](/Java/HandlerBase/HandlerBase/)

## Métodos
* [characters()](/Java/HandlerBase/characters)
* [endDocument()](/Java/HandlerBase/endDocument)
* [endElement()](/Java/HandlerBase/endElement)
* [error()](/Java/HandlerBase/error)
* [fatalError()](/Java/HandlerBase/fatalError)
* [ignorableWhitespace()](/Java/HandlerBase/ignorableWhitespace)
* [notationDecl()](/Java/HandlerBase/notationDecl)
* [processingInstruction()](/Java/HandlerBase/processingInstruction)
* [resolveEntity()](/Java/HandlerBase/resolveEntity)
* [setDocumentLocator()](/Java/HandlerBase/setDocumentLocator)
* [startDocument()](/Java/HandlerBase/startDocument)
* [startElement()](/Java/HandlerBase/startElement)
* [unparsedEntityDecl()](/Java/HandlerBase/unparsedEntityDecl)
* [warning()](/Java/HandlerBase/warning)

## Ejemplo
~~~java
{{ site.data.Java.H.HandlerBase.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HandlerBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
