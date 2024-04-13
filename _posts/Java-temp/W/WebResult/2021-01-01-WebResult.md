---
title: WebResult
permalink: /Java/WebResult/
date: 2021-01-11
key: Java.W.WebResult
category: Java
tags: ['java se', 'javax.jws', 'java.xml.ws', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebResult.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(METHOD) public @interface WebResult
~~~

## Elementos
* [header](/Java/WebResult/header)
* [name](/Java/WebResult/name)
* [partName](/Java/WebResult/partName)
* [targetNamespace](/Java/WebResult/targetNamespace)

## Ejemplo
~~~java
{{ site.data.Java.W.WebResult.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
