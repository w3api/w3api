---
title: ConnectionEventListener
permalink: /Java/ConnectionEventListener/
date: 2021-01-11
key: Java.C.ConnectionEventListener
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConnectionEventListener.description }}

## Sintaxis
~~~java
public interface ConnectionEventListener extends EventListener
~~~

## Métodos
* [connectionClosed()](/Java/ConnectionEventListener/connectionClosed/)
* [connectionErrorOccurred()](/Java/ConnectionEventListener/connectionErrorOccurred/)

## Ejemplo
~~~java
{{ site.data.Java.C.ConnectionEventListener.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ConnectionEventListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
