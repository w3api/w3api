---
title: ExtendedGSSCredential.impersonate()
permalink: Java/ExtendedGSSCredential/impersonate
date: 2021-01-11
key: JavaJava.E.ExtendedGSSCredential
category: java
tags: ['java se', 'com.sun.security.jgss', 'jdk.security.jgss', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtendedGSSCredential.metodos valor="impersonate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
GSSCredential impersonate(GSSName name) throws GSSException
~~~

## Parámetros
* **GSSName name**,  {% include w3api/param_description.html metodo=_dato parametro="GSSName name" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[ExtendedGSSCredential](/Java/ExtendedGSSCredential/)

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
