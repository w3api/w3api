---
title: DefaultHandler
permalink: Java/DefaultHandler
date: 2021-01-11
key: JavaJava.D.DefaultHandler
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'clase java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultHandler.description }}

## Sintaxis
~~~java
public class DefaultHandler extends Object implements EntityResolver, DTDHandler, ContentHandler, ErrorHandler
~~~

## Constructores
* [DefaultHandler()](/Java/DefaultHandler/DefaultHandler/)

## Métodos
* [characters()](/Java/DefaultHandler/characters)
* [endDocument()](/Java/DefaultHandler/endDocument)
* [endElement()](/Java/DefaultHandler/endElement)
* [endPrefixMapping()](/Java/DefaultHandler/endPrefixMapping)
* [error()](/Java/DefaultHandler/error)
* [fatalError()](/Java/DefaultHandler/fatalError)
* [ignorableWhitespace()](/Java/DefaultHandler/ignorableWhitespace)
* [notationDecl()](/Java/DefaultHandler/notationDecl)
* [processingInstruction()](/Java/DefaultHandler/processingInstruction)
* [resolveEntity()](/Java/DefaultHandler/resolveEntity)
* [setDocumentLocator()](/Java/DefaultHandler/setDocumentLocator)
* [skippedEntity()](/Java/DefaultHandler/skippedEntity)
* [startDocument()](/Java/DefaultHandler/startDocument)
* [startElement()](/Java/DefaultHandler/startElement)
* [startPrefixMapping()](/Java/DefaultHandler/startPrefixMapping)
* [unparsedEntityDecl()](/Java/DefaultHandler/unparsedEntityDecl)
* [warning()](/Java/DefaultHandler/warning)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
