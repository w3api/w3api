---
title: Principal.implies()
permalink: Java/Principal-java-security/implies
date: 2021-01-04
key: JavaJava.P.Principal-java-security
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Principal-java-security.metodos valor="implies" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean implies(Subject subject)
~~~

## Parámetros
* **Subject subject**,  {% include w3api/param_description.html metodo=_data parametro="Subject subject" %}

## Clase Padre
[Principal](/Java/Principal-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Principal-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
