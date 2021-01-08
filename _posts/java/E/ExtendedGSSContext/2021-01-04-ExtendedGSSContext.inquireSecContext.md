---
title: ExtendedGSSContext.inquireSecContext()
permalink: Java/ExtendedGSSContext/inquireSecContext
date: 2021-01-04
key: JavaJava.E.ExtendedGSSContext
category: java
tags: ['java se', 'com.sun.security.jgss', 'jdk.security.jgss', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtendedGSSContext.metodos valor="inquireSecContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object inquireSecContext(InquireType type) throws GSSException
~~~

## Parámetros
* **InquireType type**,  {% include w3api/param_description.html metodo=_data parametro="InquireType type" %}

## Excepciones
[GSSException](/Java/GSSException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ExtendedGSSContext](/Java/ExtendedGSSContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExtendedGSSContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
