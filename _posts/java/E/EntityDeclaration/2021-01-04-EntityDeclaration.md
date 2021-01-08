---
title: EntityDeclaration
permalink: Java/EntityDeclaration
date: 2021-01-04
key: JavaJava.E.EntityDeclaration
category: java
tags: ['java se', 'javax.xml.stream.events', 'java.xml', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EntityDeclaration.description }}

## Sintaxis
~~~java
public interface EntityDeclaration extends XMLEvent
~~~

## Métodos
* [getBaseURI()](/Java/EntityDeclaration/getBaseURI)
* [getName()](/Java/EntityDeclaration/getName)
* [getNotationName()](/Java/EntityDeclaration/getNotationName)
* [getPublicId()](/Java/EntityDeclaration/getPublicId)
* [getReplacementText()](/Java/EntityDeclaration/getReplacementText)
* [getSystemId()](/Java/EntityDeclaration/getSystemId)

## Ejemplo
~~~java
{{ site.data.Java.E.EntityDeclaration.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EntityDeclaration.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
