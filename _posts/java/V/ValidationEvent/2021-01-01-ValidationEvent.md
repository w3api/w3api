---
title: ValidationEvent
permalink: Java/ValidationEvent
date: 2021-01-11
key: JavaJava.V.ValidationEvent
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'interface java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.ValidationEvent.description }}

## Sintaxis
~~~java
public interface ValidationEvent
~~~

## Campos
* [ERROR](/Java/ValidationEvent/ERROR)
* [FATAL_ERROR](/Java/ValidationEvent/FATAL_ERROR)
* [WARNING](/Java/ValidationEvent/WARNING)

## Métodos
* [getLinkedException()](/Java/ValidationEvent/getLinkedException)
* [getLocator()](/Java/ValidationEvent/getLocator)
* [getMessage()](/Java/ValidationEvent/getMessage)
* [getSeverity()](/Java/ValidationEvent/getSeverity)

## Ejemplo
~~~java
{{ site.data.Java.V.ValidationEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.ValidationEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
