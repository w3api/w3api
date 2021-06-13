---
title: WebEndpoint
permalink: /Java/WebEndpoint/
date: 2021-01-11
key: Java.W.WebEndpoint
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebEndpoint.description }}

## Sintaxis
~~~java
@Target(METHOD) @Retention(RUNTIME) @Documented public @interface WebEndpoint
~~~

## Elementos
* [name](/Java/WebEndpoint/name)

## Ejemplo
~~~java
{{ site.data.Java.W.WebEndpoint.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebEndpoint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
