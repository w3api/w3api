---
title: InitialContext.composeName()
permalink: Java/InitialContext/composeName
date: 2021-01-11
key: JavaJava.I.InitialContext
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3', 'JNDI Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContext.metodos valor="composeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String composeName(String name, String prefix) throws NamingException
public Name composeName(Name name, Name prefix) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **Name prefix**,  {% include w3api/param_description.html metodo=_dato parametro="Name prefix" %}

## Excepciones
[NamingException](/Java/NamingException/)

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
