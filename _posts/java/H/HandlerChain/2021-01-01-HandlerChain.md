---
title: HandlerChain
permalink: Java/HandlerChain
date: 2021-01-11
key: JavaJava.H.HandlerChain
category: java
tags: ['java se', 'javax.jws', 'java.xml.ws', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HandlerChain.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({TYPE,METHOD,FIELD}) public @interface HandlerChain
~~~

## Elementos
* [name](/Java/HandlerChain/name)

## Ejemplo
~~~java
{{ site.data.Java.H.HandlerChain.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HandlerChain.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
