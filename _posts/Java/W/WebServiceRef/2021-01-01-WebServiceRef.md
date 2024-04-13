---
title: WebServiceRef
permalink: /Java/WebServiceRef/
date: 2021-01-11
key: Java.W.WebServiceRef
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebServiceRef.description }}

## Sintaxis
~~~java
@Target({TYPE,METHOD,FIELD}) @Retention(RUNTIME) @Documented @Repeatable(WebServiceRefs.class) public @interface WebServiceRef
~~~

## Elementos
* [lookup](/Java/WebServiceRef/lookup)
* [mappedName](/Java/WebServiceRef/mappedName)
* [name](/Java/WebServiceRef/name)
* [type](/Java/WebServiceRef/type)
* [value](/Java/WebServiceRef/value)
* [wsdlLocation](/Java/WebServiceRef/wsdlLocation)

## Ejemplo
~~~java
{{ site.data.Java.W.WebServiceRef.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebServiceRef.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
