---
title: SocketOptions.getOption()
permalink: /Java/SocketOptions/getOption/
date: 2021-01-11
key: Java.S.SocketOptions
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketOptions.metodos valor="getOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getOption(int optID) throws SocketException
~~~

## Parámetros
* **int optID**,  {% include w3api/param_description.html metodo=_dato parametro="int optID" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[SocketOptions](/Java/SocketOptions/)

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
