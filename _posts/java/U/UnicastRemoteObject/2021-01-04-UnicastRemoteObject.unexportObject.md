---
title: UnicastRemoteObject.unexportObject()
permalink: Java/UnicastRemoteObject/unexportObject
date: 2021-01-04
key: JavaJava.U.UnicastRemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UnicastRemoteObject.metodos valor="unexportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean unexportObject(Remote obj, boolean force) throws NoSuchObjectException
~~~

## Parámetros
* **boolean force**,  {% include w3api/param_description.html metodo=_data parametro="boolean force" %}
* **Remote obj**,  {% include w3api/param_description.html metodo=_data parametro="Remote obj" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[UnicastRemoteObject](/Java/UnicastRemoteObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnicastRemoteObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
