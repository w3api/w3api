---
title: RemoteObject.toStub()
permalink: Java/RemoteObject/toStub
date: 2021-01-11
key: Java.R.RemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteObject.metodos valor="toStub" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Remote toStub(Remote obj) throws NoSuchObjectException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[RemoteObject](/Java/RemoteObject/)

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
