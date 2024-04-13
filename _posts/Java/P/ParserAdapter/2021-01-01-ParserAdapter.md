---
title: ParserAdapter
permalink: /Java/ParserAdapter/
date: 2021-01-11
key: Java.P.ParserAdapter
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'clase java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.ParserAdapter.description }}

## Sintaxis
~~~java
public class ParserAdapter extends Object implements XMLReader, DocumentHandler
~~~

## Constructores
* [ParserAdapter()](/Java/ParserAdapter/ParserAdapter/)

## Métodos
* [characters()](/Java/ParserAdapter/characters/)
* [endDocument()](/Java/ParserAdapter/endDocument/)
* [endElement()](/Java/ParserAdapter/endElement/)
* [getContentHandler()](/Java/ParserAdapter/getContentHandler/)
* [getDTDHandler()](/Java/ParserAdapter/getDTDHandler/)
* [getEntityResolver()](/Java/ParserAdapter/getEntityResolver/)
* [getErrorHandler()](/Java/ParserAdapter/getErrorHandler/)
* [getFeature()](/Java/ParserAdapter/getFeature/)
* [getProperty()](/Java/ParserAdapter/getProperty/)
* [ignorableWhitespace()](/Java/ParserAdapter/ignorableWhitespace/)
* [parse()](/Java/ParserAdapter/parse/)
* [processingInstruction()](/Java/ParserAdapter/processingInstruction/)
* [setContentHandler()](/Java/ParserAdapter/setContentHandler/)
* [setDocumentLocator()](/Java/ParserAdapter/setDocumentLocator/)
* [setDTDHandler()](/Java/ParserAdapter/setDTDHandler/)
* [setEntityResolver()](/Java/ParserAdapter/setEntityResolver/)
* [setErrorHandler()](/Java/ParserAdapter/setErrorHandler/)
* [setFeature()](/Java/ParserAdapter/setFeature/)
* [setProperty()](/Java/ParserAdapter/setProperty/)
* [startDocument()](/Java/ParserAdapter/startDocument/)
* [startElement()](/Java/ParserAdapter/startElement/)

## Ejemplo
~~~java
{{ site.data.Java.P.ParserAdapter.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.ParserAdapter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
