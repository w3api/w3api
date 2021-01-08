---
title: JMXAuthenticator.authenticate()
permalink: Java/JMXAuthenticator/authenticate
date: 2021-01-04
key: JavaJava.J.JMXAuthenticator
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXAuthenticator.metodos valor="authenticate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Subject authenticate(Object credentials)
~~~

## Parámetros
* **Object credentials**,  {% include w3api/param_description.html metodo=_data parametro="Object credentials" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[JMXAuthenticator](/Java/JMXAuthenticator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXAuthenticator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
