---
title: MultipleDocumentHandling
permalink: Java/MultipleDocumentHandling
date: 2021-01-11
key: JavaJava.M.MultipleDocumentHandling
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MultipleDocumentHandling.description }}

## Sintaxis
~~~java
public class MultipleDocumentHandling extends EnumSyntax implements PrintRequestAttribute, PrintJobAttribute
~~~

## Constructores
* [MultipleDocumentHandling()](/Java/MultipleDocumentHandling/MultipleDocumentHandling/)

## Campos
* [SEPARATE_DOCUMENTS_COLLATED_COPIES](/Java/MultipleDocumentHandling/SEPARATE_DOCUMENTS_COLLATED_COPIES)
* [SEPARATE_DOCUMENTS_UNCOLLATED_COPIES](/Java/MultipleDocumentHandling/SEPARATE_DOCUMENTS_UNCOLLATED_COPIES)
* [SINGLE_DOCUMENT](/Java/MultipleDocumentHandling/SINGLE_DOCUMENT)
* [SINGLE_DOCUMENT_NEW_SHEET](/Java/MultipleDocumentHandling/SINGLE_DOCUMENT_NEW_SHEET)

## Métodos
* [getCategory()](/Java/MultipleDocumentHandling/getCategory)
* [getEnumValueTable()](/Java/MultipleDocumentHandling/getEnumValueTable)
* [getName()](/Java/MultipleDocumentHandling/getName)
* [getStringTable()](/Java/MultipleDocumentHandling/getStringTable)

## Ejemplo
~~~java
{{ site.data.Java.M.MultipleDocumentHandling.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MultipleDocumentHandling.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
