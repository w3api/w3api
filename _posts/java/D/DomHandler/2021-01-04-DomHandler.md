---
title: DomHandler
permalink: Java/DomHandler
date: 2021-01-04
key: JavaJava.D.DomHandler
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'interface java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DomHandler.description }}

## Sintaxis
~~~java
public interface DomHandler<ElementT,ResultT extends Result>
~~~

## Métodos
* [createUnmarshaller()](/Java/DomHandler/createUnmarshaller)
* [getElement()](/Java/DomHandler/getElement)
* [marshal()](/Java/DomHandler/marshal)

## Ejemplo
~~~java
{{ site.data.Java.D.DomHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DomHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
