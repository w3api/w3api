---
title: ExtendedGSSContext.requestDelegPolicy()
permalink: Java/ExtendedGSSContext/requestDelegPolicy
date: 2021-01-11
key: JavaJava.E.ExtendedGSSContext
category: java
tags: ['java se', 'com.sun.security.jgss', 'jdk.security.jgss', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtendedGSSContext.metodos valor="requestDelegPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void requestDelegPolicy(boolean state) throws GSSException
~~~

## Parámetros
* **boolean state**,  {% include w3api/param_description.html metodo=_dato parametro="boolean state" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[ExtendedGSSContext](/Java/ExtendedGSSContext/)

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
