---
title: InitialContext.doLookup()
permalink: /Java/InitialContext/doLookup/
date: 2021-01-11
key: Java.I.InitialContext
category: Java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3', 'JNDI Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContext.metodos valor="doLookup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T doLookup(String name)
static <T> T doLookup(Name name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}

## Clase Padre
[InitialContext](/Java/InitialContext/)

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
