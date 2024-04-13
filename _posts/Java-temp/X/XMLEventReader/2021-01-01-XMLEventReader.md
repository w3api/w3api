---
title: XMLEventReader
permalink: /Java/XMLEventReader/
date: 2021-01-11
key: Java.X.XMLEventReader
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XMLEventReader.description }}

## Sintaxis
~~~java
public interface XMLEventReader extends Iterator<Object>
~~~

## Métodos
* [close()](/Java/XMLEventReader/close)
* [getElementText()](/Java/XMLEventReader/getElementText)
* [getProperty()](/Java/XMLEventReader/getProperty)
* [hasNext()](/Java/XMLEventReader/hasNext)
* [nextEvent()](/Java/XMLEventReader/nextEvent)
* [nextTag()](/Java/XMLEventReader/nextTag)
* [peek()](/Java/XMLEventReader/peek)

## Ejemplo
~~~java
{{ site.data.Java.X.XMLEventReader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLEventReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
