---
title: GSSContext.requestLifetime()
permalink: Java/GSSContext/requestLifetime
date: 2021-01-04
key: JavaJava.G.GSSContext
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSContext.metodos valor="requestLifetime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void requestLifetime(int lifetime) throws GSSException
~~~

## Parámetros
* **int lifetime**,  {% include w3api/param_description.html metodo=_data parametro="int lifetime" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSContext](/Java/GSSContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GSSContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
