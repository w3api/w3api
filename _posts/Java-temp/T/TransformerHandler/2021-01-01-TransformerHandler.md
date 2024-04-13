---
title: TransformerHandler
permalink: /Java/TransformerHandler/
date: 2021-01-11
key: Java.T.TransformerHandler
category: Java
tags: ['java se', 'javax.xml.transform.sax', 'java.xml', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransformerHandler.description }}

## Sintaxis
~~~java
public interface TransformerHandler extends ContentHandler, LexicalHandler, DTDHandler
~~~

## Métodos
* [getSystemId()](/Java/TransformerHandler/getSystemId)
* [getTransformer()](/Java/TransformerHandler/getTransformer)
* [setResult()](/Java/TransformerHandler/setResult)
* [setSystemId()](/Java/TransformerHandler/setSystemId)

## Ejemplo
~~~java
{{ site.data.Java.T.TransformerHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransformerHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
