---
title: HttpServer
permalink: /Java/HttpServer/
date: 2021-01-11
key: Java.H.HttpServer
category: Java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpServer.description }}

## Sintaxis
~~~java
public abstract class HttpServer extends Object
~~~

## Constructores
* [HttpServer()](/Java/HttpServer/HttpServer/)

## Métodos
* [bind()](/Java/HttpServer/bind)
* [create()](/Java/HttpServer/create)
* [createContext()](/Java/HttpServer/createContext)
* [getAddress()](/Java/HttpServer/getAddress)
* [getExecutor()](/Java/HttpServer/getExecutor)
* [removeContext()](/Java/HttpServer/removeContext)
* [setExecutor()](/Java/HttpServer/setExecutor)
* [start()](/Java/HttpServer/start)
* [stop()](/Java/HttpServer/stop)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpServer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
