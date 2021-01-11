---
title: UnicastRemoteObject.clone()
permalink: Java/UnicastRemoteObject/clone
date: 2021-01-11
key: JavaJava.U.UnicastRemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UnicastRemoteObject.metodos valor="clone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object clone() throws CloneNotSupportedException
~~~

## Excepciones
[CloneNotSupportedException](/Java/CloneNotSupportedException/)

## Clase Padre
[UnicastRemoteObject](/Java/UnicastRemoteObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
