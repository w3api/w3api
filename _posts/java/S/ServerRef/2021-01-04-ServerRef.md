---
title: ServerRef
permalink: Java/ServerRef
date: 2021-01-04
key: JavaJava.S.ServerRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServerRef.description }}

## Sintaxis
~~~java
@Deprecated public interface ServerRef extends RemoteRef
~~~

## Campos
* [serialVersionUID](/Java/ServerRef/serialVersionUID)

## Métodos
* [exportObject()](/Java/ServerRef/exportObject)
* [getClientHost()](/Java/ServerRef/getClientHost)

## Ejemplo
~~~java
{{ site.data.Java.S.ServerRef.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerRef.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
