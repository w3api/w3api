---
title: StartDocument
permalink: Java/StartDocument
date: 2021-01-11
key: JavaJava.S.StartDocument
category: java
tags: ['java se', 'javax.xml.stream.events', 'java.xml', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StartDocument.description }}

## Sintaxis
~~~java
public interface StartDocument extends XMLEvent
~~~

## Métodos
* [encodingSet()](/Java/StartDocument/encodingSet)
* [getCharacterEncodingScheme()](/Java/StartDocument/getCharacterEncodingScheme)
* [getSystemId()](/Java/StartDocument/getSystemId)
* [getVersion()](/Java/StartDocument/getVersion)
* [isStandalone()](/Java/StartDocument/isStandalone)
* [standaloneSet()](/Java/StartDocument/standaloneSet)

## Ejemplo
~~~java
{{ site.data.Java.S.StartDocument.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StartDocument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
