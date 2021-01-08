---
title: WebMethod
permalink: Java/WebMethod
date: 2021-01-04
key: JavaJava.W.WebMethod
category: java
tags: ['java se', 'javax.jws', 'java.xml.ws', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebMethod.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(METHOD) public @interface WebMethod
~~~

## Elementos
* [action](/Java/WebMethod/action)
* [exclude](/Java/WebMethod/exclude)
* [operationName](/Java/WebMethod/operationName)

## Ejemplo
~~~java
{{ site.data.Java.W.WebMethod.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebMethod.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
