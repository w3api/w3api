---
title: LogicalHandler
permalink: Java/LogicalHandler
date: 2021-01-04
key: JavaJava.L.LogicalHandler
category: java
tags: ['java se', 'javax.xml.ws.handler', 'java.xml.ws', 'interface java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LogicalHandler.description }}

## Sintaxis
~~~java
public interface LogicalHandler<C extends LogicalMessageContext> extends Handler<C>
~~~

## Ejemplo
~~~java
{{ site.data.Java.L.LogicalHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LogicalHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
