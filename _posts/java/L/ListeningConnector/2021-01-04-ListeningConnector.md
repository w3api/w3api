---
title: ListeningConnector
permalink: Java/ListeningConnector
date: 2021-01-04
key: JavaJava.L.ListeningConnector
category: java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.ListeningConnector.description }}

## Sintaxis
~~~java
public interface ListeningConnector extends Connector
~~~

## Métodos
* [accept()](/Java/ListeningConnector/accept)
* [startListening()](/Java/ListeningConnector/startListening)
* [stopListening()](/Java/ListeningConnector/stopListening)
* [supportsMultipleConnections()](/Java/ListeningConnector/supportsMultipleConnections)

## Ejemplo
~~~java
{{ site.data.Java.L.ListeningConnector.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListeningConnector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
