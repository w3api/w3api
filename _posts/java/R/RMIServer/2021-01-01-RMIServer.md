---
title: RMIServer
permalink: Java/RMIServer
date: 2021-01-11
key: JavaJava.R.RMIServer
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RMIServer.description }}

## Sintaxis
~~~java
public interface RMIServer extends Remote
~~~

## Métodos
* [getVersion()](/Java/RMIServer/getVersion)
* [newClient()](/Java/RMIServer/newClient)

## Ejemplo
~~~java
{{ site.data.Java.R.RMIServer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
